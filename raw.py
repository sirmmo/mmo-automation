from fabric.api import *
from fabric.contrib.files import *

@task
def create(name):
	base_path = env["settings"]["base_paths"]["taw"]	
	with cd(base_path):
		run("mkdir %s" % name)

		
