try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Section 1.6 Symbols used in EN 1995-1-2 (Structural fire design)

# Charring parameters
beta_0 = Symbol(r"\beta_0", "One-dimensional design charring rate under standard fire exposure (mm/min)")
beta_n = Symbol(r"\beta_n", "Notional design charring rate incorporating corner roundings and fissures (mm/min)")
beta_par = Symbol(r"\beta_{par}", "Charring rate during heating phase of a parametric fire curve")

d_char_0 = Symbol(r"d_{char,0}", "One-dimensional charring depth (d_char,0 = beta_0 * t)")
d_char_n = Symbol(r"d_{char,n}", "Notional charring depth (d_char,n = beta_n * t)")
d_ef = Symbol(r"d_{ef}", "Effective charring depth (d_ef = d_char,n + k_0 * d_0)")
d_0 = Symbol(r"d_0", "Depth of zero-strength layer (d_0 = 7 mm)")

# Strength and modification factors in fire
k_fi = Symbol(r"k_{fi}", "Factor converting 5th percentile normal temperature property to 20th percentile fire property")
k_mod_fi = Symbol(r"k_{mod,fi}", "Modification factor for timber in the fire situation")
k_0 = Symbol(r"k_0", "Coefficient for the build-up of the zero-strength layer")
f_d_fi = Symbol(r"f_{d,fi}", "Design strength of timber in the fire situation")
f_20 = Symbol(r"f_{20}", "20th percentile value of strength at ambient temperature (f_20 = k_fi * f_k)")
E_20 = Symbol(r"E_{20}", "20th percentile value of modulus of elasticity at ambient temperature (E_20 = k_fi * E_05)")
gamma_M_fi = Symbol(r"\gamma_{M,fi}", "Partial factor for timber material properties in fire (gamma_M,fi = 1.0)")

# Cross-section and time parameters
A_r = Symbol(r"A_r", "Area of residual cross-section")
W_ef = Symbol(r"W_{ef}", "Section modulus of effective cross-section")
t_ch = Symbol(r"t_{ch}", "Time of start of charring of protected members")
t_f = Symbol(r"t_f", "Failure time of fire protective cladding or insulation")
t_d_fi = Symbol(r"t_{d,fi}", "Design fire resistance duration of an unprotected timber joint")
eta_fi = Symbol(r"\eta_{fi}", "Reduction factor for design load in fire situation")
