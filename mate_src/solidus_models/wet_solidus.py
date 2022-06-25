#!/usr/bin/env python3

import numpy as np

R_const = 8.3144621

def Hirschmann2009_WetPeridotite(T, T_solidus, P, Melt_Mass_Frac, H2O, D_per_melt, cpx_frac):

    H2O = H2O / 1e4

    Melt_H2O = H2O / (Melt_Mass_Frac + ((1.0 - Melt_Mass_Frac) * D_per_melt))

    M = 59.0
    dS = 0.4

    X_h2o_melt = (2 * M * (Melt_H2O / 1e2)) /\
        (18.02 + ((Melt_H2O / 1e2) * ((2 * M) - 18.02)))

    T_solidus = T_solidus / (1 - ((R_const / M * dS) * np.log(1 - X_h2o_melt)))

    return T_solidus
