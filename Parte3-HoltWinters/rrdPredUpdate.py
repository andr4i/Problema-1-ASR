import time
import rrdtool
import datetime
from getSNMP import consultaSNMP
#from Notify import check_aberration
total_input_traffic = 0
from path import *

fname=rrdpath+rrdname
# Generate charts for last 24 hours
endDate = rrdtool.last(fname) #ultimo valor del XML
begDate = endDate - 3600
while 1:
    # total_input_traffic = int(consultaSNMP('comunidadASR','localhost','1.3.6.1.2.1.2.2.1.10.1'))
    total_input_traffic = int(consultaSNMP('comunidadASR', '192.168.100.5', '1.3.6.1.2.1.2.2.1.10.11'))
    print(rrdtool.lastupdate(fname))
    # valor = rrdtool.lastupdate(fname)+1 +str(total_input_traffic)
    # valor = rrdtool.lastupdate(fname)
    # valor["date"] = valor["date"] + datetime.timedelta(seconds = 1)
    # valor["ds"]["inoctets"] = total_input_traffic
    # print(valor)
    # print(valor.get("ds"))
    valor2 = "N:" + str(total_input_traffic)
    ret = rrdtool.update(fname, valor2)
    rrdtool.dump(fname,'pred.xml')
    time.sleep(1)
#    print (check_aberration(rrdpath,rrdname))
if ret:
    print (rrdtool.error())
    time.sleep(300)
