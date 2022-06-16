#!/usr/bin/env python3

import numpy as np

R_const = 8.3144621

def Sifre2014_H2O_CO2(T, P, Melt_H2O, Melt_CO2, Melt_Na2O, Melt_K2O):

	Melt_H2O = Melt_H2O * 1e-4 #converting ppm to wt percent
	Melt_CO2 = Melt_CO2 * 1e-4 #converting ppm to wt percent

	E_CO2 = 789166.0 * np.exp(-0.1808 * Melt_CO2) + 32820.0
	E_H2O = 88744 * np.exp(-0.388 * Melt_H2O) + 73029.0

	sigma_co2 = np.exp((5.5 * (1e-5) * E_CO2) + 5.7956)
	sigma_h2o = np.exp((4.54 * (1e-5) * E_H2O) + 5.5607)

	cond = (sigma_h2o * np.exp(-E_H2O / (R_const * T))) +\
	 	(sigma_co2 * np.exp(-E_CO2 / (R_const * T)))

	return cond, cond, cond

def Pommier2008(T, P, Melt_H2O, Melt_CO2, Melt_Na2O, Melt_K2O):

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


def Ni2011(T, P, Melt_H2O, Melt_CO2, Melt_Na2O, Melt_K2O):

	Melt_H2O = 0.3 #convering ppm to wt

	cond = 10**(2.172 - ((860.82 - (204.46*np.sqrt(Melt_H2O))) / (T - 1146.8)))

	return cond, cond, cond

def Scarlato2004_DryBasalt(T, P, Melt_H2O, Melt_CO2, Melt_Na2O, Melt_K2O):

	sigma_0 = 309.0
	E = 82000

	cond = sigma_0 * np.exp(-E / (R_const * T))

	return cond, cond, cond

def TyburczyWaff1983_DryTholeiite(T, P, Melt_H2O, Melt_CO2, Melt_Na2O, Melt_K2O):

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

def TyburczyWaff1983_DryAndesite(T, P, Melt_H2O, Melt_CO2, Melt_Na2O, Melt_K2O):

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

def Gaillard2005_K2O_Dependent(T, P, Melt_H2O, Melt_CO2, Melt_Na2O, Melt_K2O):

	a = 0.172 - (0.105 * Melt_K2O)
	b = 4.742 - (0.6 * Melt_K2O)

	cond = 10.0**(a + (b * (1.0/T)))

	return cond, cond, cond

def Guo2017_WetAndesite(T, P, Melt_H2O, Melt_CO2, Melt_Na2O, Melt_K2O):

	Melt_H2O = Melt_H2O * 1e-4 #converting to wt percent

	cond = 10**(5.23 - (0.56 * (Melt_H2O**0.6)) - ((8130.4 - (1462.7*(Melt_H2O**0.6)) + ((581.3 - (12.7*Melt_H2O**2)) * P)) / T))

	return cond, cond, cond

def Laumonier2017_WetAndesite(T, P, Melt_H2O, Melt_CO2, Melt_Na2O, Melt_K2O):

	Melt_H2O = Melt_H2O * 1e-4 #converting to wt percent
	P = P * 1e5 #converting gpa to bars

	a = -0.34
	b = 8.96
	c = -8.07e-6
	d = 1.67e-4
	e = -9627
	f = 1.25e5
	g = -1.46e-1
	h = 2.462

	sigma_0 = np.exp(((a*Melt_H2O) + b) + (P * ((c*Melt_H2O) + d)))
	Ea = (e * Melt_H2O) + f
	dV = (g * Melt_H2O) + h

	cond = sigma_0 * np.exp(-(Ea + (P * dV)) / (R_const * T))

	return cond, cond, cond

def Laumonier2015_WetDacite(T, P, Melt_H2O, Melt_CO2, Melt_Na2O, Melt_K2O):

	Melt_H2O = Melt_H2O * 1e-4 #converting to wt percent
	P = P * 1e5 #converting gpa to bars

	a = -0.064
	b = 5.96
	c = 1.06e-5
	d = 2.49e-5
	e = -6146
	f = 88440
	g = 0.176
	h = 0.388

	sigma_0 = np.exp(((a*Melt_H2O) + b) + (P * ((c*Melt_H2O) + d)))
	Ea = (e * Melt_H2O) + f
	dV = (g * Melt_H2O) + h

	cond = sigma_0 * np.exp(-(Ea + (P * dV)) / (R_const * T))

	return cond, cond, cond

def Gaillard2004_WetRhyolite(T, P, Melt_H2O, Melt_CO2, Melt_Na2O, Melt_K2O):

	Melt_H2O = Melt_H2O * 1e-4 #converting to wt percent
	P = P * 1e3


	Ea = (-2925 * np.log(Melt_H2O)) + 64132.0
	sigma_0 = (-78.9 * np.log(Melt_H2O)) + 754.0

	cond = sigma_0 * np.exp((-Ea + (20*P)) / (R_const * T))

	return cond, cond, cond

def Guo2016_WetRhyolite(T, P, Melt_H2O, Melt_CO2, Melt_Na2O, Melt_K2O):

	Melt_H2O = Melt_H2O * 1e-4 #converting to wt percent

	cond = 10**(2.983 - (0.0732*Melt_H2O) -\
		((3528 - (233.8*Melt_H2O) + ((763 - 7.5*Melt_H2O**2)*P)) / T))

	return cond, cond, cond

def Chen2018_WetGranite(T, P, Melt_H2O, Melt_CO2, Melt_Na2O, Melt_K2O):

	Melt_H2O = Melt_H2O * 1e-4 #converting to wt percent

	sigma_0 = 6.673 - (0.491*P)
	Ea = 58987.0 - (2200 * np.log(Melt_H2O + 0.046))
	dV = 10927.0 - (1981 * Melt_H2O)

	cond = sigma_0 * np.exp(-(Ea + (P * dV)) / (R_const * T))

	return cond, cond, cond

def Guo2018_WetGranite(T, P, Melt_H2O, Melt_CO2, Melt_Na2O, Melt_K2O):

	Melt_H2O = Melt_H2O * 1e-4 #converting to wt percent

	cond = 10.0**(3.205 - (0.102 * Melt_H2O) -\
		(-(4228.5 - (354.7 * Melt_H2O) + (693.6 * P)) / T))

	return cond, cond, cond
