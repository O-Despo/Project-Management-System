import argparse
import os
import json

CONFIG_PATH = '~/project-management-system.conf'
COMMAND_CHOICES = [
        'setup',
        'get',
        'set',
        'mk',
        'add',
        'rm',
        'sync-config',
        'sync-project'
        ]

# initiate parser
parser = argparse.ArgumentParser(
        description="project-management-system: A command-line tool for keeping track of projects across machines",
        epilog="Made by O-Despo"
        )

parser.add_argument("command", nargs='?', const='help', help="commands to execute", choices=COMMAND_CHOICES)
parser.add_argument("-f", "-force", action='store_const', const=True, default=False)
    
