#!/usr/bin/python3

# import alarm
import psutil
import argparse
import os


def main():
    print()
    print("Hello", os.getlogin())
    print()
    print("Here is your system status overview.", os.uname().version)
    print("For a list of commands, run this file with the parameter -h")
    print()
    print()


# Defining monitoring functions
def HDD():
    a = round(psutil.disk_usage("/").free / (1024.0 ** 3), 2)
    return a


def RAM():
    b = round(psutil.virtual_memory().available / (1024.0 ** 3), 2)
    return b


def CPU():
    c = psutil.cpu_percent(0.5)
    return c


parser = argparse.ArgumentParser(description='Monitoring system stats.')

# Adding optional arguments with descriptions
group = parser.add_mutually_exclusive_group()
group.add_argument("-hdd", action="store_true", help="Displays information about storage usage")
group.add_argument("-ram", action="store_true", help='Displays information about ram usage')
group.add_argument("-cpu", action="store_true", help='Displays information about ram usage')
args = parser.parse_args()

# Implementing arguments
if __name__ == "__main__":
    main()
    if args.hdd:
        print("Available storage =", HDD(), "GB")
    elif args.ram:
        print("Available RAM =", RAM(), "GB")
    elif args.cpu:
        print("Current CPU usage =", CPU(), "%")
    else:
        print("Available storage =", HDD(), "GB")
        print("Available RAM =", RAM(), "GB")
        print("Current CPU usage =", CPU(), "%")

import alarm
