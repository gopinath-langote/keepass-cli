from tabulate import tabulate
from itertools import permutations
import re

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

# credits
# https://bitbucket.org/astanin/python-tabulate
# https://github.com/pschmitt/pykeepassx
# argparser
