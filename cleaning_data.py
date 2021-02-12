#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 01:22:57 2021

@author: sambit
"""

import pandas as pd
import os 
import glob
import numpy as np
import matplotlib.pyplot as plot

df = pd.read_csv('Bani_full_Jan.csv', delimiter = ',', index_col='date')
df = df.sort_index(axis = 0)
df = df.drop_duplicates(inplace = False)
print(df.head())
#plot.plot(df.index, df.S1SM)
#plot.show()

'''
#Sensor-1 Filtering
S1SM_outer = df[df['S1SM'] > 100]
S1Perm_outer = df[df['S1Perm'] > 100]
S1Temp_outer = df[df['S1Temp'] > 100]
S1Volt_outer = df[df['S1Volt'] > 100]

#Sensor-2 Filtering
S2SM_outer = df[df['S2SM'] > 100]
S2Perm_outer = df[df['S2Perm'] > 100]
S2Temp_outer = df[df['S2Temp'] > 100]
S2Volt_outer = df[df['S2Volt'] > 100]

#Sensor-3 Filtering
S3SM_outer = df[df['S3SM'] > 100]
S3Perm_outer = df[df['S3Perm'] > 100]
S3Temp_outer = df[df['S3Temp'] > 100]
S3Volt_outer = df[df['S3Volt'] > 100]

#Sensor-4 Filtering
S4SM_outer = df[df['S4SM'] > 100]
S4Perm_outer = df[df['S4Perm'] > 100]
S4Temp_outer = df[df['S4Temp'] > 100]
S4Volt_outer = df[df['S4Volt'] > 100]

#Sensor-5 Filtering
S5SM_outer = df[df['S5SM'] > 100]
S5Perm_outer = df[df['S5Perm'] > 100]
S5Temp_outer = df[df['S5Temp'] > 100]
S5Volt_outer = df[df['S5Volt'] > 100]

#Sensor-6 Filtering
S6SM_outer = df[df['S6SM'] > 100]
S6Perm_outer = df[df['S6Perm'] > 100]
S6Temp_outer = df[df['S6Temp'] > 100]
S6Volt_outer = df[df['S6Volt'] > 100]

#Sensor-7 Filtering
S7SM_outer = df[df['S7SM'] > 100]
S7Perm_outer = df[df['S7Perm'] > 100]
S7Temp_outer = df[df['S7Temp'] > 100]
S7Volt_outer = df[df['S7Volt'] > 100]

#Sensor-8 Filtering
S8SM_outer = df[df['S8SM'] > 100]
S8Perm_outer = df[df['S8Perm'] > 100]
S8Temp_outer = df[df['S8Temp'] > 100]
S8Volt_outer = df[df['S8Volt'] > 100]

#Sensor-9 Filtering
S9SM_outer = df[df['S9SM'] > 100]
S9Perm_outer = df[df['S9Perm'] > 100]
S9Temp_outer = df[df['S9Temp'] > 100]
S9Volt_outer = df[df['S9Volt'] > 100]

#Sensor-10 Filtering
S10SM_outer = df[df['S10SM'] > 100]
S10Perm_outer = df[df['S10Perm'] > 100]
S10Temp_outer = df[df['S10Temp'] > 100]
S10Volt_outer = df[df['S10Volt'] > 100]

#Printing the shape of the Outer for every columns
print('######Shape of the outliers for different sensors######')
print('Sensor-1:')
print("Sensor-1(SM) :",S1SM_outer.shape)
print("Sensor-1(Perm) :", S1Perm_outer.shape)
print("Sensor-1(Temp) :", S1Temp_outer.shape)
print("Sensor-1(Volt) :", S1Volt_outer.shape)
print('\n')

#2nd
print('Sensor-2:')
print("Sensor-2(SM) :",S2SM_outer.shape)
print("Sensor-2(Perm) :", S2Perm_outer.shape)
print("Sensor-2(Temp) :", S2Temp_outer.shape)
print("Sensor-2(Volt) :", S2Volt_outer.shape)
print('\n')

#3rd
print('Sensor-3:')
print("Sensor-3(SM) :",S3SM_outer.shape)
print("Sensor-3(Perm) :", S3Perm_outer.shape)
print("Sensor-3(Temp) :", S3Temp_outer.shape)
print("Sensor-3(Volt) :", S3Volt_outer.shape)
print('\n')

#4th
print('Sensor-4:')
print("Sensor-4(SM) :",S4SM_outer.shape)
print("Sensor-4(Perm) :", S4Perm_outer.shape)
print("Sensor-4(Temp) :", S4Temp_outer.shape)
print("Sensor-4(Volt) :", S4Volt_outer.shape)
print('\n')

#5th
print('Sensor-5:')
print("Sensor-5(SM) :",S5SM_outer.shape)
print("Sensor-5(Perm) :", S5Perm_outer.shape)
print("Sensor-5(Temp) :", S5Temp_outer.shape)
print("Sensor-5(Volt) :", S5Volt_outer.shape)
print('\n')

#6th
print('Sensor-6:')
print("Sensor-6(SM) :",S6SM_outer.shape)
print("Sensor-6(Perm) :", S6Perm_outer.shape)
print("Sensor-6(Temp) :", S6Temp_outer.shape)
print("Sensor-6(Volt) :", S6Volt_outer.shape)
print('\n')

#7th
print('Sensor-7:')
print("Sensor-7(SM) :",S7SM_outer.shape)
print("Sensor-7(Perm) :", S7Perm_outer.shape)
print("Sensor-7(Temp) :", S7Temp_outer.shape)
print("Sensor-7(Volt) :", S7Volt_outer.shape)
print('\n')

#8th
print('Sensor-8:')
print("Sensor-8(SM) :",S8SM_outer.shape)
print("Sensor-8(Perm) :", S8Perm_outer.shape)
print("Sensor-8(Temp) :", S8Temp_outer.shape)
print("Sensor-8(Volt) :", S8Volt_outer.shape)
print('\n')

#9th
print('Sensor-9:')
print("Sensor-9(SM) :",S9SM_outer.shape)
print("Sensor-9(Perm) :", S9Perm_outer.shape)
print("Sensor-9(Temp) :", S9Temp_outer.shape)
print("Sensor-9(Volt) :", S9Volt_outer.shape)
print('\n')

#10th
print('Sensor-10:')
print("Sensor-10(SM) :",S10SM_outer.shape)
print("Sensor-10(Perm) :", S10Perm_outer.shape)
print("Sensor-10(Temp) :", S10Temp_outer.shape)
print("Sensor-10(Volt) :", S10Volt_outer.shape)
print('\n')
print('##### Done ! ! ! #####')
'''
ind_todrop = df[(df['S1SM'] >100) | (df['S1Perm'] >100) | (df['S1Temp'] >100) |
                (df['S1Volt'] >100) | (df['S2SM'] >100) | (df['S2Perm'] >100) | (df['S2Temp'] >100)|
                (df['S2Volt'] >100) | (df['S2SM'] >100) | (df['S3Perm'] >100) | (df['S3Temp'] >100)|
                (df['S3Volt'] >100) | (df['S4SM'] >100) | (df['S4Perm'] >100) | (df['S4Temp'] >100)|
                (df['S4Volt'] >100) | (df['S5SM'] >100) | (df['S5Perm'] >100) | (df['S5Temp'] >100)|
                (df['S5Volt'] >100) | (df['S6SM'] >100) | (df['S6Perm'] >100) | (df['S6Temp'] >100)|
                (df['S6Volt'] >100) | (df['S7SM'] >100) | (df['S7Perm'] >100) | (df['S7Temp'] >100)|
                (df['S7Volt'] >100) | (df['S8SM'] >100) | (df['S8Perm'] >100) | (df['S8Temp'] >100)|
                (df['S8Volt'] >100) | (df['S9SM'] >100) | (df['S9Perm'] >100) | (df['S9Temp'] >100)|
                (df['S9Volt'] >100) | (df['S10SM'] >100) | (df['S10Perm'] >100) | (df['S10Temp'] >100)|
                (df['S10Volt'] >100)].index
#ind_todrop.shape.index
print(ind_todrop.shape)

filtered_df = df.drop(ind_todrop, axis = 0, inplace = False)  #Master_df
#print(filtered_df.shape)

#df_1hr = filtered_df.resample('60T').mean()
'''
plot.figure(figsize = (25,5))
plot.plot(filtered_df.index, filtered_df.S1SM)
plot.xticks(rotation = 45);
plot.show()
'''
#Sensor-1 Filtering
S1SM_shift = df[df['S1SM'] > 100].shift(-1, axis = 1)
S1Perm_shift = df[df['S1Perm'] > 100].shift(-2, axis = 1)
S1Temp_shift = df[df['S1Temp'] > 100].shift(-3, axis = 1)
S1Volt_shift = df[df['S1Volt'] > 100].shift(-4, axis = 1)

#Sensor-2 Filtering
S2SM_shift = df[df['S2SM'] > 100].shift(-1, axis = 1)
S2Perm_shift = df[df['S2Perm'] > 100].shift(-2, axis = 1)
S2Temp_shift = df[df['S2Temp'] > 100].shift(-3, axis = 1)
S2Volt_shift = df[df['S2Volt'] > 100].shift(-4, axis = 1)

#Sensor-3 Filtering
S3SM_shift = df[df['S3SM'] > 100].shift(-1, axis = 1)
S3Perm_shift = df[df['S3Perm'] > 100].shift(-2, axis = 1)
S3Temp_shift = df[df['S3Temp'] > 100].shift(-3, axis = 1)
S3Volt_shift = df[df['S3Volt'] > 100].shift(-4, axis = 1)

#Sensor-4 Filtering
S4SM_shift = df[df['S4SM'] > 100].shift(-1, axis = 1)
S4Perm_shift = df[df['S4Perm'] > 100].shift(-2, axis = 1)
S4Temp_shift = df[df['S4Temp'] > 100].shift(-3, axis = 1)
S4Volt_shift = df[df['S4Volt'] > 100].shift(-4, axis = 1)

#Sensor-5 Filtering
S5SM_shift = df[df['S5SM'] > 100].shift(-1, axis = 1)
S5Perm_shift = df[df['S5Perm'] > 100].shift(-2, axis = 1)
S5Temp_shift = df[df['S5Temp'] > 100].shift(-3, axis = 1)
S5Volt_shift = df[df['S5Volt'] > 100].shift(-4, axis = 1)

#Sensor-6 Filtering
S6SM_shift = df[df['S6SM'] > 100].shift(-1, axis = 1)
S6Perm_shift = df[df['S6Perm'] > 100].shift(-2, axis = 1)
S6Temp_shift = df[df['S6Temp'] > 100].shift(-3, axis = 1)
S6Volt_shift = df[df['S6Volt'] > 100].shift(-4, axis = 1)

#Sensor-7 Filtering
S7SM_shift = df[df['S7SM'] > 100].shift(-1, axis = 1)
S7Perm_shift = df[df['S7Perm'] > 100].shift(-2, axis = 1)
S7Temp_shift = df[df['S7Temp'] > 100].shift(-3, axis = 1)
S7Volt_shift = df[df['S7Volt'] > 100].shift(-4, axis = 1)

#Sensor-8 Filtering
S8SM_shift = df[df['S8SM'] > 100].shift(-1, axis = 1)
S8Perm_shift = df[df['S8Perm'] > 100].shift(-2, axis = 1)
S8Temp_shift = df[df['S8Temp'] > 100].shift(-3, axis = 1)
S8Volt_shift = df[df['S8Volt'] > 100].shift(-4, axis = 1)

#Sensor-9 Filtering
S9SM_shift = df[df['S9SM'] > 100].shift(-1, axis = 1)
S9Perm_shift = df[df['S9Perm'] > 100].shift(-2, axis = 1)
S9Temp_shift = df[df['S9Temp'] > 100].shift(-3, axis = 1)
S9Volt_shift = df[df['S9Volt'] > 100].shift(-4, axis = 1)

#Sensor-10 Filtering
S10SM_shift = df[df['S10SM'] > 100].shift(-1, axis = 1)
S10Perm_shift = df[df['S10Perm'] > 100].shift(-2, axis = 1)
S10Temp_shift = df[df['S10Temp'] > 100].shift(-3, axis = 1)
S10Volt_shift = df[df['S10Volt'] > 100].shift(-4, axis = 1)

shifted_outer = pd.concat([S1SM_shift, S1Perm_shift, S1Perm_shift, S1Temp_shift, S1Volt_shift,
                                   S2SM_shift, S2Perm_shift, S2Temp_shift, S2Volt_shift, S3SM_shift,
                                   S3Perm_shift, S3Temp_shift, S3Volt_shift, S4SM_shift, S4Perm_shift,
                                   S4Temp_shift, S4Volt_shift, S5SM_shift, S5Perm_shift, S5Temp_shift, S5Volt_shift,
                                   S6SM_shift, S5Perm_shift, S5Temp_shift, S5Volt_shift, 
                                   S7SM_shift, S7Perm_shift, S7Temp_shift, S7Volt_shift,
                                   S8SM_shift, S8Perm_shift, S8Temp_shift, S8Volt_shift,
                                   S9SM_shift, S9Perm_shift, S9Temp_shift, S9Volt_shift,
                                   S10SM_shift, S10Perm_shift, S10Temp_shift, S10Volt_shift])
print(shifted_outer.drop_duplicates(inplace = False).shape)

cleaned_df = pd.concat([filtered_df, shifted_outer])
cleaned_df = cleaned_df.drop_duplicates()
cleaned_df = cleaned_df.sort_index(axis = 0)
cleaned_df = cleaned_df.reset_index()
#print(cleaned_df.head())
#df_1hr = cleaned_df.resample('60T').mean()
#plot.figure(figsize = (25,5))
#plot.plot(df_1hr.index, df_1hr.S1SM)
#plot.xticks(rotation = 45);
#plot.show()
###

cleaned_df['date'] = pd.to_datetime(cleaned_df['date'])
cleaned_df = cleaned_df.sort_values(by="date")
#cleaned_df = cleaned_df.set_index('date')
cleaned_df.to_csv('cleaned_data.csv', index = True)
#print(cleaned_df)

df_1hr = cleaned_df.resample('60T').mean()
#print(df_1hr)
'''
plot.figure(figsize = (25,5))
plot.plot(df_1hr.index, df_1hr.S1SM)
plot.xticks(rotation = 45);
plot.show()
'''