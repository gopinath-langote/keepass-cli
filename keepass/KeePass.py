from tabulate import tabulate
from itertools import permutations
import re
from pykeepass import PyKeePass
import argparse

W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple


def search(kp, keywords):
    table = records(kp, keywords)

    print(tabulate(table, headers=["Title", "UserName", format(R, "password")], tablefmt="fancy_grid"))


def records(kp, keywords):
    tata = entries(kp, keywords)
    table = []
    keys = set()
    for entry in tata:
        row = [entry.title, entry.username, format(G, entry.password)]
        if entry.title not in keys:
            keys.add(entry.title)
            table.append(row)
    return table


def entries(kp, keywords):
    entries = []
    str = "(?i)" + patterns(keywords)
    records = kp.find_entries(title=str, regex=True, first=False)
    for entry in records:
        if not re.search('Recycle Bin', "" + repr(entry), re.IGNORECASE):
            entries.append(entry)
    return entries


def patterns(keywords):
    patterns = []
    perm = permutations(keywords)
    for i in list(perm):
        patterns.append(regex(i))
    return '|'.join(patterns)


def regex(keywords):
    str = "(.*"
    for x in keywords:
        str += x + ".*"
    str = str.strip()
    str += ")"
    return str


def format(color, str):
    if str is not None:
        return color + str + W


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", action="store", dest="file", required=True, help="Keepass file location")
    parser.add_argument("-p", "--password", action="store", dest="password", required=True,
                        help="Keepass file password")
    parser.add_argument("-s", "--search", action="store", dest="search", required=True, help="Search Key")
    args = parser.parse_args()

    kp = PyKeePass(args.file, password=args.password)

    searchTerm = args.search.split(" ")

    search(kp, searchTerm)


if __name__ == '__main__': main()

# credits
# https://bitbucket.org/astanin/python-tabulate
# https://github.com/pschmitt/pykeepassx
# argparser
