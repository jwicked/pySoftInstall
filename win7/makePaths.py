import settings
import os

def make_machine_path(host):
    unc_slash = r"\\"
    unc_machine = os.path.join(unc_slash, host, settings.MWI_share)
    return unc_machine

#build paths to media and destination
def make_software_source(soft, version):
    software_folder = os.path.join(soft, version)
    software_source = os.path.join(settings.share_root, software_folder)
    return software_source

def make_folder_destination(unc_machine_share, soft, version):
    software_folder = os.path.join(soft, version)
    folderDestination = os.path.join(unc_machine_share, software_folder)
    return folderDestination

def make_ini_source(unc_machine_share, soft, version, ini):
    ini_source = os.path.join(soft, version, ini)
    iniFileSource = os.path.join(unc_machine_share, ini_source)
    return iniFileSource

def make_ini_destination(unc_machine_share):
    iniFileDestination = os.path.join(unc_machine_share, settings.INI_Destination_Loc)
    return iniFileDestination

def make_machine_root_path(host):
    unc_slash = r"\\"
    machine_root = unc_slash+host
    return machine_root