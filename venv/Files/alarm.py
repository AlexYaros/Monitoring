import logging
import configparser
import argparse
import MonitoringV

import configparser

config = configparser.ConfigParser()
config.read("config.ini")
RAMsoftlimit = float(config.get("LIMIT", "RAMsoftlimit"))
RAMhardlimit = float(config.get("LIMIT", "RAMhardlimit"))
HDDsoftlimit = float(config.get("LIMIT", "HDDsoftlimit"))
HDDhardlimit = float(config.get("LIMIT", "HDDhardlimit"))
CPUsoftlimit = float(config.get("LIMIT", "CPUsoftlimit"))
CPUhardlimit = float(config.get("LIMIT", "CPUhardlimit"))


# for key in config["SMTP"]:  # Auf alle Elemente einer Section zugreifen
#   print(key, config["SMTP"][key])

# print(config["LIMIT"]["HDDsoftlimit"])  # auf ein Element zugreifen


logging.basicConfig(filename='app.log', format='%(asctime)s %(message)s')

if MonitoringV.CPU() > CPUsoftlimit:
    print("High cpu usage")
    logging.warning("High cpu usage")

elif MonitoringV.CPU() > CPUhardlimit:
    print("Warning! Very high cpu usage")
    logging.warning("Warning! Very high cpu usage")

if MonitoringV.RAM() < RAMsoftlimit:
    print("Low available RAM")
    logging.warning("Low available RAM")

elif MonitoringV.RAM() < RAMhardlimit:
    print("Warning! Very low available RAM")
    logging.warning("Warning! Very low available RAM")

if MonitoringV.HDD() < HDDsoftlimit:
    print("Low storage capacity")
    logging.warning("Low storage capacity")

elif MonitoringV.HDD() < HDDhardlimit:
    print("Warning! Very low storage capacity")
    logging.warning("Warning! Very low storage capacity")
