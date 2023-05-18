#!/usr/bin/env python3

import os,sys,csv,warnings,itertools
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, griddata
from mtpy.utils import gis_tools as gis_tools

class check_T_model(object):

	def __init__(self):

		args_input = sys.argv

		try:

			self.T_path = args_input[1]
			self.dat_path = args_input[2]

		except IndexError:

			print('Not enough inputs are entered, five input files are needed...')
			print('Enter the full path of...')
			print('1. Thermal model in xyz format given in the descriptions.')
			print('2. MT Data File (e.g. ModEM dat)')
			sys.exit()

		self.depth = np.arange(0,250000,5000)

		self.read_ModEM_dat()
		self.get_T()

		print('What is the depth you want to plot (in kms)?')
		try:
			self.depth_input = float(input()) * 1e3
			self.plot_temp()
		except ValueError:
			print('Have to enter a value that can be turn into floating number.')

	def read_csv(self,filename,delim):

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

	def read_ModEM_dat(self):

		#Reading ModEM dat file to get coordinates of stations and model centre.

		self.ModEM_dat_data = self.read_csv(filename = self.dat_path ,delim = ' ')

		self.station_lat = []
		self.station_lon = []
		self.station_name = []
		self.station_posx = []
		self.station_posy = []

		self.mc_lat = float(self.ModEM_dat_data[6][1])
		self.mc_lon = float(self.ModEM_dat_data[6][2])

		dash_found = False

		for row in range(8,len(self.ModEM_dat_data)):
			if self.ModEM_dat_data[row][0] == '#' :
				limitlines = row-1
				dash_found = True

		if dash_found == False:
			limitlines = len(self.ModEM_dat_data)

		for row in range(8,limitlines):
			if self.ModEM_dat_data[row][1] != self.ModEM_dat_data[row-1][1]:
				self.station_name.append(self.ModEM_dat_data[row][1])
				self.station_lat.append(float(self.ModEM_dat_data[row][2]))
				self.station_lon.append(float(self.ModEM_dat_data[row][3]))
				self.station_posx.append(float(self.ModEM_dat_data[row][4]))
				self.station_posy.append(float(self.ModEM_dat_data[row][5]))


		self.ModEM_dat_read = True
		self.res_profile_plot_list = []
		self.res_profile_max_plot_list = []
		self.res_profile_min_plot_list = []

		self.st_item_list = []

		for i in range(0,len(self.station_name)):

			self.st_item_list.append(str(i) + ' - ' + self.station_name[i])

		self.distance_from_x = 20
		self.distance_from_y = 20
		self.max_x = max(self.station_posx) + (self.distance_from_x * 1000.0)
		self.min_x = min(self.station_posx) - (self.distance_from_x * 1000.0)
		self.max_y = max(self.station_posy) + (self.distance_from_y * 1000.0)
		self.min_y = min(self.station_posy) - (self.distance_from_y * 1000.0)

	def get_T(self):

		temp_data = self.read_csv(filename = self.T_path, delim = ' ')

		self.temp = []
		self.lat = []
		self.lon = []
		self.depth_ext = []
		dep = [0.0]
		tempa = [0.0]

		for i in range(0,len(temp_data[0])):
			print(temp_data[0])
			if temp_data[0][i] == 'Latitude':
				index_lat = i
			elif temp_data[0][i] == 'Longitude':
				index_lon = i
			elif temp_data[0][i] == 'Temperature':
				index_temp = i
			elif temp_data[0][i] == 'id':
				index_id = i
			elif temp_data[0][i] == 'Depth':
				index_depth = i

		print(index_depth,index_id,index_temp,index_lon,index_lat)
		try:
			index_what = index_lat + index_lon + index_temp + index_id + index_depth
		except NameError:
			print('Header info on temperature file cannot be read, be sure the individual header parameters are named in the exact same form:')
			print('id,Latitude,Longitude,Depth,Temperature')
			sys.exit()

		for i in range(2,len(temp_data)):

			if float(temp_data[i][index_depth]) != 0.0:

				dep.append(-1.0 * float(temp_data[i][index_depth]) * 1e3)
				tempa.append(float(temp_data[i][index_temp])+273.0)

			if temp_data[i][index_id] != temp_data[i-1][index_id]:
				self.lat.append(float(temp_data[i-1][index_lat]))
				if float(temp_data[i-1][1]) < 180.0:
					self.lon.append(float(temp_data[i-1][index_lon]))
				else:
					self.lon.append(float(temp_data[i-1][index_lon]) - 360.0)
				self.depth_ext.append(dep)
				self.temp.append(tempa)
				dep = [0.0]
				tempa = [0.0]

		self.lat = np.array(self.lat)
		self.lon = np.array(self.lon)

		with warnings.catch_warnings():
			warnings.simplefilter('ignore', FutureWarning)
			utm_no = gis_tools.get_epsg(self.mc_lat,self.mc_lon)
			stuff= gis_tools.project_point_ll2utm(self.lat, self.lon, utm_zone = 34, epsg = utm_no)
		self.x_mtpy = np.zeros(len(stuff))
		self.y_mtpy = np.zeros(len(stuff))
		utm_z = []

		for i in range(0,len(stuff)):
			self.x_mtpy[i] = stuff[i][0]
			self.y_mtpy[i] = stuff[i][1]
			utm_z.append(stuff[i][3])

		with warnings.catch_warnings():
			warnings.simplefilter('ignore', FutureWarning)
			x_mtpy_center, y_mtpy_center, utm_center = gis_tools.project_point_ll2utm(self.mc_lat, self.mc_lon, utm_zone = 14, epsg = utm_no)

		self.x_rel = self.x_mtpy - x_mtpy_center
		self.y_rel = self.y_mtpy - y_mtpy_center
		
		for i in range(0,len(self.x_rel)):
			f_sond = interp1d(self.depth_ext[i],self.temp[i])
			self.temp[i] = f_sond(self.depth)
			self.depth_ext[i] = self.depth

		self.depth_ext = np.array(self.depth_ext)
		self.temp = np.array(self.temp)

		self.xnew = np.arange(np.amin(self.x_rel), np.amax(self.x_rel), 1e4)
		self.ynew = np.arange(np.amin(self.y_rel), np.amax(self.y_rel), 1e4)

		self.x_new, self.y_new = np.meshgrid(self.xnew, self.ynew)

		points_interp = np.column_stack((self.x_rel, self.y_rel))

		self.temp_interp = []

		for i in range(0,len(self.depth)):

			interp_array = np.array(self.temp[:,i])
			fnew = griddata(points_interp, interp_array, (self.x_new, self.y_new), method = 'cubic')
			fnew[np.isnan(fnew)] = 273.0
			fnew = np.asarray(list(itertools.chain(*fnew)))
			self.temp_interp.append(fnew)

		self.x_new = np.asarray(list(itertools.chain(*self.x_new)))
		self.y_new = np.asarray(list(itertools.chain(*self.y_new)))

		self.temp_interp = np.array(self.temp_interp)

		self.temp_rev = []

		for i in range(0,len(self.x_new)):

			self.temp_rev.append(self.temp_interp[:,i])

		self.temp_rev = np.array(self.temp_rev)

	def plot_temp(self):

		idx_depth_plot = (np.abs(self.depth-self.depth_input)).argmin()
		print(idx_depth_plot)
		print(self.depth[idx_depth_plot])
		print('THIS')
		self.color_map_temp = 'magma'
		fig = plt.figure()
		ax1 = plt.subplot(111)
		# cax = ax1.imshow(fnew, cmap = self.color_map_water, origin = 'lower')
		# ax1.plot(points_interp[:,0], points_interp[:,1], 'o', color = 'k')
		cax = ax1.scatter(self.x_new, self.y_new, c = self.temp_interp[idx_depth_plot], cmap = self.color_map_temp, marker = 's', linewidth = 0.01, edgecolor = 'k')
		cax.set_clim(750,2000)
		ax1.axhline(self.min_x,linestyle = '--')
		ax1.axhline(self.max_x,linestyle = '--')
		ax1.axvline(self.min_y,linestyle ='--')
		ax1.axvline(self.max_y,linestyle ='--')

		ax1.plot(self.station_posy,self.station_posx,'^',color = 'k',markersize = 3)

		ax1.scatter(self.x_rel,self.y_rel, c = self.temp[:,idx_depth_plot], cmap = self.color_map_temp, marker = 'o', s = 9)
		cbar_xx = fig.colorbar(cax,boundaries=np.linspace(750,2000),orientation="vertical", pad=0.05,
		 ticks = [750,2750.0/2,2000], ax = ax1)
		plt.show()

RUN = check_T_model()
