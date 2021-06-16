import shutil, os, glob

path_to_target = './nutrition-lc-fr-country-fr-last-edit-date-2019-08/'

cropped_image_files_list = glob.glob(path_to_target + '*cropped.jpg')
cropped_image_files_list_def = [i.split('/')[-1] for i in cropped_image_files_list]
for file in cropped_image_files_list_def:
    shutil.move(file, './cropped_images')

image_files_list = glob.glob(path_to_target + '*nutrition.jpg')
image_files_list_def = [i.split('/')[-1] for i in image_files_list]
for file in image_files_list_def:
    shutil.move(file, './image_files')

json_files_list = glob.glob(path_to_target + '*nutriments.json')
json_files_list_def = [i.split('/')[-1] for i in json_files_list]
for file in json_files_list_def:
    shutil.move(file, './json_files')

cropped_json_files_list = glob.glob(path_to_target + '*cropped.json')
cropped_json_files_list_def = [i.split('/')[-1] for i in cropped_json_files_list]
for file in cropped_json_files_list_def:
    shutil.move(file, './cropped_json_files')


