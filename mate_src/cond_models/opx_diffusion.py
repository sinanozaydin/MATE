#!/usr/bin/env python3

import numpy as np

R_const = 8.3144621

def Stalder2006(T,opx_h2o,method):

	A_H = [7.9 * 1e-3,1.7*1e-4,7.3*1e-5]
	EH = [211000.0,185000.0,158000.0]
	EH_err = [31000.0,28000.0,102000.0]

	if method == 'array':
		T = T[0]
		DH_0 = np.zeros((3,len(T)))
		DH_1 = np.zeros((3,len(T)))
		DH_2 = np.zeros((3,len(T)))
	elif method == 'index':
		T = T
		DH_0 = np.zeros((3,1))
		DH_0_max = np.zeros((3,1))
		DH_0_min = np.zeros((3,1))


	for i in range(0,3):
		DH_0[i] = 10**(A_H[i]) * np.exp(-EH[i] / (R_const * T))
		if method == 'array':
			DH_1[i] = 10**(A_H[i]) * np.exp(-(EH[i]-EH_err[i]) / (R_const * T))
			DH_2[i] = 10**(A_H[i]) * np.exp(-(EH[i]+EH_err[i]) / (R_const * T))

	DH = (DH_0[0] * DH_0[1] * DH_0[2])**(1.0/3.0)
	if method == 'array':
		DH_max = (DH_1[0] * DH_1[1] * DH_1[2])**(1.0/3.0)
		DH_min = (DH_2[0] * DH_2[1] * DH_2[2])**(1.0/3.0)
	else:
		DH_max = DH
		DH_min = DH

	return DH_max,DH_min,DH
