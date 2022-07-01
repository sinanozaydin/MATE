#!/usr/bin/env python3

import numpy as np

def Dai2009a(model_method,T,P,corr_factor,wt_err,fo2,fo2_ref,gt_h2o,method):

	R_const = 8.3144621

	A_dai = [1036.0,1950.0]
	A_dai_err = [870,236]
	B = 0.044
	r_dai_gt = 0.63
	r_dai_gt_err = 0.19
	E_dai = [128000.0,70000.0]
	E_dai_err = [6000,5000]
	V_dai = [2.50e-6,-0.57e-6]

	h2o = gt_h2o / (corr_factor*1e4)

	cond_wet = (A_dai[1] * (h2o**r_dai_gt) * np.exp(-((E_dai[1]) + (P*1e9*V_dai[1])) / (R_const * T)))
	cond_dry = (A_dai[0] * (1-(B*P)) * np.exp(-((E_dai[0]) + (P*1e9*V_dai[0])) / (R_const * T)))

	if method == 'array':
		cond_max_wet = (A_dai[1] * ((h2o + (h2o * wt_err))**(r_dai_gt-r_dai_gt_err)) * np.exp(-((E_dai[1] - E_dai_err[1]) + (P*1e9*V_dai[1])) / (R_const * T)))
		cond_min_wet = (A_dai[1] * ((h2o - (h2o * wt_err))**(r_dai_gt+r_dai_gt_err)) * np.exp(-((E_dai[1] + E_dai_err[1]) + (P*1e9*V_dai[1])) / (R_const * T)))
		cond_dry_max = (A_dai[0] * (1-(B*P)) * np.exp(-((E_dai[0] - E_dai_err[0]) + (P*1e9*V_dai[0])) / (R_const * T)))
		cond_dry_min = (A_dai[0] * (1-(B*P)) * np.exp(-((E_dai[0] + E_dai_err[0]) + (P*1e9*V_dai[0])) / (R_const * T)))


	if model_method == 0:

		cond = cond_dry + cond_wet
		if method == 'array':
			cond_max = cond_dry_max + cond_max_wet
			cond_min = cond_dry_min + cond_min_wet
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

	return cond_max,cond_min,cond,cond_dry,cond_wet
