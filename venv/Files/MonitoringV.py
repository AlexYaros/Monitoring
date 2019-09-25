import psutil
import argparse

parser = argparse.ArgumentParser(description='Monitoring system stats.')

# Adding arguments with descriptions
parser.add_argument("all", default="all", help="Display all informations")
parser.add_argument("ram", type=str, help='Displays information about ram usage')
parser.add_argument("hdd", type=str, help="Displays information about storage usage")
parser.add_argument("cpu", type=str, help="Displays information about cpu usage",)
args = parser.parse_args()
print(args)


def HDD():
    a = round(psutil.disk_usage("/").free / (1024.0 ** 3), 2)
    print(a, "GB")
    return a


def RAM():
    b = round(psutil.virtual_memory().available / (1024.0 ** 3), 2)
    print(b, "GB")
    return b


def CPU():
    c = psutil.cpu_percent(1)
    print(c, "%")
    return c


if args.hdd:
    HDD()

if args.ram:
    RAM()

if args.cpu:
    CPU()

if args.all:
    HDD()
    RAM()
    CPU()
