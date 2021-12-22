#!/usr/bin/env python
from path import *
import rrdtool

fname=rrdpath+rrdname
ret = rrdtool.create(rrdpath+rrdname,
                     "--start",'N',
                     "--step",'60',
                     "DS:inoctets:COUNTER:600:U:U",
                     "RRA:AVERAGE:0.5:1:300",
            #RRA:HWPREDICT:rows:alpha:beta:seasonal period[:rra - num]
                     "RRA:HWPREDICT:100:0.1:0.0035:20:3",
              #RRA:SEASONAL:seasonal period:gamma:rra-num
                     "RRA:SEASONAL:20:0.1:2",
              #RRA:DEVSEASONAL:seasonal period:gamma:rra-num
                     "RRA:DEVSEASONAL:20:0.1:2",
                #RRA:DEVPREDICT:rows:rra-num
                     "RRA:DEVPREDICT:100:4",
            #RRA:FAILURES:rows:threshold:window length:rra-num
                     "RRA:FAILURES:100:7:9:4")
rrdtool.dump(fname,'pred.xml')


#HWPREDICT rra-num is the index of the SEASONAL RRA.
#SEASONAL rra-num is the index of the HWPREDICT RRA.
#DEVPREDICT rra-num is the index of the DEVSEASONAL RRA.
#DEVSEASONAL rra-num is the index of the HWPREDICT RRA.
#FAILURES rra-num is the index of the DEVSEASONAL RRA.

if ret:
    print (rrdtool.error())

