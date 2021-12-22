import rrdtool
from Notify import send_alert_attached
import time

def grafica1():

    rrdpath = '/home/gonzalo/PycharmProjects/Introduccion_SNMP/4-AdministraciónDeRendimiento/RRD/'
    imgpath = '/home/gonzalo/PycharmProjects/Introduccion_SNMP/4-AdministraciónDeRendimiento/IMG/'
    fname = 'trend.rrd'
    ultima_lectura = int(rrdtool.last(rrdpath+fname))
    tiempo_final = ultima_lectura
    tiempo_inicial = tiempo_final - 500

    ret = rrdtool.graph( imgpath+"trend.png",
                         "--start",str(tiempo_inicial),
                         "--end",str(tiempo_final),
                         "--vertical-label=Carga CPU",
                         "--title=Tendencia del uso del CPU",
                         "--color", "ARROW#009900",
                         '--vertical-label', "Uso de CPU (%)",
                         '--lower-limit', '0',
                         '--upper-limit', '100',
                         "DEF:carga="+rrdpath+"trend.rrd:CPUload:AVERAGE",
                         "AREA:carga#00FF00:Carga CPU",
                         "LINE1:30",
                         "AREA:5#ff000022:stack",
                         "VDEF:CPUlast=carga,LAST",
                         "VDEF:CPUmin=carga,MINIMUM",
                         "VDEF:CPUavg=carga,AVERAGE",
                         "VDEF:CPUmax=carga,MAXIMUM",
                         "PRINT:CPUlast:%6.2lf",
                        "COMMENT:Now          Min             Avg             Max",
                         "GPRINT:CPUlast:%12.0lf%s",
                         "GPRINT:CPUmin:%10.0lf%s",
                         "GPRINT:CPUavg:%13.0lf%s",
                         "GPRINT:CPUmax:%13.0lf%s",
                         "VDEF:m=carga,LSLSLOPE",
                         "VDEF:b=carga,LSLINT",
                         'CDEF:tendencia=carga,POP,m,COUNT,*,b,+',
                         "VDEF:ULTIMO=tendencia,LAST",
                         "PRINT:ULTIMO:%6.2lf",
                         'CDEF:tendencia2=carga,m,*,b,+',
                         "LINE2:tendencia#FFBB00"
                         )

    print(ret)
    ultimo_valor=str(ret[2])
    print(ultimo_valor)
    #Almacenamos el valor del ultimo elemento de la predicción en cadena
    xvalor = str(ultimo_valor[13:18])
    #Guardamos ese valor en entero.
    xvalor = float(xvalor)
    xvalor = int(xvalor)
    print(xvalor)
    return xvalor
    # if (xvalor>60):
        # send_alert_attached("Sobrepasa Umbral línea base")
        # print("Sobrepasa Umbral línea base")

# "LINE2:tendencia2#AABB00"