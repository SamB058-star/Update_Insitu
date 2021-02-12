#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 00:35:33 2021

@author: sambit
"""

import pandas as pd
import os 
import glob
import numpy as np
import matplotlib.pyplot as plot

# read all the csv files from the directory and match the file format
csv_file_path = '/home/sambit/Desktop/Ground_data/Bani/2020_03_March'
os.chdir(csv_file_path)

colnames=['date', 'S1counts', 'S1SM', 'S1Perm', 'S1Temp', 'S1Volt',
       'S2counts', 'S2SM', 'S2Perm', 'S2Temp', 'S2Volt',
       'S3counts', 'S3SM', 'S3Perm', 'S3Temp', 'S3Volt',
       'S4counts', 'S4SM', 'S4Perm', 'S4Temp', 'S4Volt',
       'S5counts', 'S5SM', 'S5Perm', 'S5Temp', 'S5Volt',
       'S6counts', 'S6SM', 'S6Perm', 'S6Temp', 'S6Volt',
       'S7counts', 'S7SM', 'S7Perm', 'S7Temp', 'S7Volt',
       'S8counts', 'S8SM', 'S8Perm', 'S8Temp', 'S8Volt',
       'S9counts', 'S9SM', 'S9Perm', 'S9Temp', 'S9Volt',
       'S10counts', 'S10SM', 'S10Perm', 'S10Temp', 'S10Volt']
file_extension = ".csv"
list_of_files = [i for i in glob.glob(f"*{file_extension}")]



mydateparser = lambda x: pd.datetime.strptime(x, "%d.%m.%Y %H:%M:%S")

df = pd.concat([pd.read_csv(f, sep = ',', skiprows = 1, skipfooter = 2, date_parser = mydateparser, engine = 'python',
                 header = None, names = colnames, skip_blank_lines = True, error_bad_lines = False) 
      for f in list_of_files])


df['date'] = pd.to_datetime(df['date'], errors = 'coerce')
df = df.dropna(subset=['date'])

df.set_index('date', inplace = True)
df = df.sort_index()
df = df.dropna(thresh = 5)
print(df.shape)
df.to_csv('March_2020.csv', index = True)
