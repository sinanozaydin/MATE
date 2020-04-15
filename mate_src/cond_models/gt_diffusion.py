#!/usr/bin/env python3

import numpy as np

R_const = 8.3144621

def Ingrin2006(T,gt_h2o):

	A_H = -6.28
	A_H_err = 0.72
	EH = 130000.0
	EH_err = 15000.0

	DH = (10.0**A_H) * np.exp(-EH / (R_const * T))
	DH_max = (10.0**(A_H + A_H_err)) * np.exp(-(EH-EH_err) / (R_const * T))
	DH_min = (10.0**(A_H - A_H_err)) * np.exp(-(EH+EH_err) / (R_const * T))

	return DH_max,DH_min,DH
