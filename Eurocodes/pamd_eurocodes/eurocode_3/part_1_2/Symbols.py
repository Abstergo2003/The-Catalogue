try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Section 1.6 Symbols used in EN 1993-1-2

A_m = Symbol(r"A_m", "Surface area of a member per unit length")
A_p = Symbol(r"A_p", "Area of the inner surface of the fire protection material per unit length")
V_vol = Symbol(r"V", "Volume of a member per unit length")
section_factor_unprotected = Symbol(r"A_m/V", "Section factor for unprotected steel members (m^-1)")
section_factor_protected = Symbol(r"A_p/V", "Section factor for steel members insulated by fire protection material (m^-1)")
c_a = Symbol(r"c_a", "Specific heat of steel (J/kgK)")
d_p = Symbol(r"d_p", "Thickness of fire protection material")
E_a = Symbol(r"E_a", "Modulus of elasticity of steel for normal temperature design")
E_a_theta = Symbol(r"E_{a,\theta}", "Slope of linear elastic range for steel at elevated temperature theta_a")
E_d_fi = Symbol(r"E_{d,fi}", "Design effect of actions in the fire situation")
f_p_theta = Symbol(r"f_{p,\theta}", "Proportional limit for steel at elevated temperature theta_a")
f_y_theta = Symbol(r"f_{y,\theta}", "Effective yield strength of steel at elevated temperature theta_a")
k_theta = Symbol(r"k_\theta", "Relative value of a strength or deformation property of steel at elevated temperature theta_a")
theta_a = Symbol(r"\theta_a", "Steel temperature (deg C)")
theta_a_cr = Symbol(r"\theta_{a,cr}", "Critical steel temperature (deg C)")
h_net_d = Symbol(r"\dot{h}_{net,d}", "Design value of net heat flux per unit area")
eta_fi = Symbol(r"\eta_{fi}", "Reduction factor for design load level in the fire situation")
mu_0 = Symbol(r"\mu_0", "Degree of utilisation at the start of the fire")
gamma_M_fi = Symbol(r"\gamma_{M,fi}", "Partial safety factor for steel in the fire situation (recommended 1.0)")
