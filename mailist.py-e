# coding=utf8

from mailer import Mailer, Message
from string import Template

def load_template(filename):
    with open(filename) as f:
        text = f.read().decode('utf8')

    # remove RTL directional chars, they interfere with template interpolation
    for dirchr in [u'\u202a', u'\u202b', u'\u202c', u'\u200e', u'\u200f']:
        text = text.replace(dirchr, '')

    # fix newlines
    text = text.replace('\n', '<br>\n')

    # add RTL to HTML
    text = '<div dir="rtl">%s</div>' % text

    return Template(text)

PEOPLE = [
    ('eli.finer@gmail.com', u'אלי', 'm'),
    ('eli.finer@gmail.com', u'אלי2', 'm'),
    # ('yael.finer@gmail.com', u'יעל', 'f'),
]

subject = u'הסדנה הבאה'
from_address = 'Eli Finer<eli@noshem.co.il>'
male_template = load_template('letter-male.txt')
female_template = load_template('letter-female.txt')

mailer = Mailer(host='smtp.gmail.com', port=587, use_tls=True)
mailer.login('eli.finer@gmail.com', 'REDACTED')

for email, name, gender in PEOPLE:
    print email
    if gender == 'm':
        text = male_template.substitute(name=name)
    elif gender == 'f':
        text = female_template.substitute(name=name)
    # print message.encode('utf8')

    message = Message(From='eli@noshem.co.il', To=email, charset='utf8')
    message.Subject = subject.encode('utf8')
    message.Html = text.encode('utf8')

    mailer.send(message)
