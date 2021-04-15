#!/usr/bin/python3
"""Fabric tar packing module"""
from fabric.api import local
from datetime import datetime
from os import path


def do_pack():
    """Packs our website in a .tgz archive"""

    try:
        if not path.exists("versions"):
            local("mkdir -p versions")
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = "versions/web_static_{:s}.tgz".format(now)
        local("tar -cvzf {:s} web_static".format(filename))
        return filename
    except:
        return None
