#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Handle all the unsubscribers lists and merge them in order to be uploaded later on the API
"""

# ===============================================================================
# Metadata
# ===============================================================================

__authors__ = 'David Gosset'
__contact__ = 'davidgosset1994@gmail.com'
__copyright__ = ''
__license__ = ''
__date__ = 'Mon May 7 00:00:00 2018'

# ===============================================================================
# Import statements
# ===============================================================================

import numpy as np
import csv
import os
import time
import datetime as dt
from datetime import datetime
import logging

# Define log file and specifications
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, filename="logfile", filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")

np.seterr(divide='ignore', invalid='ignore')

day = str(int(datetime.now().strftime('%Y%m%d'))) # Date of the day in format 'YYYYMMDD'
hour = str(int(datetime.now().strftime('%H'))) + ':' + str(int(datetime.now().strftime('%M'))) # Hour in format 'HHMM'

list_dates = []
for k in range(0,7):
    kdate = dt.datetime.now() - dt.timedelta(days=k)
    kdate = kdate.strftime('%Y%m%d')
    list_dates.append(kdate)

# ===============================================================================
# Class & functions
# ===============================================================================


def get_unsub_files(date): # Get the list of all the .csv files that contains all the unsubscribers
    """
    :param
    :return: file_paths, list of path to access the unsub_files
    """
    DS_file_paths = []
    MB_file_paths = []
    CB_file_paths = []
    Mail_file_paths = []
    service_list = ['DrSender','Mindbaz','Mails','Cerberoos']
    for service in service_list: # Check at the same time inside of /DrSender ; /Mindbaz ; /Cerberoos
        if os.path.isdir(service):
            for DB_dir in os.listdir(service + '/csv/'): # Unsub files are all kept inside of csv/
                if os.path.isdir(service + '/csv/' + DB_dir):
                    for unsub_file in os.listdir(service + '/csv/' + DB_dir):
                        if str(unsub_file).endswith(date + '.csv'): # Takes only the csv files
                            if service == 'DrSender':
                                DS_file_paths.append(service + '/csv/' + DB_dir + '/' + unsub_file) # Add the file path in the list
                            if service == 'Mindbaz':
                                MB_file_paths.append(service + '/csv/' + DB_dir + '/' + unsub_file) # Add the file path in the list
                            if service == 'Mail':
                                Mail_file_paths.append(service + '/csv/' + DB_dir + '/' + unsub_file) # Add the file path in the list
                            if service == 'Cerberoos':
                                CB_file_paths.append(service + '/csv/' + DB_dir + '/' + unsub_file) # Add the file path in the list

    return DS_file_paths, MB_file_paths, CB_file_paths, Mail_file_paths

def merge_drsender(file_paths, day): # Get all the unsub_files and merge them into a single all_unsub_file for DrSender
    """
    :param file_paths, list of path to access the unsub_files of DrSender
    :param day, date of the wanted merging
    :return: unsublist, list of all the unsubscribers of this day
    """
    DS_unsubs = ''
    seen = []
    with open('DrSender/Daily/Unsub_DS_{}.csv'.format(day), 'w') as fw: # Open the file in which we will write today
        for path in file_paths:
            if path.startswith('DrSender'): # Make sure that we are using this function with DrSender's csvs
                with open(path, 'r') as fr: # Open the unsub_file
                    DBname = path.split('/')[-2] # Get the database name out from the filename
                    timestamp = day # Current timestamp, to be used later
                    all_info = fr.read() # Read the unsub_file
                    filtered_info = list(set(all_info.split(';'))) # Filter the informations and eliminate the double while making a list
                    unsub = [','] # Start with a comma in order to separate properly in excel
                    unsublist = ''
                    for char in filtered_info: # Each information of the list is checked in order to keep only the mail adress
                        if char.find('@')!=-1:
                            char = char + ',' + DBname + ',' + day # Separate the mail address and the database name with a comma
                            if char.split(',')[0] in seen:
                                pass
                            else:
                                seen.append(char.split(',')[0])
                                unsub.append(char) # Add the mail address to the list
                                unsublist = '\n'.join(str(e) for e in unsub) # Turn the list into str to write in the global csv
                    fw.write(unsublist) # Write in Unsub_DS_{day}.csv
                    DS_unsubs += unsublist
        fw.close()
        return DS_unsubs

def merge_mindbaz(file_paths, day): # Get all the unsub_files and merge them into a single all_unsub_file for Mindbaz
    """
    :param file_paths, list of path to access the unsub_files of Mindbaz
    :param day, date of the wanted merging
    :return: unsublist, list of all the unsubscribers of this day
    """
    MB_unsubs = ''
    seen = []
    with open('Mindbaz/Daily/Unsub_MB_{}.csv'.format(day), 'w') as fw:  # Open the file in which we will write today
        for path in file_paths:
            if path.startswith('Mindbaz'):
                with open(path, 'r') as fr: # Open the unsub_file
                    DBname = 'karmaresponse_' + path.split('/')[-2] # Get the database name out from the filename
                    all_info = fr.read() # Read the unsub_file
                    filtered_info = list(set(all_info.split('\n'))) # Filter the informations and eliminate the double while making a list
                    unsub = [','] # Start with a comma in order to separate properly in excel
                    unsublist = ''
                    for char in filtered_info: # Each information of the list is checked in order to keep only the mail adress
                        if char.find('@')!=-1:
                            char = char.split(';')[0] + ',' + DBname + ',' + day # Separate the mail address and the database name with a comma
                            if char.split(',')[0] in seen:
                                pass
                            else:
                                seen.append(char.split(',')[0])
                                unsub.append(char) # Add the mail address to the list
                                unsublist = '\n'.join(str(e) for e in unsub) # Turn the list into str to write in the global csv
                    fw.write(unsublist) # Write in Unsub_MB_{day}.csv
                    MB_unsubs += unsublist
        fw.close()
        return MB_unsubs


def merge_cerberoos(file_paths, day): # Get all the unsub_files and merge them into a single all_unsub_file for Cerberoos
    """
    :param file_paths, list of path to access the unsub_files of Cerberoos
    :param day, date of the wanted merging
    :return: unsublist, list of all the unsubscribers of this day
    """
    CB_unsubs = ''
    seen = []
    path_to_test = 'Cerberoos/csv/Tutorum/unsubs_{}.csv'
    if os.path.exists(path_to_test):
        with open('Cerberoos/Weekly/Unsub_CB_{}.csv'.format(day), 'w') as fw:  # Open the file in which we will write today
            for path in file_paths:
                if path.startswith('Cerberoos'):
                    with open(path, 'r') as fr: # Open the unsub_file
                        DBname = path.split('/')[-2] # Get the database name out from the filename
                        all_info = fr.read() # Read the unsub_file
                        filtered_info = list(set(all_info.split('\n'))) # Filter the informations and eliminate the double while making a list
                        unsub = [','] # Start with a comma in order to separate properly in excel
                        unsublist = ''
                        for char in filtered_info: # Each information of the list is checked in order to keep only the mail adress
                            if char.find('@')!=-1:
                                char = char.split(';')[0] + ',' + DBname + ',' + day # Separate the mail address and the database name with a comma
                                if char.split(',')[0] in seen:
                                    pass
                                else:
                                    seen.append(char.split(',')[0])
                                    unsub.append(char) # Add the mail address to the list
                                    unsublist = '\n'.join(str(e) for e in unsub) # Turn the list into str to write in the global csv
                        fw.write(unsublist) # Write in Unsub_MB_{day}.csv
                        CB_unsubs += unsublist
            fw.close()
            return CB_unsubs
    else:
        return ''


def merge_all_daily(day,DSunsubs,MBunsubs,Mailunsubs,CBunsubs):
    """
    :param day, date of the wanted merging
    :param DSunsubs, list of unsubscribers of <day> on DrSender
    :param MBunsubs, list of unsubscribers of <day> on Mindbaz
    :param Mailunsubs, list of unsubscribers of <day> by Mails
    :param CBunsubs, list of unsubscribers of <day> on Cerberoos
    :return:
    """
    with open('MergedFiles/Daily/ALL_Daily_Unsubs_{}.csv'.format(day), 'w') as fw:
        ALL_unsubs = DSunsubs + MBunsubs + Mailunsubs + CBunsubs
        fw.write(ALL_unsubs)
        fw.close()

def merge_all_weekly(day):
    """
    :param day, date of the wanted merging
    :return:
    """
    path_to_test = 'Cerberoos/csv/Tutorum/unsubs_{}.csv'.format(day)
    list_dates = []
    DSunsubs = ''
    MBunsubs = ''
    ALL_unsubs = ''
    seen = []
    for k in range(0,7):
        kdate = dt.datetime.now() - dt.timedelta(days=k)
        kdate = kdate.strftime('%Y%m%d')
        list_dates.append(kdate)
    if os.path.exists(path_to_test):
        list_of_files = get_list_files_to_merge(list_dates)
        with open('MergedFiles/Weekly/ALL_Weekly_Unsubs_{}.csv'.format(day), 'w') as fw:  # Open the file in which we will write today
            for filepath in list_of_files:
                with open(filepath, 'r') as fr: # Open the unsub_file
                    print('Adding ' + filepath)
                    all_info = fr.read() # Read the unsub_file
                    filtered_info = list(set(all_info.split('\n'))) # Filter the informations and eliminate the double while making a list
                    unsub = [','] # Start with a comma in order to separate properly in excel
                    unsublist = ''
                    for char in filtered_info: # Each information of the list is checked in order to keep only the mail adress
                        if not char.split(',')[0] in seen:
                            seen.append(char.split(',')[0])
                            unsub.append(char) # Add the mail address to the list
                            unsublist = '\n'.join(str(e) for e in unsub) # Turn the list into str to write in the global csv
                    fw.write(unsublist) # Write in Unsub_MB_{day}.csv
                fr.close()
        fw.close()
        #with open('MergedFiles/Weekly/ALL_Weekly_Unsubs_{}.csv'.format(day), 'w') as fw:
            #ALL_unsubs = DSunsubs + MBunsubs
            #fw.write(ALL_unsubs)
            #fw.close()

def get_list_files_to_merge(list_dates):
    MBlist = []
    DSlist = []
    Maillist = []
    for date in list_dates:
        MBfile = 'Mindbaz/Daily/Unsub_MB_{}.csv'.format(date)
        if os.path.isfile(MBfile):
            MBlist.append('Mindbaz/Daily/Unsub_MB_{}.csv'.format(date))
        Mailfile = 'Mails/Daily/Unsub_Mail_{}.csv'.format(date)
        if os.path.isfile(Mailfile):
            Maillist.append('Mails/Daily/Unsub_Mail_{}.csv'.format(date))
        DSfile = 'DrSender/Daily/Unsub_DS_{}.csv'.format(date)
        if os.path.isfile(DSfile):
            DSlist.append('DrSender/Daily/Unsub_DS_{}.csv'.format(date))
    list_files_to_merge = MBlist + Maillist + DSlist
    return list_files_to_merge



for current_date in list_dates:
    DS,MB,CB,Mails = get_unsub_files(current_date)
    DSunsubs = merge_drsender(DS, current_date)
    MBunsubs = merge_mindbaz(MB, current_date)
    CBunsubs = merge_cerberoos(CB, current_date)
    merge_all_daily(current_date,DSunsubs,MBunsubs,'',CBunsubs)
merge_all_weekly(day)
