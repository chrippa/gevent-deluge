#!/usr/bin/env python

try:
    from setuptools import setup

    install_requires = ["gevent"]
    extrakws = {"install_requires": install_requires}
except ImportError:
    from distutils.core import setup
    extrakws = {}

from geventdeluge import __version__

setup(name="gevent-deluge",
      version=__version__,
      description="An implementation of the Deluge RPC protocol using gevent.",
      url="",
      author="Christopher Rosell",
      author_email="chrippa@tanuki.se",
      license="Simplified BSD",
      packages=["geventdeluge"],
      **extrakws
)
