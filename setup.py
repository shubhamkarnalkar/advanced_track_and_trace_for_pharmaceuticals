from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in advanced_track_and_trace_for_pharmaceuticals/__init__.py
from advanced_track_and_trace_for_pharmaceuticals import __version__ as version

setup(
	name="advanced_track_and_trace_for_pharmaceuticals",
	version=version,
	description="A solution for the track and trace of pharamceuticals products which needs to be moniored",
	author="Shubhamkar Nalkar",
	author_email="shubhamkar.nalkar@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
