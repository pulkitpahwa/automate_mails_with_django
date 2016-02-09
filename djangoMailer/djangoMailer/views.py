from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.http import HttpResponse
from email.MIMEImage import MIMEImage

import os
import csv

def home(request) :
    with open("my_csv.csv","r") as f : 
        data = csv.reader(f)
#       rows[0] is name, rows[1] is email, rows[4] contains image to be sent 
        for rows in data : 
            text_message = "Hi {},"
            text_message = text_message.format(str(rows[0]).capitalize())
            print text_message
            email = EmailMultiAlternatives("Congratulations", text_message , to = [rows[1] ])
#           Comment out the following lines if you need to send some attachment. I send images corresponding to each user
#            fp = open(os.path.join(os.path.dirname(__file__), rows[4]), 'rb')
#            msg_img = MIMEImage(fp.read())
#            fp.close()
#            msg_img.add_header('Content-ID', '<{}>'.format(rows[4]))
#            email.attach(msg_img)
            email.send()


    return HttpResponse("emails sent successfully")
