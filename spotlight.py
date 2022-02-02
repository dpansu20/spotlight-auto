from shutil import copy2
from os import listdir, rename, remove, getenv
from os.path import isfile, join, exists, normpath, expandvars
import subprocess

FILEBROWSER_PATH = join(getenv('WINDIR'), 'explorer.exe')

src_dir = expandvars(r'%LocalAppData%/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets')
target_dir = 'E:/Spotlight'

if __name__ == "__main__":
    if exists(src_dir):             # check if source directory exists

        src_files = listdir(src_dir)

        print("Reading files....\n")

        count = 0
        for f in src_files:     # prints all the file names which are fetched
            count += 1
            print(str(count) + " => \'" + f + "\'")

        print('\n')
        
        if exists(target_dir):      # check if target directory exists

            subprocess.run([FILEBROWSER_PATH, normpath(target_dir)])    # open explorer in target folder

            print("Copying files....\n")

            for f in src_files:
                if exists(join(target_dir, f)):
                    print("File already exist " + "\'" + f + "\'")
                else:
                    copy2(join(src_dir, f), join(target_dir, f))    # starts copying files, if it does not already exist
                    print("Copied \'" + f + "\'")

            print("\n")

            # target_files = listdir(target_dir)    # lists all files and folders
            # lists only files (and those NOT containg the .jpg extension)
            target_files = [f for f in listdir(target_dir) if isfile(join(target_dir, f)) and not f[-4:] == ".jpg"]

            for f in target_files:
                
                file_name = f + ".jpg"

                if exists(join(target_dir, file_name)):
                    remove(join(target_dir, f))
                    print("Removed \'" + f + "\' as its .jpg already exists")
                else:
                    rename(join(target_dir, f), join(target_dir, file_name))    # converts files to .jpg, if .jpg of their original names does not already exist
                    print("Renamed \'" + file_name + "\'")