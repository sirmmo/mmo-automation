from fabric.api import *

from local_settings import settings

from . import mysql, django, repo, wordpress, apache

@task
def here():
	env["hosts"] = ["localhost"]

	env["settings"] = settings


