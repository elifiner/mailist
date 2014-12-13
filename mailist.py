#!/usr/bin/python
# coding=utf8
import re
import sys

import config
from gmailer import Gmailer

MAIL_HEADERS = {
    u'עבור' : 'to',
    u'נושא' : 'subject',
}

def bidi(s):
    # convert a multiline string for bidi debug printing
    from bidi.algorithm import get_display
    s = get_display(s)
    lines = s.splitlines()
    maxlen = max(len(l) for l in lines)
    lines = [('%' + str(maxlen) + 's') % l for l in lines]
    return '\n'.join(lines)

def text2html(text):
    text = text.replace('\n', '<br>\n')
    text = '<div dir="rtl">%s</div>' % text
    return text

def parse_addresses(filename):
    with open(filename) as f:
        headers = f.readline().strip().split(',')
        for line in f:
            values = line.decode('utf8').strip().split(',')
            rec = dict(zip(headers, values))
            yield {
                u'שם' : rec['name'],
                u'מייל' : rec['email'],
                u'ז' : rec['gender'] == 'male',
                u'נ' : rec['gender'] == 'female',
            }

def parse_merged_messages(filename):
    with open(filename) as f:
        all_messages = f.read().decode('utf8')
        messages = re.split('\s*~~~\s*', all_messages)
        for msg in messages:
            if not msg:
                continue
            rec = {}
            lines = msg.splitlines()
            for i, line in enumerate(lines):
                if ':' in line:
                    header, value = map(unicode.strip, line.split(':'))
                    rec[MAIL_HEADERS[header]] = value
                else:
                    break
            text = '\n'.join(lines[i+1:]).strip()
            rec['text'] = text
            yield rec


class Template(object):
    def __init__(self, filename):
        self.templ = open(filename).read().decode('utf8')

    def apply(self, attrs):
        def _repl(match):
            name = match.group(1)
            if u':' in name:
                name, text = name.split(u':')
                return text if attrs[name] else u''
            else:
                return attrs[name]

        return re.sub(ur'%(.+?)%', _repl, self.templ)

def main():
    import argparse
    parser = argparse.ArgumentParser(description='send multiple emails through gmail')
    parser.add_argument('-m', '--merge', nargs=2, metavar=('address_csv', 'template'), help='generate emails')
    parser.add_argument('-s', '--send', nargs=1, metavar='merged', help='send emails')
    args = parser.parse_args()

    if not args.merge and not args.send:
        parser.error('either --merge or --send should be specified')

    # generate mail merge file
    if args.merge:
        csv_file, template_file = args.merge
        templ = Template(template_file)

        for rec in parse_addresses(csv_file):
            msg = templ.apply(rec)
            if sys.stdout.isatty():
                print bidi(msg).encode('utf-8')
            else:
                print msg.encode('utf-8')
            print '~~~'

    # send emails in mail merge file
    elif args.send:
        gm = Gmailer(config.GMAIL_LOGIN, config.GMAIL_PASSWORD)
        for msg in parse_merged_messages(args.send[0]):
            print >>sys.stderr, msg['to'] + '...',
            gm.send(config.FROM_ADDRESS, msg['to'], msg['subject'], text2html(msg['text']))
            print >>sys.stderr, 'ok'

if __name__ == '__main__':
    main()
