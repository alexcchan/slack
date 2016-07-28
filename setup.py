#!/usr/bin/python

from distutils.core import setup

setup(
	# Basic package information.
	name = 'slack',
	version = '0.0.0',
	packages = ['slack'],
	include_package_data = True,
	install_requires = ['httplib2', 'simplejson'],
	url = 'https://github.com/alexcchan/slack/tree/master',
	keywords = 'slack api',
	description = 'Slack API Wrapper for Python',
	classifiers = [
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Internet'
	],
)


