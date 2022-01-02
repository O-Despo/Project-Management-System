import argparse
import os
import json

class ProjectManagementSystem():
    def __init__(self):
        """Creates needed variables"""
        # Need const values
        self.CONFIG_PATH = '~/project-management-system.conf'

        self.COMMAND_CHOICES = {
                'setup': self.setup,
                'get': self.get,
                'set': self.set,
                'mk': self.mk,
                'add': self.add,
                'rm': self.rm,
                'sync-config', self.sync_config,
                'sync-project': self.sync_project
                }

        self.DEFAULT_CONFIG = {
                'machine_name': '',
                'projects': {}
                }
        
    def __exit__(self):
        """Closes config file"""
        pass
    
    def __call__(self, parsed_args):
        """Runs the given command and the rutoines around it"""
        if os.path.isfile(self.CONFIG_PATH):
            self.config_file_r = open(self.CONFIG_PATH, 'r')
            self.config_json = json.load(self.config_file_r)
            self.config_file_r.close()
        else:
            self.msg = "run setup first"
            return()
        
        self.parsed_args = parsed_args
        func = self.COMMAND_CHOICES[parsed_args.command]
        func()
        
        self.config_file_w = open(self.CONFIG_PATH, 'w')
        self.config_json = json.load(self.config_file_w)
        self.config_file_w.close()

    def setup(self):
        """Closes config file"""
        if os.path.isfile(self.CONFIG_PATH):
            self.msg = "already set"
        else:
            self.config_file_w = open(self.CONFIG_PATH, 'w')

            #Use the 2nd arg as machine name
            self.DEFAULT_CONFIG['machine_name'] = self.parsed_args.command_input[0]
            
            #Save config_file
            self.config_json = json.dump(self.DEFAULT_CONFIG, self.config_file_w)
            self.config_file_w.close()

            self.msg = f"Success: machine config created with name {self.parsed_args.command_input[0]}"

        return()

    def get(self):
        """Closes config file"""
        pass

    def mk(self):
        #TODO Put on back burner
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
parser.add_argument("command_input", nargs='*', const='', help="the argument to be passed to the command input")
parser.add_argument("-f", "-force", action='store_const', const=True, default=False)

if __name__ == '__main__':

# Open db files
if os.path.isfile(CONFIG_PATH):
    config_file_r = open(CONFIG_PATH, 'r')
    config_json_r = open(CONFIG_PATH, 'r')
