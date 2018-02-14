import imaplib
import email
import time
import sys
import getpass
#from time import gmtime, strftime
#import pyttsx
from espeak import espeak
import re
import RPi.GPIO as GPIO

from subprocess import call
import os

from grovepi import *
from grove_rgb_lcd import *


LOG = True

MAIL_CHECK_FREQ = 20

print "\n\n\n############# MAIL CHECKER SYSTEM ###########"
print "#\n#"

USERNAME = raw_input('# Enter Username: ')

PASSWORD = getpass.getpass()

server = imaplib.IMAP4_SSL('imap.gmail.com')
server.login(USERNAME,PASSWORD);

print '# Logged In...'

#print '# starting audio engine'
#engine = pyttsx.init()
#print '# engine started'

#engine.setProperty( 'rate' , '60' )

inp = input('# Enter 0: espeak OR 1: Google Text-to-Speech : ');

while True:
    server.select('inbox')

    result, data = server.search(None,'UNSEEN')

    ids = data[0].split(' ')

    for idn in ids:
        print '# msg : '+idn
        typ, data = server.fetch( idn , '(RFC822)' )
        msgFrom = email.message_from_string(data[0][1])

        typ, data = server.store( idn, '+FLAGS', '\\Seen')
        fr = msgFrom['From']
        fr = fr.split('<')[1];
        fr = fr.split('>')[0];
        sub = msgFrom['Subject']

        print 'From : '+ fr
        print 'Subject :'+ sub
        txt = 'New Email from '+ fr +'. '+ sub

        # print output to lcd
        setRGB(0,128,68)
        #setText( txt )

        # speak txt
        if( inp ):
            os.system('./google.sh \"'+txt+'\"')
            #call([ './google.sh' ,txt ])
        else:
            espeak.synth( txt )

        ar = re.findall('.{1,32}',txt);

        for a in ar:
            if( len(a)>16 ):
                i,j = a[:16], a[16:]
                setText(i+'\n'+j)
            else:
                setText(a)
            time.sleep(2)

        #while espeak.is_playing:
        #    time.sleep(2);

        #engine.say( txt )

        #engine.runAndWait()

        #print msgFrom['Body']

        time.sleep( MAIL_CHECK_FREQ )

        setText('')

    time.sleep( 5 )
