from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib


class Email:
    def __init__(self, destinatario: str, remetente: str, senha: str) -> None:
        """Instancia a classe com as configurações iniciais para enviar email
        Args:
            destinatario (str): email do destinatario
            remetente (str): email do remetente
            senha (str): senha do email do remetente
        """
        self.fromaddr = remetente
        self.toaddr = destinatario
        self.password = senha

    def enviar_email(self):
        """Função responsável por enviar o email.
        Ela pega o arquivo criado do excel e anexa no email, 
        e envia o email.
        """
        msg = MIMEMultipart()
        msg['From'] = self.fromaddr
        msg['To'] = self.toaddr

        # Assunto do email
        msg['Subject'] = "E-mail de test"
        # Corpo do emial
        body = "Email enviado do nosso robô"

        msg.attach(MIMEText(body, 'plain'))

        # Arquivo a ser anexado
        filename = "vagas.xlsx"
        anexo = open("vagas.xlsx", "rb")

        p = MIMEBase('aplication', 'octet-stream')
        p.set_payload((anexo).read())
        encoders.encode_base64(p)
        p.add_header("Content-Disposition",
                     "attachment; filename= %s" % filename)
        msg.attach(p)

        s = smtplib.SMTP('smtp.gmail.com', 587)

        # Segurança
        s.starttls()

        s.login(self.fromaddr, self.password)

        # Converte para String
        text = msg.as_string()

        s.sendmail(self.fromaddr, self.toaddr, text)

        s.quit()
