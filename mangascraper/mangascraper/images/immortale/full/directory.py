import os


files_list = os.listdir('.')
base_path = os.getcwd()
for f in files_list:
    if f.split('.')[1] in ['py','pyc']:
        continue
    chapter_folder_name = f.split('-')[0]
    folder_chapter = 'Capitolo ' + chapter_folder_name
    folder_path = base_path + "/" + folder_chapter
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    file_path = base_path + "/" + f
    new_file_path = folder_path + "/" + f
    os.rename(file_path, new_file_path)
