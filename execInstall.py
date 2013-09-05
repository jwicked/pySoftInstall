import subprocess
import settings
import os

#Uses PSEXEC tool from microsoft to run a remote process to install the software.
#TODO need a way to timeout this process just incase it gets hung
#find away to provide a status update to output
def installSoft(host, inifile):
    print("Installing Software\n")
    
    cmd = settings.psexec_loc+" "+host+" "
    inifile_location = os.path.join(settings.MWI_dir, settings.INI_Destination_Loc, inifile)
    wrapper_run = settings.Wrapper+" "+inifile_location+" /a"
    print(cmd+wrapper_run)

    if subprocess.call(cmd+wrapper_run) == 0:
        print("Software installed\n")
    else:
        print("Software install failed\n")


def uninstallSoft(host, inifile):
    print("Installing Software\n")
    
    cmd = settings.psexec_loc+" "+host+" "
    inifile_location = os.path.join(settings.MWI_dir, settings.INI_Destination_Loc, inifile)
    wrapper_run = settings.Wrapper+" "+inifile_location+" /u"
    print(cmd+wrapper_run)

    if subprocess.call(cmd+wrapper_run) == 0:
        print("Software uninstalled\n")
    else:
        print("Software uninstall failed\n")
