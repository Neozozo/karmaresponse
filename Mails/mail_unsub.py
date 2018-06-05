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

params = pd.read_json('params.json')  # read file
params = params['params'].to_dict() # read the 'params' bloc

mail_list = params['mail_list']
folder_name = params['folder_name']

# ===============================================================================
# Class & functions
# ===============================================================================

def get_mails(mail, folder_name,date):
    startDate = date.strftime('%d/%m/%Y')
    day = date.strftime('%Y%m%d')
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.Folders(mail).Folders(folder_name)
    unsub = ['\n']
    messages = inbox.Items.restrict("[SentOn] > '{} 12:00 AM'".format(startDate)) # startDate format DD/MM/YYYY
    os.chdir('./Mails')
    with open('./Daily/Unsub_Mails_{}.csv'.format(day), 'a') as fw:  # Open the file in which we will write today
        for msg in messages:
            if msg.Class==43:
                if msg.SenderEmailType=='EX':
                    unsub.append(msg.Sender.GetExchangeUser().PrimarySmtpAddress + ', Mails')  # Add the mail address to the list
                else:
                    unsub.append(msg.SenderEmailAddress + ', Mails')  # Add the mail address to the list
                unsub = list(set(unsub))
        unsublist = '\n'.join(str(e) for e in unsub) # Turn the list into str to write in the global csv
        fw.write(unsublist)  # Write in Unsub_Mail_{day}.csv
        os.chdir('..')
        return unsublist

def get_mail_unsubs(mails, folder_name, daily):
    Mailunsubs = '\n'
    for mail in mails:
        Mailunsubs += get_mails(mail, folder_name,daily)
        print(Mailunsubs)
    return Mailunsubs

if __name__ == "__main__":
    # code to be executed only if this file is called with 'python file.py <arguments>'
    pass
