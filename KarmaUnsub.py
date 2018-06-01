#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Execute the whole process of Downloading, Merging, Sorting and Updating of Unsubscribers from KarmaResponse databases on Mindbaz, DrSender and Cerberoos
"""

# ===============================================================================
# Metadata
# ===============================================================================

__author__ = 'David Gosset'
__contact__ = 'davidgosset1994@gmail.com'
__copyright__ = ''
__license__ = ''
__date__ = 'Fri Jun 01 00:00:00 2018'

# ===============================================================================
# Import statements
# ===============================================================================

import sys
import os
import subprocess
import logging
import time

start = time.time() # Start measuring time

print('\n\n\n---- Starting DrSender ----\n\n\n')
os.chdir('./DrSender')
subprocess.call("php DrSender.php") # call the DrSender script to download unsubscribers
print('\n\n\n---- Starting Cerberoos ----\n\n\n')
os.chdir('..')
os.chdir('./Cerberoos')
subprocess.call("python download_unsubs.py") # call the Cerberoos script to download unsubscribers
print('\n\n\n---- Starting Mindbaz ----\n\n\n')
os.chdir('..')
os.chdir('./Mindbaz')
subprocess.call("python download_unsubs.py") # call the Mindbaz script to download unsubscribers
print('\n\n\n++++ Starting Merging ++++\n\n\n')
os.chdir('..')
subprocess.call("python ./databases_unsubs.py") # call the Merging script

end = time.time() # End measuring time

print(end-start)
