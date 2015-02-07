from fabric.api import *
from fabric.contrib.files import *

from github3 import login
from bitbucket.bitbucket import Bitbucket
 
mixes = {
	"default":["django", "python-social-auth", "psycopg2", "celery", "redis"],
}



@task
def startproject(name, mode="default"):
	dj_base = env["settings"]["django"]
	with prefix("source virtualenvwrapper.sh"):
		with cd(dj_base):
			run("mkvirtualenv %s" % name)
			with prefix("workon %s" % name):
				for pkg in mixes[mode]:
					run("pip install %s" % pkg)
				run("mkdir %s" % name)
				with cd(name):
					run("django-admin startproject %s" % name)
					with cd(name):
						run("python manage.py startapp core")