#!/usr/bin/env python3

import numpy as np

R_const = 8.3144621

def Dasgupta2013_CarbonatedPeridotite(T, T_solidus, P, CO2_Melt):

    CO2_Melt = CO2_Melt * 1e-4 #Converting to weight percent

    delta_T = np.zeros(len(T))

    for i in range(0,len(P)):

        if P[i] <= 2.5:
            a = 19.21
            b = 1491.36
            c = 0.86
        elif (P[i] > 2.5) and (P[i] <= 3.5):
            a = 27.04
            b = 1490.75
            c = 1.18
        elif (P[i] > 3.5) and (P[i] <= 4.5):
            a = 31.90
            b = 1469.92
            c = 1.31
        elif (P[i] > 4.5):
            a = -5.01
            b = 1514.84
            c = -1.23

        delta_T[i] = (a * CO2_Melt[i]) + (b * np.log((1e2 - (c * CO2_Melt[i])) / 1e2))

    T_carbon_solidus = T_solidus - delta_T

    return T_carbon_solidus
