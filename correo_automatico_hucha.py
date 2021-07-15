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

# Acumulativo de dinero
d = hoy.isocalendar()[1] # número de la semana actual
y = 27 # número de la semana en la que se comienza a ahorrar en la hucha (depende de la fecha en la que se realice el programa. En mi caso, es 15/07/2021. La semana 27 del año)

importe_actual = 0 # importe en la hucha actualmente. Si se comienza a ahorrar en el momento en el que se escribe el programa, comienza en 0. 

# Bucle para que cada semana sume 5 euros. En este caso se pretende meter en la hucha 5 euros a la semana
while d > 27:
    dif = d - 27
    importe_actual += 5 * dif
    break

valor_actual = str(importe_actual) # Para que el correo lo acepte

remitente = 'remitente@gmail.com' # Remitente del correo 
destinatarios = ['destinatario@gail.com'] # Destinatarios del correo 
asunto = 'Hucha ' + d1 # Asunto del correo
cuerpo = ('¡Buenas!' + '\n' + '\n' + 'Este es el recordatorio de poner tu parte (5 €) en la hucha.' + '\n' + '\n' + 'A día ' + d1 + ' contando con este ingreso, el dinero que has ingresado en total es de ' 
          + valor_actual + ' €.' + '\n' + '\n' + 'Que pases un buen día :)')

# Datos de correo
cuenta = 'remitente@gmail.com' # cuenta de correo desde el cual se va a enviar el email 
password = 'contraseña' # meter contraseña del correo desde el cual se va a enviar el correo

# Se crea el objeto correo con sus atributos
correo = MIMEMultipart()
correo['From'] = remitente
correo['To'] = ", ".join(destinatarios)
correo['Subject'] = asunto

# Se agrega el cuerpo del correo como objeto MIME de tipo texto
correo.attach(MIMEText(cuerpo, 'plain'))

# Se podría agregar adjuntos al correo
files = ['adjuntos'] # cualquier tipo de archivo, por ejemplo csv

for a_file in files:
    attachment = open(a_file, 'rb')
    file_name = os.path.basename(a_file)
    part = MIMEBase('application','octet-stream')
    part.set_payload(attachment.read())
    part.add_header('Content-Disposition','attachment',filename=file_name)
    encoders.encode_base64(part)
    correo.attach(part)

# Se convierte el objeto correo a texto
texto = correo.as_string()

# Se envía el correo
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(cuenta,password)
server.sendmail(remitente, destinatarios, texto)
server.quit()
