import os
import win32com.client
import shutil
import subprocess
import datetime
import time

##############################################################

#Copys source directory to destination directory(pcName), will error if dest already exists
#TODO: try and handle error gracefully instead of causing program halt
#Also try to provide a status of the copy process if possible
#account for each file and copy the files that are not there
def copySoftTo(pcName):
    srcSoftPath = r'\\frkfnabk1\support\non-standard\VBLib'
    destSoftPath = pcName+r'\c$\Windows\installer\MWI\VBLibs'
    
    print("Copying Software to: " + pcName +"\n")
    try:
        shutil.copytree(srcSoftPath, destSoftPath)
        fout.write("Software Copied,")
        print("Software Copied\n")
        return True

    except:
        print("Unable to copy software")
        return False
    

#Checks to see if software source exists on remote PC(assetInstallPath) by checking for source folder
#if the directory exists it will return false
def checkSoftExist(assetInstallPath):
    if os.path.exists(assetInstallPath):
        print("Install Source Found\n")
        return False
    else:
        print("Install Source Not found\n")
        return True

#Uses PSEXEC tool from microsoft to run a remote process to install the software.
#TODO need a way to timeout this process just incase it gets hung
#find away to provide a status update to output
def installSoft(pcName):
    print("Installing Software\n")
        
    srcVBE = pcName+r'\c$\Windows\installer\MWI\VBLibs\VBE6.DLL'
    destVBE = pcName+r'/c$/Program Files/Common Files/Microsoft Shared/VBA/VBA6/VBE6.DLL'
    srcOCX = pcName+r'\c$\Windows\installer\MWI\VBLibs\mscomct2.ocx'
    destOCX = pcName+r'\c$\Windows\system32\mscomct2.ocx'
    
    cmd = r'f:\pstools\PsExec '+pcName+r' c:\Windows\installer\mwi\vbLibs\GAVBLibs.bat'

##    copyVBE = r' move "c:\winnt\installer\mwi\VBLibs\mscomct2.ocx" "c:\winnt\system32\" /Y'
##    copyOCX = r' move c:\winnt\installer\mwi\VBLibs\VBE6.DLL "C:\Program Files\Common Files\Microsoft Shared\VBA\VBA6\" /Y'
##    installcmd1 = r' RegSvr32 /u /s "c:\winnt\system32\mscomct2.ocx"'
##    installcmd2 = r' RegSvr32 /s "c:\winnt\system32\mscomct2.ocx"'
##    installcmd3 = r' RegSvr32 /u /s "C:\Program Files\Common Files\Microsoft Shared\VBA\VBA6\VBE6.DLL"'
##    installcmd4 = r' RegSvr32 /s "C:\Program Files\Common Files\Microsoft Shared\VBA\VBA6\VBE6.DLL"'

##    print(cmd+copyVBE)
##    if subprocess.call(cmd+copyVBE) == 0:
##        fout.write("VBE Copied\n")
##    else:
##        fout.write("VBE Copy failed\n")
##        
##    if subprocess.call(cmd+copyOCX) == 0:
##        fout.write("ocx Copied\n")
##    else:
##        fout.write("ocx Copy failed\n")
##
##    if subprocess.call(cmd+installcmd1) == 0:
##        fout.write("ocx unreg\n")
##    else:
##        fout.write("ocx unreg failed\n")
##        
##    if subprocess.call(cmd+installcmd2) == 0:
##        fout.write("ocx reg\n")
##    else:
##        fout.write("ocx reg failed\n")
##        
##    if subprocess.call(cmd+installcmd3) == 0:
##        fout.write("dll unreg\n")
##    else:
##        fout.write("dll unreg failed\n")
        
    if subprocess.call(cmd) == 0:
        fout.write("reg\n")
    else:
        fout.write("reg failed\n")
    
#Ping the host to see if we should even attempt the installation
def ping(host):
    print("Pinging Host\n")
    col_items = wmi.ExecQuery("Select * from Win32_PingStatus Where Address = '%s'" % host)
    for item in col_items:
        return item.StatusCode

#Write to log the name of the host we are running against
def log_tran(assetNum):
    fout.write(assetNum.strip() + ",")


##################################################

wmi = win32com.client.GetObject(r"winmgmts:\\.\root\cimv2")
installFilePath = input("Enter file name for installs: ")

logFile = r"VBLibInstall.csv"
fout = open(logFile, "a")
dateRun = time.asctime(time.localtime(time.time()) )

try:
    os.path.isfile(installFilePath)
    inFile = open(installFilePath,"r")
except:
    print("Cannot find file. Exiting.")
    exit()

fout.write("\nPC,Status," + dateRun + "\n")

while True:
    assetNum = inFile.readline()
    if assetNum == "":
        break
    pcName = r"\\"+assetNum.strip()
    #pcName = assetNum.strip()
    host = assetNum.strip()
    #host = assetNum.strip()
    print("Checking host: "+host)
    
    assetInstallPath = pcName+r'\c$\Windows\installer\MWI\VBLibs'

    log_tran(assetNum)
    if ping(host) != 0:
        fout.write("Host Unavailable\n")
        print("Host Unavailable\n")
        continue
    if checkSoftExist(assetInstallPath) == False:
        installSoft(pcName)
        continue
    else:
        if copySoftTo(pcName) == True:
            installSoft(pcName)
            #rebootPC(pcName)
        else:
            fout.write("Error copying software\n")
            print("Error copying software")
              
        
print("Completed Sucessfully")
inFile.close()
fout.close()
