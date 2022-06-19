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

    return T_solidus
