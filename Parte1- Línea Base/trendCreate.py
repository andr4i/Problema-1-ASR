import rrdtool
ret = rrdtool.create("/home/gonzalo/PycharmProjects/Introduccion_SNMP/4-AdministraciónDeRendimiento/RRD/trend.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:CPUload:GAUGE:600:U:U",
                     "RRA:AVERAGE:0.5:1:24")
if ret:
    print (rrdtool.error())
