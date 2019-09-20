import psutil
import logging
import os

l = "true"
a = psutil.disk_usage("/")
b = psutil.virtual_memory()
#ajshdgkjasdgk
print("")
print("Festplatte:")
print("Max. Speicher:", round(a.total / (1024.0 ** 3), 2), "GB")
print("Benutzter Speicher:", round(a.used / (1024.0 ** 3), 2), "GB")
print("Freier Speicher:", round(a.free / (1024.0 ** 3), 2), "GB")
print("")
print("Arbeitsspeicher:")
print("Max. Speicher:", round(b.total / (1024.0 ** 3), 2), "GB")
print("Freier Speicher:", round(b.available / (1024.0 ** 3), 2), "GB")
print("Benutzter Speicher:", round(b.used / (1024.0 ** 3), 2), "GB")
print("")
#while True:
#    l = "true"
print("CPU-Auslastung:", psutil.cpu_percent(0.5))
if psutil.cpu_percent(1) > 80:
    print("Hohe Auslastung")

print("")
print(os.system("ps -a"))

logging.basicConfig(filename='app.log',level=logging.INFO)
