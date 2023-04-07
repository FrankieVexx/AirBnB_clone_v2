#!/usr/bin/python3
"""
Fabric script to deploy web static content
"""

from fabric.api import env, put, run
from os.path import exists
import os

env.hosts = ['52.91.118.25', '52.91.125.236']
env.user = 'ubuntu'
env.key_filen = '~/.ssh/school'


def do_deploy(archive_path):
    """
    Deploys an archive to the web servers
    """
    """ Check for archive_path """
    if not exists(archive_path):
        return False

    """ file names with and without extension """
    arch_name = os.path.basename(archive_path)
    arch_name_minus = os.path.splitext(arch_name)[0]

    try:
        """ Save archive to tmp on the web servers """
        put(archive_path, "/tmp/")

        """ Create directory for the deployed files"""
        run("sudo mkdir -p /data/web_static/releases/{}/"
            .format(arch_name_minus))

        """ Decompress the archive into the we_static folder """
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(arch_name, arch_name_minus))

        """ Delete the archive from the server """
        run("sudo rm /tmp/{}".format(arch_name))

        """ Move the files to a new folder and delete the old symbolic link """
        run("sudo mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/"
            .format(arch_name_minus, arch_name_minus))
        run("sudo rm -rf /data/web_static/releases/{}/web_static"
            .format(arch_name_minus))

        """ Delete the old symbolic link and create a new one """
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}/ \
                /data/web_static/current".format(arch_name_minus))

        return True

    except Exception as e:
        return False
