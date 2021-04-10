import rpa as r
import pyautogui as p
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

r.init()
r.url('https://www.melhorcambio.com/dolar-hoje')

p.sleep(4)

dollar_value = r.read('//*[@id="comercial"]')

r.close()


#texto do email
texto_email = 'A cotação do dolar hoje ' + str(pd.Timestamp('today')) + ' é ' + dollar_value

# email remetente, senha, destinatário
de = 'emailtest@email.com'
senha = '*********'
para = 'emailtest@email.com'

# Setup the MIME
message = MIMEMultipart()
message['From'] = de
message['To'] = para
message['Subject'] = 'Cotação do dolar'   #Título do e-mail

# Corpo do E-mail com anexos
message.attach(MIMEText(texto_email, 'plain'))

# Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587)  # Usuário do Gmail com porta
session.starttls()  # Habilita a segurança
session.login(de, senha)  # Login e senha de quem envia o e-mail
texto = message.as_string()
session.sendmail(de, para, texto)
session.quit()
