<<<<<<< HEAD
from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in tti/__init__.py
from tti import __version__ as version

setup(
	name="tti",
	version=version,
	description="App for TTI",
	author="Sione Taumoepeau",
	author_email="sione.taumoepeau@gmail.com",
=======
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in fwc_edu/__init__.py
from fwc_edu import __version__ as version

setup(
	name='fwc_edu',
	version=version,
	description='Application to manage FWC Education Department',
	author='Sione Taumoepeau',
	author_email='sione.taumoepeau@gmail.com',
>>>>>>> 4c8ef093c7eb0eb4efece16aa09f7f910d1c0d68
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
