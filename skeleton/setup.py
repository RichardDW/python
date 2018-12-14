'''
To create a solid testing / skeleton framework
install the following packages
- pip
- distribute
- nose
- virtualenv
'''

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'R. de Wolff',
    'url': 'http://incharge-it.nl',
    'download_url': 'http://incharge-it.nl',
    'author_email': 'richard@incharge-it.nl',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
