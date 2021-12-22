from TrendGraph import grafica1
import _thread
import time
from Notify import send_alert_attached
import os.path

while 1:
    resultado = grafica1()
    if(resultado>60):
        send_alert_attached("Sobrepasa Umbral línea base")
        time.sleep(100)
    time.sleep(2)