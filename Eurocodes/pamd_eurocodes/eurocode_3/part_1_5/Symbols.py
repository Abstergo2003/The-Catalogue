try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Section 1.4 Symbols used in EN 1993-1-5

A_eff = Symbol(r"A_{eff}", "Effective cross-sectional area taking into account plate buckling and shear lag")
b_eff = Symbol(r"b_{eff}", "Effective width of plate element for plate buckling or shear lag")
beta_shear_lag = Symbol(r"\beta", "Effective width factor for elastic shear lag")
kappa_param = Symbol(r"\kappa", "Non-dimensional parameter for shear lag = alpha_0 * b_0 / L_e")
alpha_0 = Symbol(r"\alpha_0", "Stiffener parameter for shear lag = sqrt(1 + A_sl / (b_0 * t))")
A_sl = Symbol(r"A_{s\ell}", "Sum of cross-sectional areas of all longitudinal stiffeners within width b_0")
k_tau = Symbol(r"k_\tau", "Shear buckling coefficient")
k_sigma = Symbol(r"k_\sigma", "Plate buckling coefficient for normal stress")
lambda_bar_p = Symbol(r"\bar{\lambda}_p", "Plate slenderness for direct stresses")
lambda_bar_w = Symbol(r"\bar{\lambda}_w", "Web slenderness for shear buckling")
chi_w = Symbol(r"\chi_w", "Reduction factor for web shear buckling")
V_bw_Rd = Symbol(r"V_{bw,Rd}", "Design shear buckling resistance of a web")
