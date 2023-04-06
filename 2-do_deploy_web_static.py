#!/usr/bin/python3
"""A fabric script to transfer decompressed webstatic
files to remote servers"""

from fabric.api import run, env, put
import os.path

env.hosts = ['52.91.118.25', '52.91.125.236']
env.key_source = '~/.ssh/school'
env.user = 'ubuntu'


def do_deploy(archive_path):
    """ Deploy code to different webservers and decompress"""

    if not os.path.isfile(archive_path):
        return False
    compressed_file = archive_path.split("/")[-1]
    no_extension = compressed_file.split(".")[0]

    try:
        remote_path = "/data/web_static/releases/{}/".format(no_extension)
        sym_link = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("sudo mkdir - p {}".format(remote_path))  #make directory
        run("sudo tar -xvzf /tmp/{} -C {}".format(compressed_file, remote_path))

    """remove compressed file"""
        run("sudo rm /tmp/{}".format(compressed_file)) 
    """Create symbolic link"""
        run("sudo ln -sf {} {}".format(remote_path, sym_link))
        return True
    except Exception as error:
        return False
