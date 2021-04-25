import schedule
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from robot_setup_work import robot_set_up_work

try:
    print('Started')

    schedule.every().day.at('17:00').do(robot_set_up_work)

    while True:# loop infinito
        schedule.run_pending()
        time.sleep(1)

# Para fazer string constructor utilize o f antes da string
except IndexError as e:
    email_body = f'''
        O bot apresento problemas, favor verificar:
        Erro: {e}
    '''

    from_email = 'miller00315@gmail.com'
    password = 'Oitavo#123'
    to_email = 'miller00315@gmail.com'

    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = 'Bot falhou'

    # Corpo do E-mail com anexos
    message.attach(MIMEText(email_body, 'plain'))

    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # Usuário do Gmail com porta
    session.starttls()  # Habilita a segurança
    session.login(from_email, password)  # Login e senha de quem envia o e-mail
    text = message.as_string()
    session.sendmail(from_email, to_email, text)
    session.quit()

