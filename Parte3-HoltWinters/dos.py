import csv
import time
from datetime import datetime
from getSNMP import consultaSNMP


def now():
    return datetime.now().strftime('%d.%m.%Y %H:%M:%S')

check = 0
nuevo = 0
diferencia = 0
anterior = 0
header = ["Date","Packdiff"]
while 1:
    total_input_traffic = int(consultaSNMP('comunidadASR', 'localhost', '1.3.6.1.2.1.2.2.1.10.1'))
    if(check==0):
        col = []
        col.append(str(now()))
        col.append(str(diferencia))
        with open("valores.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerow(col)
            nuevo = total_input_traffic
            check = 1
    else:
        if(nuevo<total_input_traffic):
            diferencia = total_input_traffic - nuevo
            nuevo = total_input_traffic
            col = []
            col.append(str(now()))
            col.append(str(diferencia))
            with open("valores.csv", "a") as file:
                writer = csv.writer(file)
                writer.writerow(col)
        else:
            col = []
            col.append(str(now()))
            col.append(str(diferencia))
            with open("valores.csv", "a") as file:
                writer = csv.writer(file)
                writer.writerow(col)
    time.sleep(1)


