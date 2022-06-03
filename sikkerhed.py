from picamera import PiCamera
import smtplib
import time
from time import sleep
from datetime import datetime, timedelta
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import RPi.GPIO as GPIO
import schedule


def motion(P, me, toaddr):

    start = time.time()
    PERIODE_OF_TIME = 60

    print("Nu begynder PIR motion sensor at opfange bevægelse")
    
    while True:

        if GPIO.input(23):
            
            print("Bevægelse!...")
            P.capture('movement.jpg')
            subject='Sikkerhedsalarm!'
            msg = MIMEMultipart()
            msg['Subject'] = subject
            msg['From'] = me
            msg['To'] = toaddr

            fp= open('movement.jpg','rb')
            img = MIMEImage(fp.read())
            fp.close()
            msg.attach(img)

            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(user = 'hovsatest',password='ztpfuostyyncsktw')
            server.send_message(msg)
            server.quit()
            if time.time () > start + PERIODE_OF_TIME : break
        

def email():
    toaddr = 'sikkerhed1000@gmail.com'
    me = 'hovsatest@gmail.com'

    GPIO.setmode(GPIO.BCM)

    P=PiCamera()
    P.resolution= (1024,768)
    P.start_preview()
    GPIO.setup(23, GPIO.IN)
    
    schedule.every().day.at("10:34").do(motion, P, me, toaddr)

    while True:
        schedule.run_pending()
email()