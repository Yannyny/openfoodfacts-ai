from typing import Dict
import requests
from models.base import BaseModel

from joblib import Memory

memory = Memory("~/.joblib", verbose=0)


URL = "https://robotoff.openfoodfacts.org/api/v1/predict/ingredients/spellcheck"


class RobotoffAPIModel(BaseModel):
    def __init__(self, index="product", confidence=1):
        super(RobotoffAPIModel, self).__init__()
        self.index = index
        self.confidence = confidence

    @property
    def name(self):
        return f"RobotoffAPI__index_{self.index}__conf_{self.confidence}"

    def apply_one(self, text: str) -> str: #[self.apply_one(item["original"]) for item in items]
        return get_correction(text, self.get_params(text=text)) #index="product", confidence=1

    def get_params(self, **kwargs):
        return {**kwargs, "index": self.index, "confidence": self.confidence}


@memory.cache
def get_correction(text: str, params: Dict) -> str:
    try:
        #print(params)
        r = requests.get(URL, params=params)
        #print(r.url)
        data = r.json()
        if data["corrected"] != "":
            return data["corrected"]
        else:
            return data["text"]
    except Exception:
        return "FAILURE"
