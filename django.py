from fabric.api import *
from fabric.contrib.files import *

from github3 import login
from bitbucket.bitbucket import Bitbucket
 
mixes = {
	"default":["django", "python-social-auth", "psycopg2", "celery", "redis"],
}

