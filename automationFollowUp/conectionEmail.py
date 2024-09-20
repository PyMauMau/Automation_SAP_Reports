import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SendEmail:
    def __init__(self, email, password):
        self._server = "smtp-mail.outlook.com"
        self._smtp_port = 587
        self.email = email
        self.password = password

    def setCredentials(self, email, password):
        self.email = email
        self.password = password

    @property
    def getCredentials(self):
        return self.email, self.password

    def sendEmail(self, to_email, subject, body):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP(self._server, self._smtp_port)
            server.starttls()
            server.login(self.email, self.password)
            server.sendmail(self.email, to_email, msg.as_string())
            server.quit()
            print('Email enviado com sucesso!')
        except Exception as e:
            print(f'Erro ao enviar email: {e}')