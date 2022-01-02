import argparse
import json

parser = argparse.ArgumentParser(
        description="project-management-system: A command-line tool for keeping track of projects across machines",
        epilog="Made by O-Despo"
        )

parser.add_argument("setup", help="Setup the local database and settings")
parser.add_argument("set")
parser.add_argument("get")
parser.add_argument("mk")
parser.add_argument("add")
parser.add_argument("rm")
parser.add_argument("sync-db")
parser.add_argument("sync")
parser.add_argument("test")

parser.add_argument("-f", "-force", action='store_const', const=True, default=False)
parser.add_argument("-a", action='store_const', const=True, default=False)

parsed = parser.parse_args()
print(parsed)
