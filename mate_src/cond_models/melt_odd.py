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

def Sifre2014(T, Melt_H2O, Melt_CO2):

	R_const = 8.3144621

	Melt_H2O = Melt_H2O * 1e-4 #converting ppm to wt percent
	Melt_CO2 = Melt_CO2 * 1e-4

	E_CO2 = 789166.0 * np.exp(-0.1808 * Melt_CO2) + 32820.0
	E_H2O = 88744 * np.exp(-3.88 * Melt_H2O) + 73029.0

	sigma_co2 = np.exp((5.5 * (1e-5) * E_CO2) + 5.7956)
	sigma_h2o = np.exp((4.54 * (1e-5) * E_H2O) + 5.5607)

	cond = (sigma_h2o * np.exp(-E_H2O / (R_const * T))) +\
	 	(sigma_co2 * np.exp(-E_CO2 / (R_const * T)))

	return cond, cond, cond
