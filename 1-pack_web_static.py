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
<<<<<<< HEAD
         
        """create an archive for webstatic"""
        local("tar -cvzf {} web_static/".format(file_path))
        
=======
     
        """create an archive for webstatic"""
        local("tar -cvzf {} web_static/".format(file_path))
     
>>>>>>> b23b4af07966bdf44444fdfe0a72fa24fdb1ec8a
        """return the path to the archive file created"""
        return "{}".format(file_path)

        """return exception errors"""
    except Exception as e:
        return None
