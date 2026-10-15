try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Section 1.7 Special symbols used in Part 3 of Eurocode 2

# Latin upper case symbols
R_ax = Symbol(r"R_{ax}", "Factor defining the degree of external axial restraint provided by elements attached to the element considered")
R_m = Symbol(r"R_m", "Factor defining the degree of moment restraint provided by elements attached to the element considered")

# Latin lower case symbols
f_ctx = Symbol(r"f_{ctx}", "Tensile strength of concrete, however defined")
f_ckT = Symbol(r"f_{ckT}", "Characteristic compressive strength of the concrete modified to take account of temperature")
h_D = Symbol(r"h_D", "Hydraulic head or hydrostatic pressure acting on the containing structure")
w_k1 = Symbol(r"w_{k1}", "Limiting crack width for Tightness Class 1 structures")
x_min = Symbol(r"x_{min}", "Minimum depth of concrete compression zone to avoid through-thickness cracking")

# Greek symbols
epsilon_av = Symbol(r"\varepsilon_{av}", "Average strain in the element")
epsilon_az = Symbol(r"\varepsilon_{az}", "Actual strain at level z")
epsilon_iz = Symbol(r"\varepsilon_{iz}", "Imposed intrinsic strain at level z")
epsilon_Tr = Symbol(r"\varepsilon_{Tr}", "Transitional thermal strain")
epsilon_Th = Symbol(r"\varepsilon_{Th}", "Free thermal strain in the concrete")
