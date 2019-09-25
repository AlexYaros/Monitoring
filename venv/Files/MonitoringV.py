#!/usr/bin/python3

import psutil
import argparse


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


parser = argparse.ArgumentParser(description='Monitoring system stats.')

# Adding arguments with descriptions
parser.add_argument("all", nargs="?", type=str, help="Display all information")
parser.add_argument("ram", nargs="?", type=str, help='Displays information about ram usage')
parser.add_argument("hdd", nargs="?", type=str, help="Displays information about storage usage")
parser.add_argument("cpu", nargs="?", type=str, help="Displays information about cpu usage", )
args = parser.parse_args()


if args.all:
    HDD()
    RAM()
    CPU()


if args.hdd:
    HDD()


elif args.ram:
    RAM()


elif args.cpu:
    CPU()
