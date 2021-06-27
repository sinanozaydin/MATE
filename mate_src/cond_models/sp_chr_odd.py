#!/usr/bin/env python3

import numpy as np

R_const = 8.3144621

def Sun2021(T):

	#Hydrogenated metstable part at 2GPa

	A_sun = 10**3.65

	E_sun = 47000.0

	cond = A_sun * np.exp(-E_sun / (R_const * T))

	cond_max = cond
	cond_min = cond

	return cond_max,cond_min,cond
