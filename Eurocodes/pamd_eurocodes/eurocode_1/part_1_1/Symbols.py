try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Latin upper case letters
A = Symbol(r"A", "Loaded area")
A_0 = Symbol(r"A_0", "Basic area")
Q_k = Symbol(r"Q_k", "Characteristic value of a variable concentrated load")

# Latin lower case letters
g_k = Symbol(r"g_k", "Weight per unit area, or weight per unit length")
n = Symbol(r"n", "Number of storeys")
q_k = Symbol(r"q_k", "Characteristic value of a uniformly distributed load, or line load")

# Greek lower case letters
alpha_A = Symbol(r"\alpha_A", "Reduction factor for loaded area")
alpha_n = Symbol(r"\alpha_n", "Reduction factor for number of storeys")
gamma = Symbol(r"\gamma", "Bulk weight density")
phi_dyn = Symbol(r"\varphi", "Dynamic magnification factor")
psi_0 = Symbol(r"\psi_0", "Factor for combination value of a variable action, see Table A1.1 of EN 1990")
phi_repose = Symbol(r"\phi", "Angle of repose (degrees)")
