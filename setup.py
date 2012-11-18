try : 
    from setuptools import setup
except ImportError :
    from distutils.core import setup


config = {
    'description' : 'Tracks Steep and Cheap',
    'author' : 'Subhodeep Moitra',
    'url' : 'https://github.com/smoitra87/steephound.git' ,
    'download_url' : \
		'https://github.com/smoitra87/steephound/downloads',
    'author_email' : 'subho@cmu.edu',
    'version' : '0.1',
	#'py_modules' : ['steephound'],
	'scripts' : ['steephound.py'],
    'name' : 'SteepHound'
}

setup(**config)

