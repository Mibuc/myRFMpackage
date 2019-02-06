# setup.py

# This file ensures that all commands operating on your module work correctly
# setup.py is the centre of all activity in building, distributing and installing modules.

from setuptools import setup

# readme() will include the README in my package
def readme():
	with open('README.rst') as f:
		return f.read()

setup(name='myRFMpackage',
	description='What the package does',
	version='1.0',
	py_modules=['calculateRFM'],
	zip_safe=False,
	install_requires=['pandas', 'numpy'],
	author='Michael Bucher',
	packages=['myRFMpackage'])
