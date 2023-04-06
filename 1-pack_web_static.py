#!/usr/bin/python3
"""a fabric script to create an archive file"""

from fabric.api import local
from datetime import datetime

def do_pack():
    """ A function that compresses a file """
    
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(current_time)

	""" Create a directory named versions
	create an arhcive of webstatic
	return the path of the archive file
	"""   
    try:
        local("mkdir -p versions")
        local("tar -cvzf {} web_static/".format(file_path))        
        return "{}".format(file_path)

    except Exception as error:
        return None
        
