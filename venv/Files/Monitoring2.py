import psutil
import logging
import os

logging.basicConfig(filename='app.log', format='%(asctime)s %(message)s')

a = psutil.disk_usage("/")
b = psutil.virtual_memory()

print("")

#Auslesung der Werte der Festplatte: total, benutzt und frei.
#Alarm, wenn freier Speicherplatz weniger als 20GB beträgt

def Festplatte():
    print("Festplatte:")
    print("Max. Speicher:", round(a.total / (1024.0 ** 3), 2), "GB")
    print("Benutzter Speicher:", round(a.used / (1024.0 ** 3), 2), "GB")
    print("Freier Speicher:", round(a.free / (1024.0 ** 3), 2), "GB")
    if a.free < 21474836480:
        logging.warning("Wenig freier Festplattenplatz")
        print("Wenig freier Festplattenplatz")
    print("")

#Auslesung der Werte des Arbeitsspeichers: total, frei und verwendet.
#Alarm, wenn freier Arbeitsspeicher weniger als 1GB beträgt

def Arbeitsspeicher():
    print("Arbeitsspeicher:")
    print("Max. Speicher:", round(b.total / (1024.0 ** 3), 2), "GB")
    print("Freier Speicher:", round(b.available / (1024.0 ** 3), 2), "GB")
    print("Benutzter Speicher:", round(b.used / (1024.0 ** 3), 2), "GB")
    if b.available < 1073741824:
        logging.warning("Wenig freier Arbeitsspeicher")
        print("Wenig freier Arbeitsspeicher")
    print("")


#Auslesung der CPU-Auslastung
# Alarm, wenn Grenzwert von 80% Auslastung überschritten wird

def CPU():
    #print("CPU-Auslastung:", psutil.cpu_percent(0.5))
    logging.info("CPU-Auslastung bei", psutil.cpu_percent(0.5))
    if psutil.cpu_percent(0.5) > 80:
        logging.warning("Hohe CPU-Auslastung")
        print("Hohe Auslastung")
    print("")

Festplatte()
Arbeitsspeicher()
CPU()

#logging.info("No warnings")

print("")
#print(os.system("ps -a"))

