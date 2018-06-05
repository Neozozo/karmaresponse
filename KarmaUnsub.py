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
from Mindbaz.download_MB_unsubs import *
from Cerberoos.download_CB_unsubs import *
from databases_unsubs import *
from Mails.mail_unsub import *

params = pd.read_json('params.json')  # read file
params = params['params'].to_dict() # read the 'params' bloc

mail_list = params['mail_list']
folder_name = params['folder_name']
server_MB = params['server_MB']
usernames_MB = params['usernames_MB']
passwords_MB = params['passwords_MB']
DB_MB = usernames_MB
server_CB = params['server_CB']
usernames_CB = params['usernames_CB']
passwords_CB = params['passwords_CB']
DB_CB = params['DB_CB']
destination = "csv/"
filename = 'unsubs_' + str(day) + '.csv'
day = str(int(dt.datetime.now().strftime('%Y%m%d')))  # Date of the day in format 'YYYYMMDD'
weekly = dt.datetime.now() - dt.timedelta(days=7)
daily = dt.datetime.now() - dt.timedelta(days=0)

list_dates = []
for k in range(0,7):
    kdate = dt.datetime.now() - dt.timedelta(days=k)
    list_dates.append(kdate)

start = time.time() # Start measuring time

print('\n\n\n---- Starting DrSender ----\n\n\n')
os.chdir('./DrSender')
subprocess.call("php DrSender.php") # call the DrSender script to download unsubscribers
os.chdir('..')
print('\n\n\n---- Starting Cerberoos ----\n\n\n')
os.chdir('./Cerberoos')
download_CB_unsubs(usernames_CB,passwords_CB,DB_CB,list_dates)
os.chdir('..')
print('\n\n\n---- Starting Checking Emails ----\n\n\n')
get_mail_unsubs(mail_list, folder_name, daily)
print('\n\n\n---- Starting Mindbaz ----\n\n\n')
os.chdir('./Mindbaz')
download_MB_unsubs(usernames_MB,passwords_MB,DB_MB,list_dates)
os.chdir('..')
print('\n\n\n++++ Starting Merging ++++\n\n\n')
for current_date in list_dates:
    Mailunsubs = get_mail_unsubs(mail_list, folder_name, current_date)
    previous_date = current_date - dt.timedelta(days=1)
    previous_date = previous_date.strftime('%Y%m%d')
    current_date = current_date.strftime('%Y%m%d')
    DS,MB,CB,Mails = get_unsub_files(current_date)
    DSunsubs = merge_drsender(DS, current_date)
    DSunsubsDm1 = merge_drsender(DS, previous_date)
    MBunsubs = merge_mindbaz(MB, current_date)
    MBunsubsDm1 = merge_drsender(DS, previous_date)
    CBunsubs = merge_cerberoos(CB, current_date)
    CBunsubsDm1 = merge_drsender(DS, previous_date)
    merge_all_daily(current_date,DSunsubs,DSunsubsDm1,MBunsubs,MBunsubsDm1,Mailunsubs,CBunsubs,CBunsubsDm1)

end = time.time() # End measuring time

print(end-start)
