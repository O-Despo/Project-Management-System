import argparse
import os
import json

class ProjectManagementSystem():
    def __init__(self):
        """Creates needed variables"""
        # Need const values
        self.CONFIG_PATH = './project-management-system.conf'

        self.COMMAND_CHOICES = {
                'setup': self.setup,
                'mk': self.mk,
                'add': self.add,
                'rm': self.rm
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
        self.parsed_args = parsed_args
        if os.path.isfile(self.CONFIG_PATH):
            self.config_file_r = open(self.CONFIG_PATH, 'r')
            self.config_json = json.load(self.config_file_r)
            self.projects_json = self.config_json['projects']
            self.config_file_r.close()
            
            func = self.COMMAND_CHOICES[parsed_args.command]
            self.msg = func()
            
            self.config_file_w = open(self.CONFIG_PATH, 'w')
            self.config_json = json.dump(self.config_json, self.config_file_w)
            self.config_file_w.close()

        elif self.parsed_args.command == 'setup':
            self.msg = self.setup()

        else:
            self.msg = "run setup first"
        
        return self.msg

    def setup(self):
        """Closes config file"""
        if os.path.isfile(self.CONFIG_PATH):
            self.msg = "already set"
        else:
            #Use the 2nd arg as machine name
            self.DEFAULT_CONFIG['machine_name'] = self.parsed_args.command_input[0]
            
            #Save config_file
            self.config_file_w = open(self.CONFIG_PATH, 'w')
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
        """Adds the project to the config"""
        project_name = self.parsed_args.command_input[0]
        origin = self.parsed_args.origin
        
        project_dir = {
                'project_name': project_name,
                'origin': origin,
                'status': 'new'
                }
        
        self.projects_json.update(project_dir)

        return f"made project {project_name} with origin {origin}"

    def rm(self):
        """Closes config file"""
        project_name = self.parsed_args.command_input[0]

        self.project_json.pop(project_name)

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
parser = argparse.ArgumentParser(
        description="project-management-system: A command-line tool for keeping track of projects across machines",
        epilog="Made by O-Despo"
        )

parser.add_argument("command", nargs='?', const='help', help="commands to execute", choices=COMMAND_CHOICES)
parser.add_argument("command_input", nargs='*', help="the argument to be passed to the command input")
parser.add_argument("-f", "-force", action='store_const', const=True, default=False)
parser.add_argument("-origin", action='store_const', const="local", default="local")

if __name__ == '__main__':
    parse = parser.parse_args()
    pms_instance = ProjectManagementSystem()
    msg = pms_instance(parse)
    print(msg)
