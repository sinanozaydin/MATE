#!/usr/bin/env python3

import numpy as np

def Zhao2016(model_method,T,P,corr_factor,wt_err,fo2,fo2_ref,cpx_h2o,cpx_fe,method):

	R_const = 8.3144621

	h2o = cpx_h2o / (corr_factor*1e4)

	a_zhao = [1.29,3.69,3.52]
	r_zhao = [0.58,1.28,0.79]
	r_zhao_err = [0.15,0.05,0.04]
	e_zhao = [83000.0,115000.0,129000.0]
	e_zhao_err = [7000,2000,2000]

	cond = (a_zhao[0] * (h2o**(r_zhao[0])) * np.exp(- (e_zhao[0]) / (R_const * T))) +\
	(a_zhao[1] * (h2o)**(r_zhao[1]) * np.exp(- (e_zhao[1]) / (R_const * T))) +\
	(a_zhao[2] * (h2o)**(r_zhao[2]) * np.exp(- (e_zhao[2]) / (R_const * T)))

	if method == 'array':

		cond_max_ = (a_zhao[0] * (h2o + (h2o * wt_err))**(r_zhao[0]-r_zhao_err[0]) * np.exp(- (e_zhao[0] - e_zhao_err[0]) / (R_const * T))) +\
		(a_zhao[1] * (h2o + (h2o * wt_err))**(r_zhao[1]-r_zhao_err[1]) * np.exp(- (e_zhao[1] - e_zhao_err[1]) / (R_const * T))) +\
		(a_zhao[2] * (h2o + (h2o * wt_err))**(r_zhao[2]-r_zhao_err[2]) * np.exp(- (e_zhao[2] - e_zhao_err[2]) / (R_const * T)))

		cond_min = (a_zhao[0] * (h2o - (h2o * wt_err))**(r_zhao[0]+r_zhao_err[0]) * np.exp(- (e_zhao[0] + e_zhao_err[0]) / (R_const * T))) +\
		(a_zhao[1] * (h2o - (h2o * wt_err))**(r_zhao[1]+r_zhao_err[1]) * np.exp(- (e_zhao[1] + e_zhao_err[1]) / (R_const * T))) +\
		(a_zhao[2] * (h2o - (h2o * wt_err))**(r_zhao[2]+r_zhao_err[2]) * np.exp(- (e_zhao[2] + e_zhao_err[2]) / (R_const * T)))

	else:

		cond_max = cond
		cond_min = cond

	cond_dry = np.zeros(len(cond))

	return cond_max,cond_min,cond,cond_dry,cond

def Zhang2019(model_method,T,P,corr_factor,wt_err,fo2,fo2_ref,cpx_h2o,cpx_fe,method):

	R_const = 8.3144621

	h2o = cpx_h2o / (corr_factor*1e4)

	a_zhang = 1438.0
	a_zhang_err = 260.0
	n_zhang = 0.09
	n_zhang_err = 0.03
	r_zhang = 1.1
	r_zhang_err = 0.1
	E_zhang = 105000.0
	E_zhang_err = 3000.0
	alpha_zhang = 71000.0
	alpha_zhang_err = 5000.0
	beta_zhang = 38000.0
	beta_zhang_err = 7000.0

	cond = (a_zhang) * (cpx_fe**n_zhang) * (h2o**r_zhang) *\
	np.exp(-(E_zhang - (alpha_zhang*cpx_fe) - (beta_zhang*(h2o**(1.0/3.0)))) / (R_const*T))

	if method == 'array':
		cond_max = (a_zhang + a_zhang_err) * (cpx_fe**(n_zhang-n_zhang_err)) * ((h2o + (h2o * wt_err))**(r_zhang-r_zhang_err)) *\
		np.exp(-((E_zhang - E_zhang_err) - ((alpha_zhang-alpha_zhang_err)*cpx_fe) - ((beta_zhang-beta_zhang_err)*((h2o + (h2o * wt_err))**(1.0/3.0)))) / (R_const*T))
		cond_min = (a_zhang - a_zhang_err) * (cpx_fe**(n_zhang+n_zhang_err)) * ((h2o - (h2o * wt_err))**(r_zhang+r_zhang_err)) *\
		np.exp(-((E_zhang + E_zhang_err) - ((alpha_zhang+alpha_zhang_err)*cpx_fe) - ((beta_zhang+beta_zhang_err)*((h2o - (h2o * wt_err))**(1.0/3.0)))) / (R_const*T))
	else:
		cond_max = cond
		cond_min = cond

	cond_dry = np.zeros(len(cond))

	return cond_max,cond_min,cond,cond_dry,cond
