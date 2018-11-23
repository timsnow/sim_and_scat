#!/usr/bin/env python

from setuptools import setup

setup(name='sim_and_scat',
	  version='0.0.1',
	  description='Python package to build appropriate environment for running the sim_and_scat open educational resource',
	  author='Andrew R. McCluskey, Adam R. Symington, James Grant, Benjamin J. Morgan, Stephen C. Parker, and Karen J. Edler',
	  author_email='a.r.mccluskey@bath.ac.uk, k.edler@bath.ac.uk',
	  url='https://arm61.github.io/sim_and_scat',
	  setup_requires=[
	  	'numpy',
	  	'scipy',
	  	'pylj',
	  	'conda',
	  	'matplotlib'
	  ],
	  install_requires=[
	  	'numpy',
	  	'scipy',
	  	'pylj',
	  	'conda',
	  	'matplotlib',
	  	'notebook'
	  ])