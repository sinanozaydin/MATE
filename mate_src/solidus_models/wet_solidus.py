#!/usr/bin/env python3

import numpy as np

R_const = 8.3144621

def Hirschmann2009_WetPeridotite(method, T, T_solidus, P, Melt_Mass_Frac, H2O, D_per_melt, cpx_frac):

    H2O = H2O / 1e4
    
    M = 59.0
    dS = 0.4

    #Melt_H2O = H2O / (Melt_Mass_Frac + ((1.0 - Melt_Mass_Frac) * D_per_melt))
    T_solidus_wet = np.zeros(len(T))
    if method == 'array':
        Melt_H2O = np.zeros(len(T_solidus))
        for i in range(0,len(Melt_Mass_Frac)):
            if Melt_Mass_Frac[i] == 0:
                Melt_H2O[i] = 0.0
                T_solidus_wet[i] = T_solidus[i]
            else:
                Melt_H2O[i] = H2O[i] / (Melt_Mass_Frac[i] + ((1.0 - Melt_Mass_Frac[i]) * D_per_melt[i]))
                TotalMoles  = (Melt_H2O[i] / 17.007) + ((100 - Melt_H2O[i]) / 92.0831)
                X_h2o_melt = (Melt_H2O[i] / 17.007) / TotalMoles
                T_solidus_wet[i] = T_solidus[i] / (1 - ((R_const / (M * dS)) * np.log(1 - X_h2o_melt)))
                
    elif method == 'index':
        if Melt_Mass_Frac == 0:
            Melt_H2O = 0.0
            T_solidus_wet = T_solidus
        else:
            Melt_H2O = H2O / (Melt_Mass_Frac + ((1.0 - Melt_Mass_Frac) * D_per_melt))
            TotalMoles  = (Melt_H2O / 17.007) + ((100 - Melt_H2O) / 92.0831)
            X_h2o_melt = (Melt_H2O / 17.007) / TotalMoles
            T_solidus_wet = T_solidus / (1 - ((R_const / (M * dS)) * np.log(1 - X_h2o_melt)))
    
    return T_solidus_wet
