try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Section 1.6 Symbols used in EN 1997-1 (General rules)

# Latin upper case letters
A_prime = Symbol(r"A'", "Effective base area of a spread foundation (A' = b' * l')")
B_prime = Symbol(r"b'", "Effective width of a foundation (b' = b - 2*e_B)")
L_prime = Symbol(r"l'", "Effective length of a foundation (l' = l - 2*e_L)")
E_d = Symbol(r"E_d", "Design value of effect of actions")
F_d = Symbol(r"F_d", "Design value of an action")
F_k = Symbol(r"F_k", "Characteristic value of an action")
G_d = Symbol(r"G_d", "Design value of permanent action")
H_d = Symbol(r"H_d", "Design horizontal load or component parallel to foundation base")
N_c = Symbol(r"N_c", "Bearing capacity factor related to cohesion")
N_q = Symbol(r"N_q", "Bearing capacity factor related to overburden pressure")
N_gamma = Symbol(r"N_\gamma", "Bearing capacity factor related to soil self-weight")
Q_d = Symbol(r"Q_d", "Design value of variable action")
R_d = Symbol(r"R_d", "Design value of resistance to an action")
R_k = Symbol(r"R_k", "Characteristic value of resistance to an action")
R_v_d = Symbol(r"R_{v,d}", "Design bearing resistance of foundation normal to base")
R_h_d = Symbol(r"R_{h,d}", "Design sliding resistance of foundation parallel to base")
V_d = Symbol(r"V_d", "Design vertical load or component normal to foundation base")

# Latin lower case letters
b = Symbol(r"b", "Width of foundation")
c_prime = Symbol(r"c'", "Cohesion intercept in terms of effective stress")
c_u = Symbol(r"c_u", "Undrained shear strength of soil")
d = Symbol(r"d", "Depth of embedment of foundation base")
e = Symbol(r"e", "Eccentricity of resultant vertical action")
l = Symbol(r"l", "Length of foundation")
q_prime = Symbol(r"q'", "Effective overburden pressure at level of foundation base")
q_u = Symbol(r"q_u", "Unconfined compressive strength of rock or cohesive soil")
s = Symbol(r"s", "Settlement of foundation")
s_0 = Symbol(r"s_0", "Immediate elastic settlement")
s_1 = Symbol(r"s_1", "Primary consolidation settlement")
s_2 = Symbol(r"s_2", "Secondary creep settlement")
u = Symbol(r"u", "Pore water pressure")

# Greek letters
gamma_soil = Symbol(r"\gamma", "Total weight density of ground")
gamma_prime = Symbol(r"\gamma'", "Effective (submerged) weight density of ground")
gamma_F = Symbol(r"\gamma_F", "Partial factor for an action")
gamma_M = Symbol(r"\gamma_M", "Partial factor for a ground material property")
gamma_R = Symbol(r"\gamma_R", "Partial factor for a resistance")
gamma_Rv = Symbol(r"\gamma_{R,v}", "Partial factor for bearing resistance")
gamma_Rh = Symbol(r"\gamma_{R,h}", "Partial factor for sliding resistance")
gamma_b = Symbol(r"\gamma_b", "Partial factor for base resistance of a pile")
gamma_s = Symbol(r"\gamma_s", "Partial factor for shaft resistance of a pile")
gamma_t = Symbol(r"\gamma_t", "Partial factor for total/combined compression resistance of a pile")
phi_prime = Symbol(r"\phi'", "Angle of shearing resistance in terms of effective stress")
delta_friction = Symbol(r"\delta", "Structure-ground interface friction angle")
sigma_prime = Symbol(r"\sigma'", "Effective normal stress")
sigma_total = Symbol(r"\sigma", "Total normal stress")
tau_shear = Symbol(r"\tau", "Shear stress")
xi = Symbol(r"\xi", "Correlation factor to derive characteristic values from pile load tests")
