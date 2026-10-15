try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Section 1.6 Symbols used in EN 1996-1-2 (Structural fire design)

theta = Symbol(r"\theta", "Temperature in degrees Celsius")
t_fi_d = Symbol(r"t_{fi,d}", "Design value of fire resistance duration")
t_fi_req = Symbol(r"t_{fi,req}", "Required fire resistance duration (e.g. 30, 60, 90, 120, 240 min)")
gamma_M_fi = Symbol(r"\gamma_{M,fi}", "Partial factor for masonry in the fire situation (gamma_M,fi = 1.0)")

N_Ed_fi = Symbol(r"N_{Ed,fi}", "Design vertical load applied to masonry wall in the fire situation")
N_Rd_fi = Symbol(r"N_{Rd,fi}", "Design vertical load resistance of masonry wall in the fire situation")
alpha_fi = Symbol(r"\alpha_{fi}", "Reduction factor for design load in the fire situation (N_Ed,fi / N_Ed)")

t_min = Symbol(r"t_{min}", "Minimum thickness of masonry wall required for a specified fire resistance class")
h_ef = Symbol(r"h_{ef}", "Effective height of the wall in the fire situation")
