import psutil
import logging
import os

logging.basicConfig(filename='app.log',level=logging.INFO)

l = "true"
a = psutil.disk_usage("/")
b = psutil.virtual_memory()

print("")

def Festplatte():
    print("Festplatte:")
    print("Max. Speicher:", round(a.total / (1024.0 ** 3), 2), "GB")
    print("Benutzter Speicher:", round(a.used / (1024.0 ** 3), 2), "GB")
    print("Freier Speicher:", round(a.free / (1024.0 ** 3), 2), "GB")

print("")

def Arbeitsspeicher():
    print("Arbeitsspeicher:")
    print("Max. Speicher:", round(b.total / (1024.0 ** 3), 2), "GB")
    print("Freier Speicher:", round(b.available / (1024.0 ** 3), 2), "GB")
    print("Benutzter Speicher:", round(b.used / (1024.0 ** 3), 2), "GB")

print("")
#while True:
#    l = "true"

def CPU():
    print("CPU-Auslastung:", psutil.cpu_percent(0.5))
    if psutil.cpu_percent(0.5) < 80:
        logging.basicConfig(format='%(asctime)s %(message)s')
        logging.warning("Hohe Auslastung")
        print("Hohe Auslastung")

print("")
print(os.system("ps -a"))

Festplatte()
Arbeitsspeicher()
CPU()


