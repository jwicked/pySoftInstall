import os
import shutil

class FolderOp:
#Copys source directory to destination directory(pcName), 
#will error if dest already exists
#TODO: try and handle error gracefully instead of causing program halt
#try to provide a status of the copy process if possible
#account for each file and copy the files that are not there
    def copyFolder(self, folderSource, folderDestination):
        if os.path.exists(folderDestination):
            print("Unable to copy folder. Already exists on local machine. Trying install.")
            return True
        else:
            try:
                print("Copying media to local machine.")
                shutil.copytree(folderSource, folderDestination)
                print("Folder copied.")
                return True

            except:
                print("Unable to copy.")
                return False

        def copyFile(fileSource, fileDestination):
            try:
                shutil.copy(fileSource, fileDestination)
                print("File copied.")
                return True
            except:
                print("Unable to copy file.")
                return False
            
    def folderExist(self, folder):
        if os.path.exists(folder):
            return True
        else:
            return False       