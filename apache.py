from fabric.api import *
from fabric.contrib.files import *

apache_base = "/etc/apache2/"

@task
def create_vhost(mode, name, aliases, base_path):
	upload_template("fabifile/templates/apache/%s.template" % mode, apache_base+"sites-available/"+name, context={"name":name, "aliases":aliases, "root":base_path}, use_jinja=True )

@task
def enable_vhost(name):
	run("ln -s %s/sites-enabled/%s %s/sites-available/%s" % (apache_base, name, apache_base, name, ))

@task
def reload_conf():
	run("service apache reload")

@task
def add_vhost(mode, name, aliases, base_path):
	execute(create_vhost, mode, name, aliases, base_path)
	execute(enable_vhost, name)
	execute(reload_conf)
