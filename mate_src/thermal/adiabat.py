#!/usr/bin/env python3

import numpy as np

def Katsura2022(P_input):

	'''
	A function that calculates the mantle adiabat temperature for given pressure
	range. Taken from Katsura (2022).

	###Parameters###
	P_input: Pressure in GPa

	'''

	Depth = [50,70,90,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,
	400,410,410,420,440,460,480,500]
	P = [1.5,2.1,2.8,3.1,3.8,4.4,5.1,5.8,6.4,7.1,7.8,8.5,9.2,9.9,10.6,11.2,
	11.9,12.6,13.4,13.7,13.7,14.1,14.9,15.6,16.4,17.1]
	T = [1646,1657,1667,1672,1682,1691,1700,1709,1718,1726,1735,1743,1751,
	1759,1766,1774,1781,1788,1796,1799,1860,1863,1871,1878,1885,1892]

	Depth = np.array(Depth)
	T_C = np.array(T) - 273.15

	T_C_out = np.interp(P_input ,P ,T_C)
	T_K_out = T_C_out + 273.15

	return T_K_out, Depth, T
