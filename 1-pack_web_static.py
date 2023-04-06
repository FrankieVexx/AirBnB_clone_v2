#!/usr/bin/python3
"""A script to create an archive file webstatic"""
from fabric.api import local
from datetime import datetime

def do_pack():
    """ Function to compress a file """
    
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(current_time)
   
    try:
        """create a directory called versions"""
        local("mkdir -p versions")
         
        """create an archive for webstatic"""
        local("tar -cvzf {} web_static/".format(file_path))
        
        """return the path to the archive file created"""
        return "{}".format(file_path)

        """return exception errors"""
    except Exception as e:
        return None
        
