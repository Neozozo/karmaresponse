#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Get all emails sent to 'unsubscribe@karmaresponse.com' and 'info@karmaresponse.com' to create and export a csv file to be merged with other
    databases csv in order to unsubscribe all of them from all databases
"""

# ===============================================================================
# Metadata
# ===============================================================================


__authors__ = 'David Gosset'
__contact__ = 'davidgosset1994@gmail.com'
__copyright__ = ''
__license__ = ''
__date__ = 'Thu May 10 00:00:00 2018'

# ===============================================================================
# Import statements
# ===============================================================================

import numpy as np
import csv
import os
import time
import datetime as dt
import logging
import win32com.client
import pandas as pd


# Define log file and specifications
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, filename="../logfile", filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")

np.seterr(divide='ignore', invalid='ignore')

params = pd.read_json('/../params.json')  # read file
params = params['params'].to_dict() # read the 'params' bloc

mail_list = params['mail_list']
folder_name = params['folder_name']
yesterday = dt.datetime.now() - dt.timedelta(days=1)
yesterday = yesterday.strftime('%d/%m/%Y')
print(yesterday)

# ===============================================================================
# Class & functions
# ===============================================================================

def get_mails(mail, folder_name,startDate):
    day = str(int(dt.datetime.now().strftime('%Y%m%d'))) # Date of the day in format 'YYYYMMDD'
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.Folders(mail).Folders(folder_name)
    print(inbox.Name)
    unsub = ['\n']
    messages = inbox.Items.restrict("[SentOn] > '{} 12:00 AM'".format(startDate)) # startDate format DD/MM/YYYY
    with open('Daily/Unsub_Mail_{}.csv'.format(day), 'w') as fw:  # Open the file in which we will write today
        for msg in messages:
            if msg.Class==43:
                if msg.SenderEmailType=='EX':
                    print(msg.Sender.GetExchangeUser().PrimarySmtpAddress)
                    print('Type1')
                    print(msg.ReceivedTime)
                    unsub.append(msg.Sender.GetExchangeUser().PrimarySmtpAddress + ', Mails')  # Add the mail address to the list
                else:
                    print(msg.SenderEmailAddress)
                    print('Type2')
                    print(msg.ReceivedTime)
                    unsub.append(msg.SenderEmailAddress + ', Mails')  # Add the mail address to the list
                unsub = list(set(unsub))
        print(unsub)
        unsub = list(filter(None, unsub))
        unsublist = '\n'.join(str(e) for e in unsub) # Turn the list into str to write in the global csv
        fw.write(unsublist)  # Write in Unsub_Mail_{day}.csv

for mail in mail_list:
    get_mails(mail, folder_name,yesterday)
