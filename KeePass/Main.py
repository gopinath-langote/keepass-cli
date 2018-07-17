from pykeepass import PyKeePass
import argparse
import KeePass

W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", action="store", dest="file", required=True, help="Keepass file location")
    parser.add_argument("-p", "--password", action="store", dest="password", required=True,
                        help="Keepass file password")
    parser.add_argument("-s", "--search", action="store", dest="search", required=True, help="Search Key")
    args = parser.parse_args()

    kp = PyKeePass(args.file, password=args.password)

    searchTerm = args.search.split(" ")

    KeePass.search(kp, searchTerm)


if __name__ == '__main__': main()
