#!/usr/bin/python3
""" Create an archive of the webstatic directory from AIrBnB_clone_v2
"""


from fabric.api import local
from datetime import datetime


def do_pack():
    """ A function to create an archive """
	
	time_now = datetime.now()
	time_string = time_now.strftime("%Y%m%d%H%M%S")

	try:
            local("mkdir -p versions")
            local("tar -cvzf versions/web_static_{}.tgz web_static".format(time_string))
            return ("versions/web_static_{}".format(time_string))

	except Exception as error:
            return None

