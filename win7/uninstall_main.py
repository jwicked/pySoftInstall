import FileOp
import MakePCName
import SoftIDQuery
import pyPing
import settings
import FolderOps
import makePaths
import execInstall

##############################################################
inputfile = FileOp.FileOps()
folder = FolderOps.FolderOp()
inifile = FileOp.FileOps()

softid = input("Please enter Software ID: ")
inFile = input("Enter file name for installs: ")

#Open a file and read asset tags from it
inputfile.open_file_r(inFile)                   
asset_list = inputfile.read_assets(inFile)
host_list  = []
for asset in asset_list:
    #convert the asset tag into a host name
    hostName = MakePCName.make_pc_name(asset)
    host_list.append(hostName)
inputfile.closeFile(inFile)


for host in host_list:
    #ping the host to see if alive
    if pyPing.py_ping(host) != 0:
        print(host+" unavailable- skipping.")
        continue
    else:
        #Query Software Database and get software information
        software = SoftIDQuery.query_software_db(softid)
        software_id = software[0]
        software_name = software[1]
        software_version = software[2]
        ini_information = software[3]
        
        
        #build paths to media and destination
        unc_machine_share = makePaths.make_machine_path(host)
        software_source = makePaths.make_software_source(software_name, software_version)
        software_destination = makePaths.make_folder_destination(unc_machine_share, software_name, software_version)
        ini_file_source = makePaths.make_ini_source(unc_machine_share, software_name, software_version, ini_information)
        ini_file_destination = makePaths.make_ini_destination(unc_machine_share)
        machine_root = makePaths.make_machine_root_path(host)
        
        #Begin copy of media folder to machine
        if folder.copyFolder(software_source, software_destination) == True:
            if inifile.copyFile(ini_file_source, ini_file_destination) == True:
                execInstall.uninstallSoft(machine_root, ini_information)
            else:
                pass
        else:
            execInstall.uninstallSoft(machine_root, ini_information)
