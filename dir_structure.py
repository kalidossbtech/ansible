#Create the directory structure of ansible 
# Name : kalidoss
# Email : kalidossbtech@gmail.com
#This file is under Editing for upgradation


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
pwd = os.getcwd()
HOME_DIR = pwd
PROJECT_NAME = 'project_name' ##sys.argv[2]
TOP_DIR = ['config', 'docs', 'group_vars', 'host_vars', 'inventory', 'playbooks', 'plugins', 'roles']

#create the directory structure using class c_dir
class c_dir:
	def config() :
		pwd_config = os.path.join(os.path.join(HOME_DIR,PROJECT_NAME),'config')
		os.chdir(pwd_config)
		os.mkdir('ssh_config') 
		os.mkdir('tmp') 
		ansi_file = open('ansible.cfg','w')
		ansi_file.write('#Write your Ansible configuration here')
		ansi_file.close()
		vault_file = open('vault_password','w')
		vault_file.close()
	def docs() : 
		pwd_docs = os.path.join(os.path.join(HOME_DIR,PROJECT_NAME),'docs')
		os.chdir(pwd_docs)
		ss = open('skel-start.md','w')
		ss.write('')
		ss.close
		sstips = open('skel-tips.md','w')
		sstips.write('')
		sstips.close

		

	def group_vars() : 
		pwd_group_vars = os.path.join(os.path.join(HOME_DIR,PROJECT_NAME),'group_vars')
		os.chdir(pwd_group_vars)
		
		g_all  = open('all.yml','w')
		g_all.write('')
		g_all.close()
		
		g_dev = open('dev.yml','w')
		g_dev.write('')
		g_dev.close()
		
		g_link = os.mk
		g_preprod = open('preprod.yml','w')
		g_preprod.write('')
		g_preprod.close()
		
		g_prod = open('prod.yml','w')
		g_prod.write('')
		g_prod.close()




	def host_vars() : pass

	def inventory() : 
		pwd_inventory = os.path.join(os.path.join(HOME_DIR,PROJECT_NAME),'inventory')
		os.chdir(pwd_inventory)
		
		i_dev = open('dev.ini','w')
		i_dev.write('')
		i_dev.close()
		
		i_preprod = open('preprod.ini','w')
		i_preprod.write('')
		i_preprod.close()
		
		i_prod = open('preod.ini','w')
		i_prod.write('')
		i_prod.close()

		#symbolic link creation


	def playbooks() : pass
	def plugins() : pass 
	def roles() : pass
		


print("We are going to create the directory structure of ansible in %s" %pwd)
yn = str(input("Are you ok with that (y/n): "))

#if true then it will create the structure
if yn in ['yes',  'y', 'YES', 'Y', 'Yes']  :
	print('yn is on yes')
	#creating project name
	if os.path.exists(os.path.join(HOME_DIR,PROJECT_NAME)) and os.path.isdir(os.path.join(HOME_DIR,PROJECT_NAME)) :
		print('The project with the same name is already there')
	elif  os.path.exists(os.path.join(HOME_DIR,PROJECT_NAME)) and os.path.isfile(os.path.join(HOME_DIR,PROJECT_NAME)) :
		print('A File is there with the Project name')
	else :
		os.mkdir(PROJECT_NAME)
		os.chdir(os.path.join(HOME_DIR,PROJECT_NAME))
		print('went inside project')
	#creating top level dir
		for top_dir in TOP_DIR :
			os.mkdir(top_dir)
			#print('top_dir_created')

		#config dir creation


		c_dir.config()
		c_dir.docs()
		c_dir.group_vars()
		c_dir.inventory()


elif yn in ['no', 'n', 'NO', 'N', 'No'] : 
	print('yn is on no')
else :
	print('go to the hell')	