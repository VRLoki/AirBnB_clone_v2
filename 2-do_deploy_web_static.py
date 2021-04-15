#!/usr/bin/python3
"""
    Fabric script that distributes an archive to the web servers.
"""
from os import path
from fabric.api import env, put, run

env.hosts = ['35.229.40.200', '35.229.23.118']


def do_deploy(archive_path):
    """ Function that distributes the archive.

    Args:
        archive_path (str): the path of the archive to deploy on the servers.
    """

    if not path.exists(archive_path):
        return False

    name = archive_path.split("/")[-1]
    name_noext = name.split(".")[0]

    remote = "/data/web_static/releases/"

    try:
        put(archive_path, '/tmp')
        run('mkdir -p {}{}/'.format(remote, name_noext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(name, remote, name_noext))
        run('rm /tmp/{}'.format(name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(remote, name_noext))
        run('rm -rf {}{}/web_static'.format(remote, name_noext))
        run('rm -rf /data/web_static/current')
        run('ln -sf {}{}/ /data/web_static/current'.format(remote, name_noext))
        print("New version deployed!")
        return True

    except:
        return False
