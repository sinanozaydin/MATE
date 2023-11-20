#!/usr/bin/env python3

import numpy as np

#List the odd-dry functions here that can be used.
###RULES###
#1. The name of the def has to be the same with the one entered in ol_dry.csv or opx_dry.csv
#2. Do not include the asterisks in the name. For exp: Constable2006*** (in csv) will be Constable2006
#Asterisks are automattically deleted in the code
#2. Function has to have the following variables as default: T,fe_ol,fe_opx,fe_cpx,fe_gt,P,fo2
#3. return the function with three variables in order of maximum,minimum,middle

#Some parameters to help you find maximum is
#-enthalpy error is max
#+pre exponent error is max
#+r exponent is max

def Constable2006(T,fe_ol,fe_opx,fe_cpx,fe_gt,P,fo2):

	#Conductivity of dry olivine taken from Constable (2006, GJI)

	e = 1.602e-19 #charge of the electron in coulombs
	k = 8.617e-5
	kT = T * k
	bfe = (5.06e24) * np.exp(-0.357 / kT)
	bmg = (4.58e26) * np.exp(-0.752 / kT)
	ufe = (12.2e-6) * np.exp(-1.05 / kT)
	umg = (2.72e-6) * np.exp(-1.09 / kT)
	condfe = bfe + (3.33e24 * np.exp(-0.02/kT) * (fo2*1e5)**(0.16666))
	condmg = bmg + (6.21e30 * np.exp(-1.83/kT) * (fo2*1e5)**(0.16666))

	sigma = (condfe * ufe * e) + (2.0*condmg* umg * e)
	sigma_max = sigma
	sigma_min = sigma

	return sigma_max,sigma_min,sigma

def Yoshino2012(T,fe_ol,fe_opx,fe_cpx,fe_gt,P,fo2):

	#Conductivity model from Yoshino et al. (2012, JGR:SE)
	#Function does not contain the effects of pressure since it has almost no effect.

	R_const = 8.3144621

	A0_yosh = 10.0**2.72
	A0_err = 37.0
	H_yosh = 196000.0
	H_yosh_err = 2000.0
	alpha_yosh = 149000.0
	alpha_yosh_err = 3000

	sigma_max = (A0_yosh + A0_err) * fe_ol * np.exp(- ((H_yosh-H_yosh_err) - ((alpha_yosh + alpha_yosh_err) * fe_ol**(0.33))) / (R_const * T))
	sigma_min = (A0_yosh - A0_err) * fe_ol * np.exp(- ((H_yosh+H_yosh_err) - ((alpha_yosh - alpha_yosh_err) * fe_ol**(0.33))) / (R_const * T))
	sigma = (A0_yosh) * fe_ol * np.exp(- ((H_yosh) - ((alpha_yosh) * fe_ol**(0.33))) / (R_const * T))

	return sigma_max,sigma_min,sigma

def Dai2014c(T,fe_ol,fe_opx,fe_cpx,fe_gt,P,fo2):

	R_const = 8.3144621

	sigma_dai2014c = 10**(2.77 + (-1.19 * fe_ol))
	e_dai2014c = 162000.0 + (-63000 * fe_ol)

	sigma = sigma_dai2014c * np.exp(-(e_dai2014c) / (R_const * T))
	sigma_max = sigma
	sigma_min = sigma

	return sigma_max,sigma_min,sigma

def Fullea2011_ol(T,fe_ol,fe_opx,fe_cpx,fe_gt,P,fo2):

	R_const = 8.3144621

	sigma_i_fullea = 10**4.73
	sigma_pol_fullea = 10**2.7 #average value of used models Fullea et al. (2011)

	e_i_fullea = 231000.0

	a_ful = [1.642,0.246,-4.85,3.259] #polynomial coefficients that calculates the fe-dependency of act. enthalpies from Omura et al (1989)
	dv_ful = 0.68e3
	fe_pol_fullea = (a_ful[0] + (a_ful[1] * fe_ol) + (a_ful[2] * (fe_ol**2.0)) + (a_ful[3]* (fe_ol**3.0)) + (P * dv_ful)) * 1e5

	sigma = (sigma_i_fullea * np.exp(-e_i_fullea / (R_const * T))) + (sigma_pol_fullea * np.exp(-fe_pol_fullea / (R_const * T)))
	sigma_max = sigma
	sigma_min = sigma

	return sigma_max,sigma_min,sigma

def Fullea2011_opx(T,fe_ol,fe_opx,fe_cpx,fe_gt,P,fo2):

	R_const = 8.3144621

	sigma_pol_fullea = 10**3.0 #average value of used models Fullea et al. (2011)

	b_ful = [1.9,-2.77,2.61,-1.09] #polynomical coefficients that calculates the fe-dependency of act. enthalpies from Seifert et al (1982)
	fe_pol_fullea = (b_ful[0] + (b_ful[1] * fe_opx) + (b_ful[2] * (fe_opx**2.0)) + (b_ful[3]* (fe_opx**3.0))) * 1e5

	sigma = (sigma_pol_fullea * np.exp(-fe_pol_fullea / (R_const * T)))
	sigma_max = sigma
	sigma_min = sigma

	return sigma_max,sigma_min,sigma

def Fullea2011_cpx(T,fe_ol,fe_opx,fe_cpx,fe_gt,P,fo2):

	R_const = 8.3144621

	sigma_pol_fullea = 10**3.25

	b_ful = [2.075,-2.77,2.61,-1.09] #polynomical coefficients that calculates the fe-dependency of act. enthalpies from Seifert et al (1982)
	fe_pol_fullea = (b_ful[0] + (b_ful[1] * fe_cpx) + (b_ful[2] * (fe_cpx**2.0)) + (b_ful[3]* (fe_cpx**3.0))) * 1e5

	sigma = (sigma_pol_fullea * np.exp(-fe_pol_fullea / (R_const * T)))
	sigma_max = sigma
	sigma_min = sigma

	return sigma_max,sigma_min,sigma

def Fullea2011_gt(T,fe_ol,fe_opx,fe_cpx,fe_gt,P,fo2):

	R_const = 8.3144621

	sigma_pol_fullea = (10.0)**(-0.72 + np.log10(1 - (0.44*P)))
	sigma_i_fullea = 4.96

	e_i_fullea = 205000.0

	b_ful = [2.6,-15.33,80.4,-194.6,202.6,-75.0]
	dv_ful = 2.5 * 1e-6
	fe_pol_fullea = (b_ful[0] + (b_ful[1] * fe_gt) + (b_ful[2] * (fe_gt**2.0)) + (b_ful[3]* (fe_gt**3.0)) +\
	(b_ful[4]* (fe_gt**4.0)) + (b_ful[5]* (fe_gt**5.0)) + (dv_ful * P)) * 1e5

	sigma = (sigma_i_fullea * np.exp(-e_i_fullea / (R_const * T))) +\
	 (sigma_pol_fullea * np.exp(-fe_pol_fullea / (R_const * T)))
	sigma_max = sigma
	sigma_min = sigma

	return sigma_max,sigma_min,sigma


def Zhang2016(T,fe_ol,fe_opx,fe_cpx,fe_gt,P,fo2):

	#Conductivity model from Zhang et al. (2016, Contr. Min. & Petr.)

	R_const = 8.3144621

	a_z1 = 855610
	e_z1 = 251000.0
	e_z1_err = 2000.0
	dv_z1 = 4.15*1e-6
	a_z2 = 163
	e_z2 = 233000.0
	e_z2_err = 1000.0
	alpha_z2 = 199000.0
	alpha_z2_err = 60.0
	dv_z2 = 1.06*1e-6
	beta_z2 = 12000


	sigma_max = a_z1 * np.exp(- ((e_z1 - e_z1_err) + (P * dv_z1)) / (R_const * T)) +\
	 (a_z2 * fe_opx * np.exp(- ((e_z2 - e_z2_err) - ((alpha_z2 + alpha_z2_err) * (fe_opx**0.33)) + (P * (dv_z2 - ((beta_z2)*fe_opx)))) / (R_const * T)))
	sigma_min = a_z1 * np.exp(- ((e_z1 + e_z1_err) + (P * dv_z1)) / (R_const * T)) +\
	 (a_z2 * fe_opx * np.exp(- ((e_z2 + e_z2_err) - ((alpha_z2 - alpha_z2_err) * (fe_opx**0.33)) + (P * (dv_z2 - ((beta_z2)*fe_opx)))) / (R_const * T)))
	sigma = a_z1 * np.exp(- (e_z1 + (P * dv_z1)) / (R_const * T)) +\
	 (a_z2 * fe_opx * np.exp(- (e_z2 - (alpha_z2 * (fe_opx**0.33)) + (P * (dv_z2 - (beta_z2*fe_opx)))) / (R_const * T)))

	return sigma_max,sigma_min,sigma

def Pommier2018(T,fe_ol,fe_opx,fe_cpx,fe_gt,P,fo2):

	#For Ol fro Pommier et al. (2018)

	R_const = 8.3144621

	A = [284.0,780.0,261.0]
	A_err = [53.0,73.0,45.0]

	E = [126400.0,122700.0,114500.0]
	E_err = [2000.0,1100.0,1900.0]

	sigma = np.zeros((3,len(T)))
	sigma_max = np.zeros((3,len(T)))
	sigma_min = np.zeros((3,len(T)))

	for i in range(0,3):
		sigma[i] = A[i] * np.exp(-E[i] / (R_const*T))
		sigma_max[i] = (A[i]+A_err[i]) * np.exp(-(E[i] - E_err[i]) / (R_const*T))
		sigma_min[i] = (A[i]-A_err[i]) * np.exp(-(E[i] + E_err[i]) / (R_const*T))

	sigma = (sigma[0] * sigma[1] * sigma[2])**(1.0/3.0)
	sigma_max = (sigma_max[0] * sigma_max[1] * sigma_max[2])**(1.0/3.0)
	sigma_min = (sigma_min[0] * sigma_min[1] * sigma_min[2])**(1.0/3.0)

	return sigma_max,sigma_min,sigma

def Dai2009a_dry(T,fe_ol,fe_opx,fe_cpx,fe_gt,P,fo2):

	#For GT from Dai and Karato (2009)
	#There's a wet version of this model so it is denoted with extra _dry at the end

	R_const = 8.3144621

	A_dai = 1036.0
	A_dai_err = 870
	B = 0.044
	E_dai = 128000.0
	E_dai_err = 6000.0
	V_dai = 2.50 * 1e-6

	sigma_max = (A_dai + A_dai_err) * (1-(B*P)) * np.exp(-((E_dai - E_dai_err) + (P*1e9*V_dai)) / (R_const * T))
	sigma_min = (A_dai - A_dai_err) * (1-(B*P)) * np.exp(-((E_dai + E_dai_err) + (P*1e9*V_dai)) / (R_const * T))
	sigma = (A_dai) * (1-(B*P)) * np.exp(-((E_dai) + (P*1e9*V_dai)) / (R_const * T))

	return sigma_max,sigma_min,sigma
