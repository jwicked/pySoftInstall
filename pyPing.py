import wmi
import win32com.client

wmiObj = win32com.client.GetObject(r"winmgmts:\\.\root\cimv2")

#Ping the host to see if we should even attempt the installation
def py_ping(host):
    print("Pinging Host: "+host)
    col_items = wmiObj.ExecQuery("Select * from Win32_PingStatus Where Address = '%s'" % host)
    for item in col_items:
        return item.StatusCode