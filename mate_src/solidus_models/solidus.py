#!/usr/bin/env python3

import numpy as np

R_const = 8.3144621

def Hirschmann2009_DryPeridotite(T, P):

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
