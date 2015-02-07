from fabric.api import *
from fabric.colors import *

from . import mysql, django, repo, wordpress, apache, raw

import json
import os.path


@task
def here():
	env["hosts"] = ["localhost"]
	env["deployments"]  = json.load(open("deployments.json"))
	env["settings"]  = json.load(open("settings.json"))


@task
def check_deployments():
	with hide('output'):
		for server in env["deployments"]:
			if os.path.isfile(env["settings"]["base_paths"]["apache"]+"/sites-enabled/%s" % env["deployments"][server]["vhost"]):
				env["deployments"][server]["apache"] = True
				the_color = green
			else:
				env["deployments"][server]["apache"] = False
				the_color = red

			localip = run("ifconfig | grep inet | grep -v 127.0.0.1")
			pinged = run("ping %s -c 1" % server)
			ip = pinged.split("(")[1].split(")")[0]
			print( the_color(server) + " " + the_color("deployed") + " " + env["deployments"][server]["mode"] + " - " + yellow(ip))

		json.dump(env["deployments"], open("deployments.json", "wb"), indent=4)
