from fabric.api import *
from fabric.contrib.files import *

import xmlrpclib


def connection():

	api = xmlrpclib.ServerProxy('https://rpc.gandi.net/xmlrpc/')
	apikey = env["settings"]["accounts"]["gandi"]["api_key"]

	return api, apikey

@task
def version():
	api, key = connection()
	print(api.version.info(key))