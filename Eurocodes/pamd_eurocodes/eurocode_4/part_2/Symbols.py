try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Section 1.6 Symbols used in EN 1994-2 (Composite bridges)

L_eff = Symbol(r"L_{eff}", "Effective span length for composite bridge girders")
b_eff = Symbol(r"b_{eff}", "Total effective width of concrete flange in composite bridge deck")
b_0 = Symbol(r"b_0", "Distance between outer rows of shear connectors or between web centerlines")
b_i = Symbol(r"b_i", "Geometric width of concrete flange cantilever or interior bay")
beta = Symbol(r"\beta", "Effective width factor accounting for shear lag in bridge deck flanges")

Delta_tau_R = Symbol(r"\Delta\tau_R", "Fatigue shear strength of headed stud connectors")
Delta_tau_E = Symbol(r"\Delta\tau_E", "Equivalent constant amplitude shear stress range in connectors")
Delta_sigma_c = Symbol(r"\Delta\sigma_c", "Reference fatigue strength of detail at 2 * 10^6 cycles")

tau_Ed = Symbol(r"\tau_{Ed}", "Design longitudinal shear stress in bridge flange")
v_Ed = Symbol(r"v_{Ed}", "Design longitudinal shear force per unit length")
V_Ed = Symbol(r"V_{Ed}", "Design vertical shear force in composite bridge girder")
M_Ed = Symbol(r"M_{Ed}", "Design bending moment on composite bridge girder")
N_Ed = Symbol(r"N_{Ed}", "Design axial force in composite bridge deck or girder")

gamma_Mf = Symbol(r"\gamma_{Mf}", "Partial factor for fatigue strength of shear connection in bridges")
gamma_V = Symbol(r"\gamma_V", "Partial factor for headed stud shear connectors in composite bridges")
gamma_a = Symbol(r"\gamma_a", "Partial factor for structural steel in bridge construction")
alpha_st = Symbol(r"\alpha_{st}", "Stiffness ratio between concrete deck and structural steel girder")
k_v = Symbol(r"k_v", "Shear lag interaction factor for wide bridge flanges")
w_max = Symbol(r"w_{max}", "Maximum allowable crack width in composite bridge concrete decks")
