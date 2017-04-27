#!/usr/bin/env python2.7
#import MySQLdb
import os
import re
import shutil
import sys
import smtplib
import string
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import mysql.connector
from mysql.connector import errorcode


#emails = {"Tim Scott" : "tscott@southbendin.gov", "Regina Williams-Preseton" : "rpreston@southbendin.gov","Randy Kelly" : "rkelly@southbendin.gov","Jo M. Broden" : "jbroden@southbendin.gov","David Varner" : "dvarner@southbendin.gov","Oliver Davis" : "odavis@southbendin.gov","John Voorde" : "jvoorde@southbendin.gov","Gavin Ferlic" : "gferlic@southbendin.gov","Karen L. White" : "kwhite@southbendin.gov"}

emails = {"Tim Scott" : "bbadura@nd.edu", "Regina Williams-Preseton" : "bbadura@nd.edu", "Randy Kelly" : "bbadura@nd.edu", "Jo M. Broden" : "bbadura@nd.edu", "David Varner" : "bbadura@nd.edu", "Oliver Davis" : "bbadura@nd.edu"}
districts = {1 : "Tim Scott", 2 : "Regina Williams-Preseton", 3 : "Randy Kelly", 4 : "Jo M. Broden", 5 : "David Varner", 6 : "Oliver Davis"}

try:
    cnn = mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        database='SBCC')
    print ("it works")
except mysql.connector.Error as e:
    if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with username or Password")
    elif e.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(e)

cursor = cnn.cursor()

if len(sys.argv) > 1:
    useremail = str(sys.argv[1])

rowReq = """
    SELECT * FROM users 
    WHERE EMAIL = '{}'""".format(useremail)

cursor.execute(rowReq)
row = cursor.fetchone()
messagestr = str(row[6])
fnamestr = str(row[1])
lnamestr = str(row[2])
district = int(row[4])
ccmemb = districts[district]

cnn.commit()
cursor.close()
cnn.close()

def sendEmail(name, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("southbendconnect", "cse20312Project")
    msg = MIMEMultipart()
    msg['From'] = "southbendconnect@gmail.com"
    msg['To'] = emails[name]
    msg['Subject'] = "SouthBendConnect; Name: " + fnamestr + " " + lnamestr
    msg.attach(MIMEText(message, 'plain'))
    text = msg.as_string()
    errors = server.sendmail("southbendconnect@gmail.com", emails[name], text)
    server.quit()
    
    
sendEmail(ccmemb,  messagestr)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
