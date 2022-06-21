#!/usr/bin/env python3

import numpy as np

def Hirschmann2009_Dry(T,P,H2O,Melt_H2O):

    T_solidus = np.zeros(len(P))

    for i in range(0,len(P)):

        if P[i] <= 10.0:
            T_solidus[i] = (-5.1404654*(P[i]**2.0)) +\
                (132.899012 * P[i]) + 1124.123
        elif P[i] > 10.0:
            T_solidus[i] = (-1.092*(P[i]-10)**2.0) +\
                (32.39 * (P[i]-10)) + 1395.0

    T_solidus = T_solidus + 273.15 #Converting to Kelvin

    return T_solidus

def Katz2003(T, P, H2O, Melt_H2O):

    T_solidus = 1085.7 + (132.9*P) - (5.1*P**2)
    T_liquids_lherz = 1475.0 + (80.0*P) - (3.2*P**2)
    T_liquidus = 1780.0 + (45.0*P) - (2.0*P**2)

    R_cpx = 0.5 * (0.08 * P)

    X_h2o_sat_melt = (12.0*P**0.6) + (1.0*P)
