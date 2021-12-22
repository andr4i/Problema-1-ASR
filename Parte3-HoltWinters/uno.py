# dataframe opertations - pandas
from rrdPredGraph import grafica2
import time
import _thread
import _thread
import os.path


from Notify import send_alert_attached
import os.path
contador = 0
while 1:
    resultado = grafica2()
    if((resultado==1)and(contador==0)):
        send_alert_attached("Sobrepasa Umbral línea base")
        print("Correo Enviado")
        contador = 1000
    else:
        if(contador > 0):
            contador = contador - 2
        time.sleep(2)