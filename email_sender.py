import os
import smtplib
import time
from getpass import getpass

banner = """
            
            ###########################################
            #                                         #
            #   MMMMM  MMMMMMMMM  MMMMM  MMM  M       #
            #   M      M   M   M  M   M   M   M       #
            #   MMMM   M   M   M  MMMMM   M   M       #
            #   M      M   M   M  M   M   M   M       #
            #   MMMMM  M   M   M  M   M  MMM  MMMMM   #
            #                                         #
            ################# By MBC ##################
"""
hostnames = {
    "gmail": "smtp.gmail.com",
    "yahoo": "smtp.mail.yahoo.com",
    "outlook": "smtp.live.com",
    "aol": "smtp.aol.com",
}
if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")
print(banner)
sender = input("from:    >> ")
pwd = getpass("Password: >> ")
receiver = input("To:    >> ")
msg = input("Message:    >> ")
host = sender.split("@")[1].split(".")[0]
print(host)
if host in hostnames.keys():
    hostname = hostnames.get(host)
    print(hostname)
    with smtplib.SMTP_SSL(host=hostname, port=smtplib.SMTP_PORT) as smtp:
        smtp.login(sender, pwd)
    print("Logging...")
    time.sleep(2)
    print("Logging succeded!")
    try:
        smtp.sendmail(from_addr=sender, to_addrs=receiver, msg=msg)
        print("sending...")
        time.sleep(3)
        print("Your email has been sent successfuly!")
    except:
        print("Something went wrong while sending the email!")
else:
    print("Error! hostname not found.")
