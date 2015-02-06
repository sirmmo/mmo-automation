from fabric.api import *
 
from fabric.contrib.files import *

from github3 import login
from bitbucket.bitbucket import Bitbucket


@task
def create_repo(name, private=False):
	if private:
		bb = Bitbucket(accounts["bb"]["username"], accounts["bb"]["password"])
		success, result = bb.repository.create(name, private=private)
	else:
		gh = login(accounts["gh"]["username"], password=accounts["gh"]["password"])
		gh.create_repo(name, gitignore_template="Python", auto_init=True)
		print ("repo created")