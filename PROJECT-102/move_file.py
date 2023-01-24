import os
import shutil

from_dir = "downloads"
to_dir = "document_files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

# Move All Image files from Downloads Folder to Another Folder
for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)

    if extension == '':
        continue
    if extension in ['.gif','.png','.jpg','.jpeg','.jfif']:

        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "documents_files"
        path3 = to_dir + '/' + "documents_files" + '/' + file_name

        # Check if Folder/Directory Path Exists Before Moving
        # Else make a NEW Folder/Directory Then Move
        if os.path.exists(path2):
            print("Moving" + file_name + "......")

            # Move from path1 ---> path3
            shutil.move(path1, path3)

        else:
            os.makedirs(path2)
            print("moving" + file_name + ".....")
            shutil.move(path1, path3)    