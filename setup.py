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
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
