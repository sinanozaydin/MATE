#!/usr/bin/env python3

import numpy as np

R_const = 8.3144621

def Hu2018H(T):

	#Hydrogenated metstable part at 2GPa

	A_hu = 10**2.079

	E_hu = 81000.0

	cond = A_hu * np.exp(-E_hu / (R_const * T))

	cond_max = cond
	cond_min = cond

	return cond_max,cond_min,cond

def Hu2018DH(T):

	#Dehydrogenated metstable part at 2GPa

	A_hu = 10**1.87
	E_hu = 68000.0

	cond = A_hu * np.exp(-E_hu / (R_const * T))
	cond_max = cond
	cond_min = cond

	return cond_max,cond_min,cond

def Wang2012(T):

	#Conductivity model taken from Wang et al. (2012) - Contr. to Min Petr
	#This is the Hornblende and actinolite.

	A_wang_amph = [10**2.03,10**23.88]

	E_wang_amph = [67000.0,378000.0]

	cond = (A_wang_amph[0] * np.exp(-E_wang_amph[0] / (R_const*T))) + (A_wang_amph[1] * np.exp(-E_wang_amph[1] / (R_const*T)))

	cond_min = cond
	cond_max = cond

	return cond_max,cond_min,cond

def Wang2012_LE(T):

	A_wang_amph = 10**2.03

	E_wang_amph = 67000.0

	cond = (A_wang_amph * np.exp(-E_wang_amph / (R_const*T)))

	cond_max = cond
	cond_min = cond

	return cond_max,cond_min,cond
