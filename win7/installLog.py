#Write to log the name of the host we are running against
def log_tran(assetNum):
    fout.write(assetNum.strip() + ",")
logFile = r"QualityCenter10_5_Install.csv"

fout = open(logFile, "a")
dateRun = time.asctime(time.localtime(time.time()) )

fout.write("\nPC,Status," + dateRun + "\n")

    log_tran(assetNum)