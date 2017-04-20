#!/usr/bin/env python2.7
import MySQLdb
import os
import re
import shutil
import sys
import requests
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


#emails = {"Tim Scott" : "tscott@southbendin.gov", "Regina Williams-Preseton" : "rpreston@southbendin.gov","Randy Kelly" : "rkelly@southbendin.gov","Jo M. Broden" : "jbroden@southbendin.gov","David Varner" : "dvarner@southbendin.gov","Oliver Davis" : "odavis@southbendin.gov","John Voorde" : "jvoorde@southbendin.gov","Gavin Ferlic" : "gferlic@southbendin.gov","Karen L. White" : "kwhite@southbendin.gov"}

emails = {"Tim Scott" : "pjuneja@nd.edu", "Regina Williams-Preseton" : "rpreston@southbendin.gov","Randy Kelly" : "rkelly@southbendin.gov","Jo M. Broden" : "jbroden@southbendin.gov","David Varner" : "dvarner@southbendin.gov","Oliver Davis" : "odavis@southbendin.gov","John Voorde" : "jvoorde@southbendin.gov","Gavin Ferlic" : "gferlic@southbendin.gov","Karen L. White" : "kwhite@southbendin.gov"}
districts = {"Tim Scott" : 1, "Regina Williams-Preseton" : 2,"Randy Kelly" : 3,"Jo M. Broden" : 4,"David Varner" : 5,"Oliver Davis" : 6,"John Voorde" : 0,"Gavin Ferlic" : 0,"Karen L. White" : 0}

db = MySQLdb.connect('localhost', 'root', '', 'SBCC')
cursor = db.cursor()
cursor.execute("SELECT FIRSTNAME FROM USERS")
firstname = cursor.fetchone()
cursor.execute("SELECT LASTNAME FROM USERS")
lastname = cursor.fetchone()
db.close()

def sendEmail(name, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("southbendconnect", "cse20312Project")
    msg = MIMEMultipart()
    msg['From'] = "southbendconnect@gmail.com"
    msg['To'] = emails[name]
    msg['Subject'] = "SouthBendConnect; Name: " + firstname + " " + lastname
    msg.attach(MIMEText(message, 'plain'))
    text = msg.as_string()
    errors = server.sendmail("southbendconnect@gmail.com", emails[name], text)
    server.quit()
    
    
sendEmail("Tim Scott",  "Script body test. Is this working? \n How about now?")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
