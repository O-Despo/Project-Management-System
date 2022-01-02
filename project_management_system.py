import argparse
import os
import json

class ProjectManagementSystem():
    def __init__(self):
        """Creates needed variables"""
        # Need const values
        self.CONFIG_PATH = '~/project-management-system.conf'

        # self.COMMAND_CHOICES = {
                # 'setup',
                # 'get',
                # 'set',
                # 'mk',
                # 'add',
                # 'rm',
                # 'sync-config',
                # 'sync-project'
                # }
        # pass

    def __exit__(self):
        """Closes config file"""
        pass
    
    def __call__(self, command):
        """Runs the given command and the rutoines around it"""
        pass

    def setup(self):
        """Closes config file"""
        pass

    def get(self):
        """Closes config file"""
        pass

    def mk(self):
        """Closes config file"""
        pass

    def add(self):
        """Closes config file"""
        pass

    def rm(self):
        """Closes config file"""
        pass

    def sync_project(self):
        """Closes config file"""
        pass

    def sync_config(self):
        """Closes config file"""
        pass





# initiate parser
parser = argparse.ArgumentParser(
        description="project-management-system: A command-line tool for keeping track of projects across machines",
        epilog="Made by O-Despo"
        )

parser.add_argument("command", nargs='?', const='help', help="commands to execute", choices=COMMAND_CHOICES)

parser.add_argument("-f", "-force", action='store_const', const=True, default=False)

if __name__ == '__main__':

# Open db files
if os.path.isfile(CONFIG_PATH):
    config_file_r = open(CONFIG_PATH, 'r')
    config_json_r = open(CONFIG_PATH, 'r')
