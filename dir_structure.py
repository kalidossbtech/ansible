# Create the directory structure of ansible
# Name : kalidoss
# Email : kalidossbtech@gmail.com
# Python version : Python 3.7.2

#Run this file : python dir_structure.py 

'''
├── LICENSE
├── README.md                             # Documentation entry point
├── ansible.cfg -> config/ansible.cfg     # Symlink to vagrant config
├── config                              # Configuration directory
│   ├── ansible.cfg                       # Ansible configuration
│   ├── ssh_config                        # SSH configuration
│   ├── tmp                               # Temporary files
│   └── vault_password                    # Default vault file
├── docs                                # Advanced documentation topics
│   ├── skel-start.md
│   └── skel-tips.md
├── group_vars                          # Group vars directory
│   ├── all.yml                           # Common variables to all hosts
│   ├── dev.yml                           # Dev env variables
│   ├── preprod.yml                       # Preprod env variables
│   └── prod.yml                          # Production env variables
├── host_vars                           # Host vars directory
├── inventory                           # Inventory directory
│   ├── default.ini -> dev.ini            # Default inventory to use
│   ├── dev.ini                           # Dev inventory
│   ├── preprod.ini                       # Preprod inventary
│   └── prod.ini                          # Production inventory
├── playbooks                           # Playbook directory
│   ├── 0_local_requirements.yaml         # Configure local system
│   ├── 1_target_test.yml                 # Test targets
│   ├── 2_target_requirements.yml         # Basic configuration of targets
│   └── 3_target_sysadmin.yml             # Advanced confivuration of targets
├── plugins                             # Plugin directory
│   ├── action                            # Action plugins
│   ├── callback                          # Callback plugins
│   ├── connection                        # Connection plugins
│   ├── filter                            # Filter plugins
│   ├── lookup                            # Lookup plugins
│   ├── modules                           # Modules plugins
│   └── vars                              # Vars plugins
└── roles                               # Roles directory
    ├── local                             # Locale roles
    ├── profiles                          # Profile roles
    ├── requirements.yml                  # Vendor roles list
    └── vendors                           # Vendor roles
'''

import os, sys
#Variables

HOME_DIR = os.getcwd()
PROJECT_NAME = input("Type Your Project Name: ")
TOP_DIR = ['config', 'docs', 'group_vars', 'host_vars', 'inventory', 'playbooks', 'plugins', 'roles']

# create the directory structure using class c_dir
class c_dir:
    def config():
        pwd_config = os.path.join(os.path.join(HOME_DIR, PROJECT_NAME), 'config')
        os.chdir(pwd_config)
        os.mkdir('ssh_config')
        os.mkdir('tmp')

        ansi_file = open('ansible.cfg', 'w')
        ansi_file.write('#Write your Ansible configuration here')
        ansi_file.close()
        vault_file = open('vault_password', 'w');vault_file.close()

    def docs():
        pwd_docs = os.path.join(os.path.join(HOME_DIR, PROJECT_NAME), 'docs')
        os.chdir(pwd_docs)
        ss = open('skel-start.md', 'w'); ss.close()
        sstips = open('skel-tips.md', 'w'); sstips.close()

    def group_vars():
        pwd_group_vars = os.path.join(os.path.join(HOME_DIR, PROJECT_NAME), 'group_vars')
        os.chdir(pwd_group_vars)

        for i in ['all.yml', 'dev.yml', 'preprod.yml', 'prod.yml']:
            req = open('%s'%i, 'w');req.close()

    def host_vars(): pass

    def inventory():
        pwd_inventory = os.path.join(os.path.join(HOME_DIR, PROJECT_NAME), 'inventory')
        os.chdir(pwd_inventory)

        for i in ['dev.ini','prepod.ini','prod.ini']:
            req = open('%s'%i, 'w');req.close()
        os.symlink('dev.yml', 'default.ini')

    def playbooks():
        pwd_inventory = os.path.join(os.path.join(HOME_DIR, PROJECT_NAME), 'playbooks')
        os.chdir(pwd_inventory)
        for i in ['0_local_requirements.yaml', '1_target_test.yml', '2_target_requirements.yml', '3_target_sysadmin.yml']:
            pb = open('%s'%i, 'w');pb.close()

    def plugins():
        pwd_inventory = os.path.join(os.path.join(HOME_DIR, PROJECT_NAME), 'plugins')
        os.chdir(pwd_inventory)
        for i in ['action', 'callback', 'connection', 'filter', 'lookup', 'modules']:
            os.mkdir('%s'%i)

    def roles():
        pwd_inventory = os.path.join(os.path.join(HOME_DIR, PROJECT_NAME), 'roles');os.chdir(pwd_inventory)
        for i in ['local', 'profiles', 'vendors']: os.mkdir('%s' % i)
        req = open('requirements.yml', 'w');req.close()


print("We are going to create the directory structure of ansible in %s" % HOME_DIR)
yn = str(input("Are you ok with that (y/n): "))

# if true then it will create the structure
if yn in ['yes', 'y', 'YES', 'Y', 'Yes']:
    # creating project name
    if os.path.exists(os.path.join(HOME_DIR, PROJECT_NAME)) and os.path.isdir(os.path.join(HOME_DIR, PROJECT_NAME)):
        print('The project with the same name is already there')
    elif os.path.exists(os.path.join(HOME_DIR, PROJECT_NAME)) and os.path.isfile(os.path.join(HOME_DIR, PROJECT_NAME)):
        print('A File is there with the Project name')
    else:
        os.mkdir(PROJECT_NAME)
        os.chdir(os.path.join(HOME_DIR, PROJECT_NAME))
        # creating top level dir
        for top_dir in TOP_DIR:
            os.mkdir(top_dir)

        # config dir creation
        c_dir.config();c_dir.docs();c_dir.group_vars();c_dir.inventory();c_dir.playbooks();c_dir.plugins();c_dir.roles()
        #Creating outside files
        os.chdir(os.path.join(HOME_DIR, PROJECT_NAME))

        #Read me file creation
        readme = open('Readme.txt', 'w');readme.write('#Enter about your Project');readme.close()

        #LICENSE file creation
        lic = open('LICENSE', 'w');lic.write('#License details of your project');lic.close()
        host = open('hosts', 'w');host.close()
        ansi_link = os.path.join(os.path.join(os.path.join(HOME_DIR, PROJECT_NAME), 'config'),'ansible.cfg')
        os.symlink(ansi_link,'ansible.cfg')
        print('Project created Successfully')

elif yn in ['no', 'n', 'NO', 'N', 'No']: print('yn is on no')
else: print('Go to the Hell')
