#!/usr/bin/env python3

import csv,sys,os
import numpy as np

def read_csv(filename,delim):

	#Simple function for reading csv files and give out filtered output for given delimiter (delim)

	file_obj = open(filename,'rt',encoding = "utf8") #Creating file object
	file_csv = csv.reader(file_obj,delimiter = delim) #Reading the file object with csv module, delimiter assigned to ','
	data = [] #Creating empty array to append data

	#Appending data from csb object
	for row in file_csv:
		data.append(row)

	#Filtering data for None elements read.
	for j in range(0,len(data)):
		data[j] = list(filter(None,data[j]))
	data = list(filter(None,data))

	return data
	
args_input = sys.argv

try:

	self.T_path = args_input[1]

except IndexError:

	print('Not enough inputs are entered, five input files are needed...')
	print('Enter the full path of...')
	print('1. Thermal model in xyz format given in the descriptions.')
	
