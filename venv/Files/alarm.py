import logging
import psutil

logging.basicConfig(filename='app.log', format='%(asctime)s %(message)s')

logging.info("CPU-Auslastung bei", psutil.cpu_percent(0.5))

print(psutil.cpu_percent(1))