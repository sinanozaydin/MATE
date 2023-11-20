#!/usr/bin/env python3

import numpy as np

def Dai2014a(model_method,T,P,corr_factor,fo2,fo2_ref,wt_err,ol_h2o,method):

	R_const = 8.3144621

	dv_dai2014 = -0.86 * 1e3 # m^3 /mol Taken from Dai2014b-PEPI, Error is insignificant, since the effect itself is insignificant...
	p_ref = 4.0
	cw_ref = 460.0 / 1e4
	e1_dai = 74000.0
	e1_dai_err = 3000
	e2_dai = 115000
	e2_dai_err = 4000
	r_dai = 0.8
	r_dai_err = 0.2
	q_dai = -0.066 #Taken from Dai2014c-P"EPI, Error is insignificant.
	q_dry = 0.16666 #Taken from Constable (2006)
	wt_err = wt_err
	h2o = ol_h2o / (1e4 * corr_factor)
	#Changing fo2 to complex to avoid Runtime errors
	fo2 = np.array(fo2, dtype = np.complex)
	fo2_ref = np.array(fo2_ref, dtype = np.complex)
	#p*dv multiplied by 1e3 to get them all on the basis of the SI units J/mol, which activation energy is in.
	if method == 'array':
		dai_ref_max = ((10.0**0.48) * np.exp(-((e1_dai - e1_dai_err) + (p_ref*dv_dai2014)) / (R_const * T))) + (10.0**2.84 * np.exp(-((e2_dai-e2_dai_err) + (p_ref*dv_dai2014)) / (R_const * T)))
		dai_ref_min = ((10.0**0.48) * np.exp(-((e1_dai + e1_dai_err) + (p_ref*dv_dai2014)) / (R_const * T))) + (10.0**2.84 * np.exp(-((e2_dai+e2_dai_err) + (p_ref*dv_dai2014)) / (R_const * T)))
		cond_max_wet = (dai_ref_max * (((h2o + (h2o * wt_err)) / (cw_ref))**(r_dai-r_dai_err)) * (fo2/fo2_ref)**(q_dai)) *  np.exp(- ((P - p_ref) * dv_dai2014) / (R_const*T))
		cond_min_wet = (dai_ref_min * (((h2o - (h2o * wt_err)) / (cw_ref))**(r_dai+r_dai_err)) * (fo2/fo2_ref)**(q_dai)) *  np.exp(- ((P - p_ref) * dv_dai2014) / (R_const*T))
	dai_ref = ((10.0**0.48) * np.exp(-((e1_dai) + (p_ref*dv_dai2014)) / (R_const * T))) + (10.0**2.84 * np.exp(-((e2_dai) + (p_ref*dv_dai2014)) / (R_const * T)))
	cond_wet = (dai_ref * (h2o / (cw_ref))**(r_dai) * (fo2/fo2_ref)**(q_dai)) *  np.exp(- ((P - p_ref) * dv_dai2014) / (R_const*T))
	dai_dry =  10**2.4 * ((fo2/fo2_ref)**(q_dry)) * np.exp(-(154000.0 + (P * dv_dai2014)) / (R_const * T))

	if model_method == 0:

		cond = np.real(dai_dry + cond_wet)
		if method == 'array':
			cond_max = np.real(dai_dry + cond_max_wet)
			cond_min = np.real(dai_dry + cond_min_wet)
		else:
			cond_max = cond
			cond_min = cond

	elif model_method == 1:

		cond = np.real(cond_wet)

		if method == 'array':
			cond_max = np.real(cond_max_wet)
			cond_min = np.real(cond_min_wet)
		else:
			cond_max = cond
			cond_min = cond

	return cond_max,cond_min,cond,dai_dry,cond_wet

def Dai2020_200ppmTi(model_method,T,P,corr_factor,fo2,fo2_ref,wt_err,ol_h2o,method):

	R_const = 8.3144621

	dv_dai2014 = -0.86 * 1e-6 # m^3 /mol Taken from Dai2014b-PEPI, Error is insignificant, since the effect itself is insignificant...
	q_dai = -0.066 #Taken from Dai2014c-P"EPI, Error is insignificant.
	q_dry = 0.16666 #Taken from Constable (2006)

	wt_err = wt_err
	h2o = ol_h2o / (1e4 * corr_factor)

	A_dai_200 = 3.01

	r_dai_200 = 0.51
	r_dai_200_err = 0.18

	E_dai_200 = 87000.0
	E_dai_200_err = 3000.0

	cond_wet = (10.0 ** A_dai_200) * ((h2o)**r_dai_200) * np.exp(-(E_dai_200) / (R_const * T))
	if method == 'array':
		cond_max_wet = (10.0 ** A_dai_200) * ((h2o + (h2o * wt_err))**(r_dai_200-r_dai_200_err)) * np.exp(-(E_dai_200-E_dai_200_err) / (R_const * T))
		cond_min_wet = (10.0 ** A_dai_200) * ((h2o - (h2o * wt_err))**(r_dai_200+r_dai_200_err)) * np.exp(-(E_dai_200+E_dai_200_err) / (R_const * T))

	dai_dry =  10**2.4 * ((fo2/fo2_ref)**(q_dry)) * np.exp(-(154000.0 + (P * dv_dai2014)) / (R_const * T))

	if model_method == 0:

		cond = dai_dry + cond_wet
		if method == 'array':
			cond_max = dai_dry + cond_max_wet
			cond_min = dai_dry + cond_min_wet
		else:
			cond_max = cond
			cond_min = cond

	elif model_method == 1:

		cond = cond_wet
		if method == 'array':
			cond_max = cond_max_wet
			cond_min = cond_min_wet
		else:
			cond_max = cond
			cond_min = cond

	return cond_max,cond_min,cond,dai_dry,cond_wet


def Dai2020_683ppmTi(model_method,T,P,corr_factor,fo2,fo2_ref,wt_err,ol_h2o,method):

	R_const = 8.3144621

	e1_dai = 100000.0
	e1_dai_err = 2000.0
	A1_dai = 10.0**1.94
	e2_dai = 94000.0
	e2_dai_err = 2000.0
	A2_dai = 10.0**3.98
	r_dai = 0.98
	r_dai_err = 0.21
	q_dai = -0.089
	q_dry = 0.097
	h2o = ol_h2o / (1e4+corr_factor)
	dai_dry = A1_dai * ((fo2/fo2_ref)**(q_dry)) * np.exp(-(e2_dai) / (R_const * T))
	cond_wet = A2_dai * ((fo2/fo2_ref)**(q_dai)) * ((h2o)**(r_dai - r_dai_err)) * np.exp(-(e2_dai) / (R_const * T))
	if method == 'array':
		cond_max_wet = A2_dai * ((fo2/fo2_ref)**(q_dai)) * (h2o + (h2o * wt_err))**(r_dai - r_dai_err) * np.exp(-(e2_dai - e2_dai_err) / (R_const * T))
		cond_min_wet = A2_dai * ((fo2/fo2_ref)**(q_dai)) * (h2o - (h2o * wt_err))**(r_dai + r_dai_err) * np.exp(-(e2_dai + e2_dai_err) / (R_const * T))


	if model_method == 0:
		cond = dai_dry + cond_wet
		if method == 'array':
			cond_max = dai_dry + cond_max_wet
			cond_min = dai_dry + cond_min_wet
		else:
			cond_max = cond
			cond_min = cond

	elif model_method == 1:

		cond = cond_wet
		if method == 'array':
			cond_max = cond_max_wet
			cond_min = cond_min_wet
		else:
			cond_max = cond
			cond_min = cond

	return cond_max,cond_min,cond,dai_dry,cond_wet
