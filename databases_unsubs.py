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
from datetime import datetime
import logging

# Define log file and specifications
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, filename="logfile", filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")

np.seterr(divide='ignore', invalid='ignore')

day = str(int(datetime.now().strftime('%Y%m%d'))) # Date of the day in format 'YYYYMMDD'
hour = str(int(datetime.now().strftime('%H'))) + ':' + str(int(datetime.now().strftime('%M'))) # Hour in format 'HHMM'

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
    for service in os.listdir('./'): # Check at the same time inside of /DrSender ; /Mindbaz ; /Cerberoos
        if os.path.isdir(service):
            for DB_dir in os.listdir(service + '/csv/'): # Unsub files are all kept inside of csv/
                if os.path.isdir(service + '/csv/' + DB_dir):
                    for unsub_file in os.listdir(service + '/csv/' + DB_dir):
                        if str(unsub_file).endswith(date + '.csv'): # Takes only the csv files
                            print(service + '/csv/' + DB_dir + '/' + unsub_file)
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
    :return:
    """
    countat=0 # A Simple counter
    with open('DrSender/Daily/Unsub_DS_{}.csv'.format(day), 'w') as fw: # Open the file in which we will write today
        for path in file_paths:
            if path.startswith('DrSender'): # Make sure that we are using this function with DrSender's csvs
                with open(path, 'r') as fr: # Open the unsub_file
                    DBname = path.split('/')[-2] # Get the database name out from the filename
                    print(DBname)
                    timestamp = day # Current timestamp, to be used later
                    all_info = fr.read() # Read the unsub_file
                    filtered_info = list(set(all_info.split(';'))) # Filter the informations and eliminate the double while making a list
                    unsub = [','] # Start with a comma in order to separate properly in excel
                    unsublist = ''
                    for char in filtered_info: # Each information of the list is checked in order to keep only the mail adress
                        if char.find('@')!=-1:
                            char = char + ',' + DBname # Separate the mail address and the database name with a comma
                            countat+=1 # Increase the counter
                            unsub.append(char) # Add the mail address to the list
                            unsublist = '\n'.join(str(e) for e in unsub) # Turn the list into str to write in the global csv
                    fw.write(unsublist) # Write in Unsub_DS_{day}.csv

def merge_mindbaz(file_paths, day): # Get all the unsub_files and merge them into a single all_unsub_file for Mindbaz
    """
    :param file_paths, list of path to access the unsub_files of Mindbaz
    :return:
    """
    with open('Mindbaz/Daily/Unsub_MB_{}.csv'.format(day), 'w') as fw:  # Open the file in which we will write today
        for path in file_paths:
            if path.startswith('Mindbaz'):
                with open(path, 'r') as fr: # Open the unsub_file
                    DBname = 'karmaresponse_' + path.split('/')[-2] # Get the database name out from the filename
                    print(DBname)
                    all_info = fr.read() # Read the unsub_file
                    filtered_info = list(set(all_info.split('\n'))) # Filter the informations and eliminate the double while making a list
                    unsub = [','] # Start with a comma in order to separate properly in excel
                    unsublist = ''
                    for char in filtered_info: # Each information of the list is checked in order to keep only the mail adress
                        if char.find('@')!=-1:
                            char = char.split(';')[0] + ',' + DBname # Separate the mail address and the database name with a comma
                            unsub.append(char) # Add the mail address to the list
                            unsublist = '\n'.join(str(e) for e in unsub) # Turn the list into str to write in the global csv
                    fw.write(unsublist) # Write in Unsub_MB_{day}.csv


def merge_cerberoos(file_paths): # Get all the unsub_files and merge them into a single all_unsub_file for Cerberoos
    """
    :param file_paths, list of path to access the unsub_files of Cerberoos
    :return:
    """
    for path in file_paths:
        if path.startswith('Cerberoos'):
            print(path)

DS,MB,CB,Mails = get_unsub_files(day)
merge_drsender(DS, day)
merge_mindbaz(MB, day)
