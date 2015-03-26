#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
  name="VKMusic",
  version="0.1.2",
  packages=['vkmusic'],
  install_requires=['requests', 'vk_api'],
  include_package_data=True,
  author="Andrii Korzh",
  author_email="Andrii.Korzh@gmail.com",
  description="Extremely small tool to export audios from vk.com",
  license='BSD',
  keywords="vk music",
  url="http://korzhyk.github.com/VKMusic/",   # project home page, if any
  zip_safe=True,
  entry_points="""
  [console_scripts]
     vkmusic=vkmusic.runner:main
  """
)