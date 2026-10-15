try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Section 1.5 Symbols used in EN 1993-1-8

e_1 = Symbol(r"e_1", "End distance from fastener hole centre to adjacent end in direction of load transfer")
e_2 = Symbol(r"e_2", "Edge distance from fastener hole centre to adjacent edge perpendicular to load transfer")
p_1 = Symbol(r"p_1", "Spacing between fastener centres in direction of load transfer")
p_2 = Symbol(r"p_2", "Spacing between fastener centres perpendicular to direction of load transfer")
d_0 = Symbol(r"d_0", "Hole diameter for bolt or rivet")
A_s = Symbol(r"A_s", "Tensile stress area of bolt")
F_v_Rd = Symbol(r"F_{v,Rd}", "Design shear resistance per shear plane of a bolt")
F_b_Rd = Symbol(r"F_{b,Rd}", "Design bearing resistance of a bolt or plate")
F_t_Rd = Symbol(r"F_{t,Rd}", "Design tension resistance of a bolt")
B_p_Rd = Symbol(r"B_{p,Rd}", "Design punching shear resistance of bolt head or nut")
F_s_Rd = Symbol(r"F_{s,Rd}", "Design slip resistance of a preloaded bolt at ultimate limit state")
S_j = Symbol(r"S_j", "Rotational stiffness of a joint")
S_j_ini = Symbol(r"S_{j,ini}", "Initial rotational stiffness of a joint")
V_wp_Rd = Symbol(r"V_{wp,Rd}", "Design plastic shear resistance of a column web panel")
z_arm = Symbol(r"z", "Lever arm between tension and compression centres in a moment joint")
mu_slip = Symbol(r"\mu", "Slip factor between friction surfaces")
beta_w = Symbol(r"\beta_w", "Correlation factor for fillet welds according to steel grade")
gamma_M2 = Symbol(r"\gamma_{M2}", "Partial safety factor for resistance of bolts, rivets, pins, welds and plates in bearing")
gamma_M3 = Symbol(r"\gamma_{M3}", "Partial safety factor for slip resistance of preloaded bolts at ultimate limit state")
