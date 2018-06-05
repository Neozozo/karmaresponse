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
__date__ = 'Thu May 31 00:00:00 2018'

# ===============================================================================
# Import statements
# ===============================================================================


import sys
from ftplib import FTP
import os
import time
import logging
import numpy as np
import datetime as dt
import pysftp
import pandas as pd
import zipfile


# Define log file and specifications
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, filename="../logfile", filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")

np.seterr(divide='ignore', invalid='ignore')

params = pd.read_json('params.json')  # read file
params = params['params'].to_dict() # read the 'params' bloc

server_CB = params['server_CB']
usernames_CB = params['usernames_CB']
passwords_CB = params['passwords_CB']
DB_CB = params['DB_CB']
destination = "csv/"
day = str(int(dt.datetime.now().strftime('%Y%m%d')))  # Date of the day in format 'YYYYMMDD'
filename = 'unsubs_' + str(day) + '.csv'

list_dates = []
for k in range(0,7):
    kdate = dt.datetime.now() - dt.timedelta(days=k)
    kdate = kdate.strftime('%Y%m%d')
    list_dates.append(kdate)

# Make connection to sFTP
def downloadFile(user, pw, source, list_dates):
    try :
        ftp = FTP(server_CB)
        ftp.login(user,pw)
        if not os.path.exists(destination + source + '/'):
            # create csv directory if not existing
            os.makedirs(destination + source)
        for current_date in list_dates:
            filematch = '*.*' # a match for any file in this case, can be changed or left for user to input
            for filename in ftp.nlst(filematch): # Loop - looking for matching files
                if filename.startswith('Unsubscribers_{}'.format(current_date)):
                    if os.path.exists(destination + source + '/' + filename):
                        print('\n' + source + '/' + filename + ' Already downloaded\n')
                    else:
                        fhandle = open(destination + source + '/' + filename, 'wb')
                        print('\nFinished downloading ' + source + '\n')
                        ftp.retrbinary('RETR ' + filename, fhandle.write)
                        fhandle.close()
                        unzipping(current_date)
                        print('\nUnzipped ' + source + '\n')
        ftp.close()
    except Exception as error:
        print(error)

def download_CB_unsubs(usernames,passwords,sources,list_dates):
    for k in range(0,len(usernames)):
        downloadFile(usernames[k],passwords[k],sources[k],list_dates)

def unzipping(day):
    try :
        DBdirs = os.listdir('csv')
        for DB in DBdirs:
            list_files = os.listdir('csv/' + DB + '/')
            for zipzip in list_files:
                if zipzip.startswith('Unsubscribers_{}'.format(day)):
                    csvfile = 'unsubs_{}.csv'.format(day)
                    csv_in_zip = zipzip.split('.')[0] + '.csv'
                    if not os.path.exists('csv/' + DB + '/' + csvfile):
                        zip_ref = zipfile.ZipFile('csv/' + DB + '/' + zipzip, 'r')
                        zip_ref.extractall('csv/' + DB + '/')
                        zip_ref.close()
                        os.rename('csv/' + DB + '/' + csv_in_zip, 'csv/' + DB + '/' + 'unsubs_{}.csv'.format(day))
    except Exception as error:
        print(error)

if __name__ == "__main__":
    # code to be executed only if this file is called with 'python file.py <arguments>'
    pass
