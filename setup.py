from setuptools import setup

import sys


if not sys.version_info[0] == 2:
	sys.exit("Error: Launchpad_rtmidi.py requires Python 2")


setup(
	name = "launchpad_rtmidi_py",
	version = "0.7.0",
	description = "A Novation Launchpad control suite for Python ('python-rtmidi' fork of FMMT666 package)",
	long_description = open('README').read(),
	author = "Dave Hilowitz",
	author_email = "dhilowitz@users.noreply.github.com",
	license = "CC BY 4.0",
	keywords = "novation launchpad midi rtmidi",
	url = "https://github.com/dhilowitz/launchpad_rtmidi.py",
	packages = ["launchpad_rtmidi_py"],
	install_requires = ["python-rtmidi"]
)
