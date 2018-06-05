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

params = pd.read_json('params.json')  # read file
params = params['params'].to_dict() # read the 'params' bloc

server_MB = params['server_MB']
usernames_MB = params['usernames_MB']
passwords_MB = params['passwords_MB']
sources_MB = usernames_MB
destination = "csv/"
day = str(int(dt.datetime.now().strftime('%Y%m%d')))  # Date of the day in format 'YYYYMMDD'
filename = 'unsubs_' + str(day) + '.csv'

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

list_dates = []
for k in range(0,7):
    kdate = dt.datetime.now() - dt.timedelta(days=k)
    kdate = kdate.strftime('%Y%m%d')
    list_dates.append(kdate)

# Make connection to sFTP
def downloadFile(user, pw, source, list_dates):
    try :
        with pysftp.Connection(server_MB,username=user,password=pw,cnopts = cnopts) as sftp:
            if not os.path.exists(destination + str(source.split('_')[1])):
                # create csv directory if not existing
                os.makedirs(destination + str(source.split('_')[1]))
            for current_date in list_dates:
                os.chdir(destination + str(source.split('_')[1]))
                FILENAME = 'unsubs_' + str(current_date) + '.csv'
                sftp.isfile('/' + source + '/export/' + FILENAME) ## TRUE
                if os.path.exists(FILENAME):
                    print('\n' + str(source.split('_')[1]) + ' ' + FILENAME + ' Already downloaded\n')
                else:
                    file = sftp.get('/' + source + '/export/' + FILENAME)
                    print("\nFinished downloading " + str(source.split('_')[1]) + '\n')
                os.chdir('../..')
        sftp.close()
    except Exception as error:
        print(error)

def download_MB_unsubs(usernames,passwords,sources,list_dates):
    for k in range(0,len(usernames)):
        downloadFile(usernames[k],passwords[k],sources[k],list_dates)

if __name__ == "__main__":
    # code to be executed only if this file is called with 'python file.py <arguments>'
    pass
