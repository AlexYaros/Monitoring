import logging
import MonitoringV
import configparser
import os
import smtplib, ssl

config = configparser.ConfigParser()
config.read("config.ini")

absender = str(config.get("SMTP", "absender"))
password = str(config.get("SMTP", "password"))
empfaenger = str(config.get("SMTP", "empfaenger"))
smtphost = str(config.get("SMTP", "smtphost"))
port = int(config.get("SMTP", "port"))

message = """\
Subject: Hi there

This message is sent from Python."""

def mail():
    # Create a secure SSL context
    context = ssl.create_default_context()

    # Specifying the server address, port, sender and password
    with smtplib.SMTP_SSL(smtphost, port, context=context) as server:
        server.login(absender, password)
        server.sendmail(absender, empfaenger, message)


RAMsoftlimit = float(config.get("LIMIT", "RAMsoftlimit"))
RAMhardlimit = float(config.get("LIMIT", "RAMhardlimit"))
HDDsoftlimit = float(config.get("LIMIT", "HDDsoftlimit"))
HDDhardlimit = float(config.get("LIMIT", "HDDhardlimit"))
CPUsoftlimit = float(config.get("LIMIT", "CPUsoftlimit"))
CPUhardlimit = float(config.get("LIMIT", "CPUhardlimit"))


logging.basicConfig(filename='app.log', format='%(asctime)s - %(levelname)s - %(message)s')

CPU = MonitoringV.CPU()
RAM = MonitoringV.RAM()
HDD = MonitoringV.HDD()

#print(CPU)
#print(RAM)
#print(HDD)

if CPUsoftlimit < CPU < CPUhardlimit:
    print("High cpu usage at", CPU, "%")
    logging.warning("High cpu usage at %s", CPU)

elif CPUsoftlimit < CPU > CPUhardlimit:
    print("Warning! Very high cpu usage at", CPU, "%")
    logging.warning("Warning! Very high cpu usage at %s", CPU)

if RAMsoftlimit > RAM > RAMhardlimit:
    print("Low available RAM at", RAM, "GB")
    logging.warning('Low available RAM at %s GB', RAM)

elif RAMsoftlimit > RAM < RAMhardlimit:
    print("Warning! Very low available RAM at", RAM, "GB")
    logging.warning("Warning! Very low available RAM at %s GB", RAM)

if HDDsoftlimit > HDD > HDDhardlimit:
    print('Low available storage capacity at', HDD, "GB")
    logging.warning("Low available storage capacity at %s GB", HDD)
    message = """\
Subject: Monitoring warning

Low available storage capacity at)."""
    mail()

elif HDDsoftlimit > HDD < HDDhardlimit:
    print("Warning! Very low available storage capacity at", HDD, "GB")
    logging.warning("Warning! Very low available storage capacity at %s GB", HDD)
