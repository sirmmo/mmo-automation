from fabric.api import *
from fabric.contrib.files import *



@task 
def create(name):
	run("""mysql -u %s -p%s -e "create database %s;" """ % (env["settings"]["mysql"]["u"], env["settings"]["mysql"]["p"], name))
				

