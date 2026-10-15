try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Section 1.6 Symbols used in EN 1995-2 (Bridges)

L_bridge = Symbol(r"L", "Span length of the bridge girder or deck")
b_deck = Symbol(r"b_{deck}", "Width of the timber bridge deck")
sigma_p = Symbol(r"\sigma_p", "Transverse prestress compressive stress in stress-laminated timber decks")
sigma_p_min = Symbol(r"\sigma_{p,min}", "Minimum residual prestress compressive stress to prevent joint separation")
Delta_sigma_p = Symbol(r"\Delta\sigma_p", "Loss of prestress due to timber creep, moisture fluctuations, and tendon relaxation")

k_mod_bridge = Symbol(r"k_{mod}", "Modification factor for load duration and moisture in Service Class 3 bridge environments")
k_def_bridge = Symbol(r"k_{def}", "Deformation factor for creep evaluation in bridge conditions")
gamma_M_bridge = Symbol(r"\gamma_M", "Partial factor for timber material properties in bridge structures")

a_s = Symbol(r"a_s", "Center-to-center spacing of transverse prestressing tendons")
f_c_90_d = Symbol(r"f_{c,90,d}", "Design compressive strength perpendicular to grain under anchor plates")
u_net_freq = Symbol(r"u_{net,freq}", "Net deflection under the frequent combination of bridge traffic actions")
V_bridge = Symbol(r"V_d", "Design vertical shear force in composite timber bridge deck or girder")
M_bridge = Symbol(r"M_d", "Design bending moment on the longitudinal bridge superstructure")
