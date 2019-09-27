import logging
import MonitoringV
import configparser
import os

config = configparser.ConfigParser()
config.read("config.ini")
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

elif HDDsoftlimit > HDD < HDDhardlimit:
    print("Warning! Very low available storage capacity at", HDD, "GB")
    logging.warning("Warning! Very low available storage capacity at %s GB", HDD)
