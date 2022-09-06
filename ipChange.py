#!/usr/bin/python3

#This is a simple utility that I needed in my day to day, which informs me by mail if my public ip changes
#By automating the script it alerts you by email when the public IP changes
#For example with crontab I would check every 5 minutes
#*/5 * * * * /ROUTE_TO/ipChange.py
#The script consists of two python files and a text file to store the previous ip:
#ipChange.py (PRINCIPAL SCRIPT)
#config.py (CONFIGURATION FILE FOR EMAIL)
#ipOld.txt (OLD IP)
#I have my own external web server and use my own script to report my ip instead of using akamai.com
#using the php command: $_SERVER['HTTP_CLIENT_IP']

import requests
import smtplib, ssl
import config

#Retrieve the previous IP from the local file
ipOld = open('ipOld.txt', 'r')
ipOld = (ipOld.read())
ipOld = ipOld.replace("\n","")

#Find the current ip
response = requests.get("http://whatismyip.akamai.com/")
ipActive = str(response.content)
ipActive = str(ipActive).replace("b'","")
ipActive = str(ipActive).replace("'","")

#Compare the active ip with the previous one
if (ipActive != ipOld):
        #If it has changed, I update the ipActive in the local file
        newIp=open("ipOld.txt", "w")
        newIp.write(ipActive)
        newIp.close()
        #Mail
        port = 465
        smtp_server = config.smtp_server
        sender_email = config.username
        receiver_email = config.receiver_email
        password=config.password
        from_address = config.from_address
        message = """From: """ + from_address + """
        To: """ + receiver_email + """
Subject: The IP has changed
Previous IP: """ + ipOld + """\nNew IP: """ + ipActive
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
