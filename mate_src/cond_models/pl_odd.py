#!/usr/bin/env python3

import numpy as np

R_const = 8.3144621

def Li2016_Phlogopite(T, P, param1, param2, method):

	A_li_001 = 10**10.15
	A_li_010 = 10**8.41#!/usr/bin/env python3

import numpy as np

R_const = 8.3144621

def Li2016(T,flu,method):

	A_li_001 = 10**10.15
	A_li_010 = 10**8.41
	A_li_110 = 10**6.09

	E_li_001 = 204000.0
	E_li_010 = 179000.0
	E_li_110 = 134000.0

	E_li_001_err = 3000.0
	E_li_010_err = 4000.0
	E_li_110_err = 5000.0

	cond_001 = A_li_001 * np.exp(-(E_li_001) / (R_const * T))
	cond_010 = A_li_010 * np.exp(-(E_li_010) / (R_const * T))
	cond_110 = A_li_110 * np.exp(-(E_li_110) / (R_const * T))

	if method == 'array':
		cond_001_max = A_li_001 * np.exp(-(E_li_001 - E_li_001_err) / (R_const * T))
		cond_001_min = A_li_001 * np.exp(-(E_li_001 + E_li_001_err) / (R_const * T))
		cond_010_max = A_li_010 * np.exp(-(E_li_010 - E_li_010_err) / (R_const * T))
		cond_010_min =  A_li_010 * np.exp(-(E_li_010 + E_li_010_err) / (R_const * T))
		cond_110_max = A_li_110 * np.exp(-(E_li_110 - E_li_110_err) / (R_const * T))
		cond_110_min = A_li_110 * np.exp(-(E_li_110 + E_li_110_err) / (R_const * T))

	cond = (cond_001 * cond_010 * cond_110)**(1.0/3.0)
	if method == 'array':
		cond_max = (cond_001_max * cond_010_max * cond_110_max)**(1.0/3.0)
		cond_min = (cond_001_min * cond_010_min * cond_110_min)**(1.0/3.0)
	else:
		cond_max = cond
		cond_min = cond

	return cond_max,cond_min,cond

def Li2017(T,flu,method):

	A_li = 10**8.59

	E_li = 191000.0

	E_li_err = 5000.0

	r_li = 0.98

	r_li_err = 0.06

	cond = A_li * (flu**r_li) * np.exp(-E_li / (R_const * T))
	if method == 'array':
		cond_max = A_li * (flu**(r_li - r_li_err)) * np.exp(-(E_li - E_li_err) / (R_const * T))
		cond_min = A_li * (flu**(r_li + r_li_err)) * np.exp(-(E_li + E_li_err) / (R_const * T))
	else:
		cond_max = cond
		cond_min = cond

	return cond_max,cond_min,cond

	A_li_110 = 10**6.09

	E_li_001 = 204000.0
	E_li_010 = 179000.0
	E_li_110 = 134000.0

	cond_001 = A_li_001 * np.exp(-(E_li_001) / (R_const * T))
	cond_010 = A_li_010 * np.exp(-(E_li_010) / (R_const * T))
	cond_110 = A_li_110 * np.exp(-(E_li_110) / (R_const * T))

	cond = (cond_001 * cond_010 * cond_110)**(1.0/3.0)

	return cond

def Li2017_Phlogopite_param1_F(T, P, param1, param2, method):

	A_li = 10**8.59
	E_li = 191000.0
	r_li = 0.98

	cond = A_li * (param1**r_li) * np.exp(-E_li / (R_const * T))

	return cond
