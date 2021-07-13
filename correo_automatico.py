# Importación de librerías
import pandas as pd
import datetime 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from datetime import date

# Correo
hoy = date.today()
d1 = hoy.strftime("%d-%m-%Y")
remitente = 'correo_remitente@gmail.com'
destinatarios = ['correo_destino@gmail.com']
asunto = 'Hucha ' + d1
cuerpo = '¡Buenas!' + '\n' + 'Este es un correo de prueba'

# Datos de correo
cuenta = 'correo@gmail.com'
password = 'contraseña' # meter contraseña del correo

# Se crea el objeto correo con sus atributos
correo = MIMEMultipart()
correo['From'] = remitente
correo['To'] = ", ".join(destinatarios)
correo['Subject'] = asunto

# Se agrega el cuerpo del correo como objeto MIME de tipo texto
correo.attach(MIMEText(cuerpo, 'plain'))

# Se podría agregar un adjunto al correo
#files = [df_final]

#for a_file in files:
#    attachment = open(a_file, 'rb')
#    file_name = os.path.basename(a_file)
#    part = MIMEBase('application','octet-stream')
#    part.set_payload(attachment.read())
#    part.add_header('Content-Disposition','attachment',filename=file_name)
#    encoders.encode_base64(part)
#    mensaje.attach(part)

# Se convierte el objeto correo a texto
texto = correo.as_string()

# Se envía el correo
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(cuenta, password)
server.sendmail(remitente, destinatarios, texto)
server.quit()