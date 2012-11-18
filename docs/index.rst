.. SteepHound documentation master file, created by
   sphinx-quickstart on Sat Nov 17 21:09:39 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to SteepHound's documentation!
======================================
Steep Hound is a tracker for `Steep and Cheap <http://steepandcheap.com>`_ , a website that displays one awesome deal at a time. 

Downloading SteepHound
----------------------

You can get the latest version of steephound from
https://github.com/smoitra87/steephound/archive/master.zip . Unzip the folder using ::

	$ unzip steephound-master.zip
	

Alternatively, if you have git installed you can pull the source from github, like so ::

	$ git clone http://github.com/smoitra87/steephound.git

.. _install:

Installing SteepHound (Not Required)
------------------------------------

This step is not really required. However if you would like to permanently place steephound in your system path, you can proceed with this step. 
. ::

	$ sudo python setup.py install

Running SteepHound
------------------
If you have installed steephound in step install_ , running it is fairly easy. Execute the following command from anywhere ::
	
	$ steephound.py

Otherwise, you will need to be in the same directory as the downloaded folder and then run ::
	
	$ python steephound.py

You need to keep the terminal active in order for the script to run indefinitely. 
Alternatively you can use `nohup <http://en.wikipedia.org/wiki/Nohup>`_ and 
`screen <http://www.rackaid.com/resources/linux-screen-tutorial-and-how-to/>`_  in order to keep the program running in the background forever. 



Module
------
See below for description of :mod:`steephound` modules

Contents:

.. toctree::
	:maxdepth: 2

	modules




---------------------------------

:Contributors: Subhodeep Moitra, Sam Taggart


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

