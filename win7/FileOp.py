import os
import shutil

class FileOps:
    def __init__(self):
        pass
    
    def open_file_r(self, inputFile):
        try:
            os.path.isfile(inputFile)
            self.file = open(inputFile,"r")
        except:
            print("Cannot find file. Exiting.")
            exit()
            
    def open_file_w(self, inputFile):
        try:
            os.path.isfile(inputFile)
            self.file = open(inputFile,"w")
        except:
            print("Cannot find file. Exiting.")
            exit()    

    def closeFile(self, inFile):
        self.file.close()
        
    def read_assets(self, inFile):
        asset_names = []
        for asset_name in self.file:
            asset = asset_name.strip()
            asset_names.append(asset)
        return asset_names
        
    def copyFile(self, fileSource, fileDestination):
        try:
            if os.path.isfile(fileSource):
                shutil.copy(fileSource, fileDestination)
                print("File copied.")
                return True
            else:
                pass
        except:
            print("Cannot find file. Exiting.")
            exit()
            
    def moveFile(self, fileSource, fileDestination):
        try:
            if os.path.isfile(fileSource):
                shutil.move(fileSource, fileDestination)
                print("File Moved.")
                return True
            else:
                pass
        except:
            print("Cannot find File. Exiting.")
            exit()