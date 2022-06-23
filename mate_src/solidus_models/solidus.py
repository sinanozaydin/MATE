#!/usr/bin/env python3

import numpy as np

def Hirschmann2009_Dry(T, P, H2O, D_per_melt, cpx_frac):

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

def Katz2003_Wet(T, P, H2O, D_per_melt, cpx_frac):

    import warnings
    from scipy.optimize import root

    def X_H2O(h2obulk, F):

        return h2obulk/(D_per_melt + F*(1.0 - D_per_melt))

    def delta_T(X):

        return 43.0*X**0.75

    def F_dry():

        F_cpx_out = cpx_frac/R_cpx
        T_cpx_out = F_cpx_out**(1.0/1.5) * (T_liquidus_lherz - T_solidus) + T_solidus

        with warnings.catch_warnings():
            warnings.simplefilter('ignore', RuntimeWarning)
            F_opx = F_cpx_out + (1.0 - F_cpx_out)*((T - T_cpx_out)/(T_liquidus - T_cpx_out))**1.5
            F_cpx = ((T - T_solidus)/(T_liquidus_lherz - T_solidus))**1.5

        F = np.copy(F_cpx)
        F[F > F_cpx_out] = F_opx[F > F_cpx_out]
        return F

    def F_wet(T_solidus, T_liquidus, T_liquidus_lherz):

        # Evaluate anhydrous melting
        F_cpx_out = cpx_frac/R_cpx
        F_opx = F_dry()

        delT_sat = delta_T(X_h2o_sat_melt)

        def F_iter(F):

            F[np.isnan(F)] = 0.0
            h2o_i = X_H2O(H2O, F)

            delT = delta_T(h2o_i)
            delT = np.minimum(delT, delT_sat)
            delT = np.clip(delT, 0, 1e99)

            with warnings.catch_warnings():
                warnings.simplefilter('ignore', RuntimeWarning)
                F_new = ((T - (T_solidus - delT))/(T_liquidus_lherz - T_solidus))**1.5

            F_new[np.isnan(F_new)] = 0

            return F_new - F

        sol = root(F_iter, x0=F_opx, method='anderson')
        F = sol.x

        h2o_i = X_H2O(H2O, F)

        delT = delta_T(h2o_i)
        delT = np.minimum(delT, delT_sat)
        delT = np.clip(delT, 0, 1e99)

        T_solidus = T_solidus - delT
        T_liquidus = T_liquidus - delT
        T_liquidus_lherz  = T_liquidus_lherz - delT

        T_cpx_out = F_cpx_out**(1.0/1.5) * (T_liquidus_lherz - T_solidus) + T_solidus

        with warnings.catch_warnings():
            warnings.simplefilter('ignore', RuntimeWarning)
            F_opx = F_cpx_out + (1.0 - F_cpx_out)*((T - T_cpx_out)/(T_liquidus - T_cpx_out))**1.5

        F[F > F_cpx_out] = F_opx[F > F_cpx_out]
        return F, T_solidus

    H2O = H2O * 1e-4

    T_solidus = 1085.7 + (132.9*P) - (5.1*P**2)
    T_liquidus_lherz = 1475.0 + (80.0*P) - (3.2*P**2)
    T_liquidus = 1780.0 + (45.0*P) - (2.0*P**2)

    R_cpx = 0.5 * (0.08 * P)

    X_h2o_sat_melt = (12.0*P**0.6) + (1.0*P)

    if np.mean(H2O) == 0.0:
        F = F_dry()
    else:
        F, T_solidus = F_wet(T_solidus,T_liquidus,T_liquidus_lherz)

    return T_solidus, F
