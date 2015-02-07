from fabric.api import *
from fabric.contrib.files import *


@task
def create_vhost(mode, name, aliases, base_path):
	apache_base = env["settings"]["base_paths"]["apache"]
	upload_template("fabifile/templates/apache/%s.template" % mode, apache_base+"sites-available/"+name, context={"name":name, "aliases":aliases, "root":base_path}, use_jinja=True )

@task
def enable_vhost(name):
	apache_base = env["settings"]["base_paths"]["apache"]
	run("ln -s %s/sites-enabled/%s %s/sites-available/%s" % (apache_base, name, apache_base, name, ))

@task
def reload_conf():
	apache_base = env["settings"]["base_paths"]["apache"]
	run("service apache reload")

@task
def add_vhost(mode, name, aliases, base_path):
	execute(create_vhost, mode, name, aliases, base_path)
	execute(enable_vhost, name)
	execute(reload_conf)
