#!/usr/bin/env python3

import numpy as np
R_const = 8.3144621

def Novella2017(T,ol_h2o):

	A_H = [-0.7,-5,-3.5]

	A_H_err = [0.9,0.9,0.4]

	EH = [229000.0,172000.0,188000.0]

	EH_err = [18000.0,19000.0,8000.0]

	DH_0 = np.zeros((3,len(T[0])))
	DH_1 = np.zeros((3,len(T[0])))
	DH_2 = np.zeros((3,len(T[0])))

	for i in range(0,3):

		DH_0[i] = 10**(A_H[i]) * np.exp(-EH[i] / (R_const * T[0]))
		DH_1[i] = 10**(A_H[i] + A_H_err[i]) * np.exp(-(EH[i]-EH_err[i]) / (R_const * T[0]))
		DH_2[i] = 10**(A_H[i] - A_H_err[i]) * np.exp(-(EH[i]+EH_err[i]) / (R_const * T[0]))

	DH = (DH_0[0] * DH_0[1] * DH_0[2])**(1.0/3.0)
	DH_max = (DH_1[0] * DH_1[1] * DH_1[2])**(1.0/3.0)
	DH_min = (DH_2[0] * DH_2[1] * DH_2[2])**(1.0/3.0)

	return DH_max,DH_min,DH

def Sun2019(T,ol_h2o):

	A_H = -7.4
	A_H_err = 0.8
	EH = 130000.0
	EH_err = 17000.0

	r_sun = 0.41

	DH = (10.0**A_H) * (ol_h2o**r_sun) * np.exp(-EH / (R_const * T))
	DH_max = (10.0**(A_H + A_H_err)) * (ol_h2o**r_sun) * np.exp(-(EH-EH_err) / (R_const * T))
	DH_min = (10.0**(A_H - A_H_err)) * (ol_h2o**r_sun) * np.exp(-(EH+EH_err) / (R_const * T))

	return DH_max,DH_min,DH

def DuFrane2012(T,ol_h2o):

	A_H = [-4.9,-5.4,-8.4]
	A_H_err = [1.4,0,0]
	EH = [140000.0,170000.0,100000.0]
	EH_err = [30000.0,0,0]

	DH_0 = np.zeros((3,len(T[0])))
	DH_1 = np.zeros((3,len(T[0])))
	DH_2 = np.zeros((3,len(T[0])))
	for i in range(0,3):

		DH_0[i] = 10**(A_H[i]) * np.exp(-EH[i] / (R_const * T[0]))
		DH_1[i] = 10**(A_H[i] + A_H_err[i]) * np.exp(-(EH[i]-EH_err[i]) / (R_const * T[0]))
		DH_2[i] = 10**(A_H[i] - A_H_err[i]) * np.exp(-(EH[i]+EH_err[i]) / (R_const * T[0]))

	DH = (DH_0[0] * DH_0[1] * DH_0[2])**(1.0/3.0)
	DH_max = (DH_1[0] * DH_1[1] * DH_1[2])**(1.0/3.0)
	DH_min = (DH_2[0] * DH_2[1] * DH_2[2])**(1.0/3.0)

	return DH_max,DH_min,DH

def Kohlstedt1998(T,ol_h2o):

	A_H = [-3.85,-3.82,-6.83]

	EH = [145000.0,180000.0,110000.0]

	DH_0 = np.zeros((3,len(T[0])))

	for i in range(0,3):
		DH_0[i] = 10**(A_H[i]) * np.exp(-EH[i] / (R_const * T[0]))

	DH = (DH_0[0] * DH_0[1] * DH_0[2])**(1.0/3.0)
	DH_max = DH
	DH_min = DH

	return DH_max,DH_min,DH

def Demouchy2006(T,ol_h2o):

	A_H = [-4.5,-4.5,-1.4]
	A_H_err = [4.1,4.1,0.5]

	EH = [204000.0,204000.0,258000.0]
	EH_err = [94000.0,94000.0,11000.0]

	DH_0 = np.zeros((3,len(T[0])))
	DH_0_max = np.zeros((3,len(T[0])))
	DH_0_min = np.zeros((3,len(T[0])))

	for i in range(0,3):
		DH_0[i] = 10**(A_H[i]) * np.exp(-EH[i] / (R_const * T[0]))
		DH_0_max[i] = 10**(A_H[i] + A_H_err[i]) * np.exp(-(EH[i] - EH_err[i]) / (R_const * T[0]))
		DH_0_min[i] = 10**(A_H[i] - A_H_err[i]) * np.exp(-(EH[i] + EH_err[i]) / (R_const * T[0]))

	DH = (DH_0[0] * DH_0[1] * DH_0[2])**(1.0/3.0)
	DH_max = (DH_0_max[0] * DH_0_max[1] * DH_0_max[2])**(1.0/3.0)
	DH_min = (DH_0_min[0] * DH_0_min[1] * DH_0_min[2])**(1.0/3.0)

	return DH_max,DH_min,DH
