#!/usr/bin/python3
"""Fabric deployment module"""
from fabric.api import *
from datetime import datetime
from os import path

env.hosts = ['35.229.40.200', '35.229.23.118']
env.user = "ubuntu"
env.key_filename = "~/.ssh/holberton"


def do_deploy(archive_path):
    """Deploys our website to our servers!"""

    if not path.exists(archive_path):
        return False

    filename = archive_path.split("/")[-1]
    noext, ext = path.splitext(filename)
    remotepath = "/data/web_static/releases/"

    try:
        put(archive_path, '/tmp')
        run('mkdir -p {}{}/'.format(remotepath, noext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(filename, remotepath, noext))
        run('rm -f /tmp/{}'.format(filename))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(remotepath, noext))
        run('rm -rf {}{}/web_static'.format(remotepath, noext))
        run('rm -rf /data/web_static/current')
        run('ln -sf {}{}/ /data/web_static/current'.format(remotepath, noext))
        print("New version deployed!")
    except:
        return False
