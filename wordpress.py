from fabric.api import *
from fabric.contrib.files import *

import requests
import re

wp_base ="/var/www"
wp_ita = "https://it.wordpress.org/wordpress-4.1-it_IT.zip"

@task
def create(name):
	salt = requests.get("https://api.wordpress.org/secret-key/1.1/salt/").text.split("\n")
	print salt
	
	with cd(wp_base):
		run("wget %s" % wp_ita)
		run("unzip wordpress-4.1-it_IT.zip")
		run("mv wordpress %s" % name)
		#run("git clone https://github.com/WordPress/WordPress.git")
		#run("mv WordPress %s" % name)
		run("chown -R www-data:www-data %s/%s" % (wp_base, name))
		with cd(name):
			with cd("wp-content/plugins"):
				run("git clone https://github.com/rilwis/meta-box.git")

			run("cp wp-config-sample.php wp-config.php")
			sed("wp-config.php", "database_name_here", name)
			sed("wp-config.php", "username_here", env["settings"]["mysql"]["u"])
			sed("wp-config.php", "password_here", env["settings"]["mysql"]["p"])
			sed("wp-config.php", """define[(]'AUTH_KEY',         'put your unique phrase here'[)];""", salt[0])
			sed("wp-config.php", """define[(]'SECURE_AUTH_KEY',  'put your unique phrase here'[)];""", salt[1])
			sed("wp-config.php", """define[(]'LOGGED_IN_KEY',    'put your unique phrase here'[)];""", salt[2])
			sed("wp-config.php", """define[(]'NONCE_KEY',        'put your unique phrase here'[)];""", salt[3])
			sed("wp-config.php", """define[(]'AUTH_SALT',        'put your unique phrase here'[)];""", salt[4])
			sed("wp-config.php", """define[(]'SECURE_AUTH_SALT', 'put your unique phrase here'[)];""", salt[5])
			sed("wp-config.php", """define[(]'LOGGED_IN_SALT',   'put your unique phrase here'[)];""", salt[6])
			sed("wp-config.php", """define[(]'NONCE_SALT',       'put your unique phrase here'[)];""", salt[7])
		execute("wordpress.create_theme", name)
		execute("mysql.create", name)

@task
def create_plugin(name, plugin_name):
	with cd(wp_base):
		with cd(name):
			with cd("wp-content/plugins"):
				run("git clone https://github.com/hlashbrooke/WordPress-Plugin-Template.git %s" % plugin_name)

@task
def create_theme(name, theme_name):
	with cd(wp_base):
		with cd(name):
			with cd("wp-content/themes"):
				run("git clone https://github.com/roots/roots.git")
				run("mv roots %s" % theme_name)
				with cd(theme_name):
					run("npm install")


