#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Download unsubscribers CSV from Mindbaz's FTP
"""

# ===============================================================================
# Metadata
# ===============================================================================

__authors__ = 'David Gosset'
__contact__ = 'davidgosset1994@gmail.com'
__copyright__ = ''
__license__ = ''
__date__ = 'Fri May 11 00:00:00 2018'

# ===============================================================================
# Import statements
# ===============================================================================


import sys
import ftplib
import os
import time
import logging
import numpy as np
import datetime as dt
import pysftp
import pandas as pd


# Define log file and specifications
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, filename="../logfile", filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")

np.seterr(divide='ignore', invalid='ignore')

params = pd.read_json('../params.json')  # read file
params = params['params'].to_dict() # read the 'params' bloc

server = params['server']
username = params['username']
password = params['password']
sources = username
destination = "csv/"
day = str(int(dt.datetime.now().strftime('%Y%m%d')))  # Date of the day in format 'YYYYMMDD'
filename = 'unsubs_' + str(day) + '.csv'

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

# Make connection to sFTP
def downloadFile(user, pw, source, FILENAME):
    try :
        with pysftp.Connection(server,username=user,password=pw,cnopts = cnopts) as sftp:
            if not os.path.exists(destination + str(source.split('_')[1])):
                # create csv directory if not existing
                os.makedirs(destination + str(source.split('_')[1]))
            os.chdir(destination + str(source.split('_')[1]))
            sftp.isfile('/' + source + '/export/' + FILENAME) ## TRUE
            file = sftp.get('/' + source + '/export/' + FILENAME)
            print("Downloaded: " + destination + str(source.split('_')[1]) + '/' + FILENAME)
            os.chdir('../..')
        sftp.close()
    except Exception as error:
        print(error)

def download_all_unsubs(username,password,sources,filename):
    for k in range(0,len(username)):
        downloadFile(username[k],password[k],sources[k],filename)

download_all_unsubs(username,password,sources,filename)
