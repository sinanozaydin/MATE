#!/usr/bin/env python3

import numpy as np

def Sifre2014(T, Melt_H2O, Melt_CO2):

	R_const = 8.3144621

	Melt_H2O = Melt_H2O * 1e-4 #converting ppm to wt percent
	Melt_CO2 = Melt_CO2 * 1e-4 #converting ppm to wt percent

	E_CO2 = 789166.0 * np.exp(-0.1808 * Melt_CO2) + 32820.0
	E_H2O = 88744 * np.exp(-0.388 * Melt_H2O) + 73029.0

	sigma_co2 = np.exp((5.5 * (1e-5) * E_CO2) + 5.7956)
	sigma_h2o = np.exp((4.54 * (1e-5) * E_H2O) + 5.5607)

	cond = (sigma_h2o * np.exp(-E_H2O / (R_const * T))) +\
	 	(sigma_co2 * np.exp(-E_CO2 / (R_const * T)))

	return cond, cond, cond
