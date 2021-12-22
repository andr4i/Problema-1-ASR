import smtplib
import imghdr
from email.message import EmailMessage
from fpdf import FPDF

class PDF(FPDF):
    pass

    def logo(self, name, x, y, w, h):
        self.image(name, x, y, w, h)

    def titles(self, title):
        self.set_xy(10.0, 0.0)
        self.set_font('Arial', 'B', 24)
        self.set_text_color(58, 127, 246)
        self.cell(w=210.0, h=40.0, align='L', txt=title, border=0)

    def titles2(self):
        self.set_xy(10.0, 0.0)
        self.set_font('Arial', 'B', 36)
        self.set_text_color(58, 127, 246)
        self.cell(w=210.0, h=40.0, align='L', txt="Resúmen de comparación:", border=0)

    def titles3(self):
        self.set_xy(25.0, 45.0)
        self.set_font('Arial', 'B', 14)
        self.set_text_color(58, 127, 246)
        self.cell(w=210.0, h=40.0, align='L', txt="Cambios Relevantes:", border=0)

    def porcentaje(self, porcent):
        self.set_xy(0.0, 30.0)
        self.set_font('Arial', 'B', 96)
        self.set_text_color(58, 127, 246)
        self.cell(w=210.0, h=40.0, align='C', txt=f"{int(porcent)}%", border=0)

    def texts(self, txto):
        self.set_xy(10.0, 40.0)
        self.set_font('Arial', 'B', 14)
        self.set_text_color(58, 127, 246)
        # self.cell(w=210.0, h=40.0, align='C', txt=txto, border = 0)
        self.multi_cell(0, 5, txto)
        self.cell(0, 5)

    def desEnfermedad(self, enf):
        self.set_xy(10.0, 95.0)
        with open(enf, 'rb') as xy:
            txt = xy.read().decode("utf-8")
        self.set_font('Arial', 'B', 14)
        self.set_text_color(58, 127, 246)
        self.multi_cell(0, 5, txt)
        # self.cell(w=210.0, h=40.0, align='C', txt=txt, border = 0)
        self.cell(0, 5)

    def texts1(self, txto):
        self.set_xy(10.0, 125.0)
        self.set_font('Arial', 'B', 14)
        self.set_text_color(58, 127, 246)
        self.cell(w=210.0, h=40.0, align='L', txt=txto, border=0)

    def grafica1(self, image):
        self.image(image, x = 10, y = 55, w = 0, h = 0, type= '', link = '')

def reporte():
    pdf = PDF()
    pdf.add_page()
    pdf.titles("Reporte.")
    pdf.set_author('Gonzalo Andrei')
    txto = "Se espera que el valor de uso de CPU estará fuera de lo esperado."
    pdf.texts(txto)
    gr1 = "/home/gonzalo/PycharmProjects/Introduccion_SNMP/4-AdministraciónDeRendimiento/IMG/trend.png"
    pdf.grafica1(gr1)
    pdf.output('ResultadosT.pdf','F')

COMMASPACE = ', '
# Define params
rrdpath = '/home/gonzalo/PycharmProjects/Introduccion_SNMP/4-AdministraciónDeRendimiento/RRD/'
imgpath = '/home/gonzalo/PycharmProjects/Introduccion_SNMP/4-AdministraciónDeRendimiento/IMG/'
fname = 'trend.rrd'

mailsender = "2cuenta.second@gmail.com"
mailreceip = "x19j28@gmail.com"
mailserver = 'smtp.gmail.com: 587'
password = '3stonoes'

def send_alert_attached(subject):
    """ Envía un correo electrónico adjuntando la imagen en IMG
    """
    reporte()
    Sender_Email = "2cuenta.second@gmail.com"
    Reciever_Email = "x19j28@gmail.com"
    Password = "3stonoes"
    newMessage = EmailMessage()
    newMessage['Subject'] = "Notificación valores creciendo"
    newMessage['From'] = Sender_Email
    newMessage['To'] = Reciever_Email
    newMessage.set_content('Mensaje de Prueba')
    files = ['/home/gonzalo/PycharmProjects/Introduccion_SNMP/4-AdministraciónDeRendimiento/Parte2-MínimosCuadrados/ResultadosT.pdf']
    for file in files:
        with open(file, 'rb') as f:
            file_data = f.read()
            file_name = f.name
        newMessage.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(Sender_Email, Password)
        smtp.send_message(newMessage)