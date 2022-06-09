#!/usr/bin/env python3

import numpy as np

R_const = 8.3144621

def Sifre2014(T, P, Melt_H2O, Melt_CO2, Melt_Na2O):

	Melt_H2O = Melt_H2O * 1e-4 #converting ppm to wt percent
	Melt_CO2 = Melt_CO2 * 1e-4 #converting ppm to wt percent

	E_CO2 = 789166.0 * np.exp(-0.1808 * Melt_CO2) + 32820.0
	E_H2O = 88744 * np.exp(-0.388 * Melt_H2O) + 73029.0

	sigma_co2 = np.exp((5.5 * (1e-5) * E_CO2) + 5.7956)
	sigma_h2o = np.exp((4.54 * (1e-5) * E_H2O) + 5.5607)

	cond = (sigma_h2o * np.exp(-E_H2O / (R_const * T))) +\
	 	(sigma_co2 * np.exp(-E_CO2 / (R_const * T)))

	return cond, cond, cond

def Pommier2008(T, P, Melt_H2O, Melt_CO2, Melt_Na2O):

	Melt_H2O = Melt_H2O * 1e-4 #convering ppm to wt
	P = P * 1e3 #converting GPa to MPa

	phi = (2.439e-11 * Melt_Na2O) + 1.72e-10
	G = (-2.107e11 * Melt_Na2O) + 1.297e12

	Eb = 0.23 * (1*8*(1.602e-19)**2) / (phi * (1.02e-10 - 1.4e-10))
	Es = 4.0 * np.pi * G * 1.7e-10 * (1.02e-10 - 9.3e-11)**2.0 + (1e3 * Melt_H2O**2.0)

	Ea = Eb + Es

	sigma_0 = np.exp((Ea + 9.9) / 12.5)

	cond = sigma_0 * np.exp((-Ea - (P * 20)) / (R_const*T))


	return cond, cond, cond


def Ni2011(T, P, Melt_H2O, Melt_CO2, Melt_Na2O):

	Melt_H2O = 0.3 #convering ppm to wt

	cond = 10**(2.172 - ((860.82 - (204.46*np.sqrt(Melt_H2O))) / (T - 1146.8)))

	return cond, cond, cond

def Scarlato2004_DryBasalt(T, P, Melt_H2O, Melt_CO2, Melt_Na2O):

	sigma_0 = 309.0
	E = 82000

	cond = sigma_0 * np.exp(-E / (R_const * T))

	return cond, cond, cond

def TyburczyWaff1983_DryTholeiite(T, P, Melt_H2O, Melt_CO2, Melt_Na2O):

	sigma_0_low = 1.12e5
	E_low = 112000.0
	dv_low = 4.6

	sigma_0_high = 2.15e5
	E_high = 153000.0
	dv_high = -0.06

	cond = np.zeros(len(T))
	for i in range(0,len(T)):

		if P[i] < 0.9:
			cond[i] = sigma_0_low * np.exp(-(E_low + (dv_low * P[i] * 1e3)) / (R_const * T[i]))
		else:
			cond[i] = sigma_0_high * np.exp(-(E_high + (dv_high * P[i] * 1e3)) / (R_const * T[i]))

	return cond, cond, cond

def TyburczyWaff1983_DryAndesite(T, P, Melt_H2O, Melt_CO2, Melt_Na2O):

	sigma_0_low = 1.01e3
	E_low = 78000.0
	dv_low = 17.9

	sigma_0_high = 6.61e3
	E_high = 117000.0
	dv_high = 3.25

	cond = np.zeros(len(T))
	for i in range(0,len(T)):

		if P[i] < 0.9:
			cond[i] = sigma_0_low * np.exp(-(E_low + (dv_low * P[i] * 1e3)) / (R_const * T[i]))
		else:
			cond[i] = sigma_0_high * np.exp(-(E_high + (dv_high * P[i] * 1e3)) / (R_const * T[i]))

	return cond, cond, cond
