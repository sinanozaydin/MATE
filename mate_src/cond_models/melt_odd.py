#!/usr/bin/env python3

import numpy as np

def Ni2011_Basalt(model_method,T,P,corr_factor,fo2,fo2_ref,wt_err,ol_h2o):

	cond = np.exp(2.172 - (860.82 - (204.46 * np.sqrt(melt_h2o))) / (T - 1146.8))

	return cond_max,cond_min,cond,dai_dry,cond_wet

def Gaillard2008_Carbonatite(T):

	R_const = 8.3144621

	cond = 3440 * np.exp(-31900 / (R_const * T))
	cond_max = (3440 + 800) * np.exp((-31900 - 800) / (R_const * T))
	cond_min = (3440 - 800) * np.exp((-31900 + 800) / (R_const * T))

	return cond_max, cond_min, cond
