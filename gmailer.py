# coding=utf8

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr

class Gmailer(object):
    def __init__(self, username, password):
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo()
        self.server.login(username, password)

    def send(self, from_address, to_address, subject, html):
        msg = MIMEText(html, 'html', 'utf8')
        msg['Subject'] = str(Header(subject, 'utf8'))
        msg['From'] = self._addr(from_address, 'utf8')
        msg['To'] = self._addr(to_address, 'utf8')
        self.server.sendmail(self._email(from_address), self._email(to_address), msg.as_string())

    def quit(self):
        self.server.quit()

    def _addr(self, addr, encoding):
        name, email = parseaddr(addr)
        name = str(Header(name, encoding))
        email = str(email)
        return formataddr((name, email))

    def _email(self, addr):
        return parseaddr(addr)[1]
