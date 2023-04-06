#!/usr/bin/python3
""" A fabric script to compress a file"""

from fabric.api import run, env, put
import os.path

env.hosts = ["54.162.93.251", "100.25.3.37"]

def do_deploy(archive_path):
    
    if not os.path.isfile(archive_path):
        return False
    compressed_file = archive_path.split("/")[-1]
    no_extension = compressed_file.split(".")[0]
    
    try:
        remote_path = "/data/web_static/releases/{}".format(no_extension)
        sym_link = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("mkdir - p {}".format(remote_path))
    
        run("tar -xvzf /tmp/{} -C {}".format(compressed_file, remote_path))
        run("rm /tmp/{}".format(compressed_file))
        run("ln -sf {} {}".format(remote_path, sym_link))
   
        return True
    except Exception as e:
        return False
