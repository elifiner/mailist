# coding=utf8
from mailer import Mailer, Message

subject = u'הסדנה הבאה'
text = open('letter.txt').read().decode('utf8')

# remove RTL directional chars, they interfere with template interpolation
for dirchr in [u'\u202a', u'\u202b', u'\u202c', u'\u200e', u'\u200f']:
    text = text.replace(dirchr, '')
# fix newlines
text = text.replace('\n', '<br>\n')
# add RTL to HTML
text = '<div dir="rtl">%s</div>' % text

message = Message(From='eli@noshem.co.il', To='eli.finer@gmail.com', charset='utf8')
message.Subject = subject.encode('utf8')
message.Html = text.encode('utf8')

m = Mailer(host='smtp.gmail.com', port=587, use_tls=True)
m.login('eli.finer@gmail.com', 'REDACTED')
m.send(message)
