#!/usr/bin/env python3

import numpy as np

R_const = 8.3144621

def Hirschmann2009_DryPeridotite(T, P):

    T_solidus = np.zeros(len(P))

    for i in range(0,len(P)):

        if P[i] <= 10.0:
            T_solidus[i] = (-1.092 * (P[i] - 10.0)**2.0) +\
                (32.39 * (P[i] - 10.0)) + 1935.0
        elif P[i] > 10.0:
            T_solidus[i] = (26.53 * (P[i]-23.5)) + 2175.0

    T_solidus = T_solidus + 273.15 #Converting to Kelvin

    return T_solidus

def Hirschmann2000_DryPeridotite(T, P):

    T_solidus = (-5.104 * (P**2.0)) + (132.899 * P) + 1120.661

    T_solidus = T_solidus + 273.15 #Converting to Kelvin

    return T_solidus

def Sarafian2017_DryPeridotite(T,P):

    T_solidus = Hirschmann2009_DryPeridotite(T,P)

    T_solidus = T_solidus + 60

    return T_solidus
