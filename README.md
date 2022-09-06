# ipChange
Simple python utility that informs me by email if my public ip changes

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
