try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Section 1.6 Symbols used in EN 1999-1-1 / ENV 1999-1-1 (General structural rules for aluminium)

# Material strengths and HAZ parameters
f_o = Symbol(r"f_o", "Characteristic 0.2% proof strength of aluminium alloy")
f_u = Symbol(r"f_u", "Characteristic ultimate tensile strength of aluminium alloy")
f_o_haz = Symbol(r"f_{o,haz}", "Characteristic 0.2% proof strength in the Heat-Affected Zone (HAZ) of a weld")
f_u_haz = Symbol(r"f_{u,haz}", "Characteristic ultimate tensile strength in the Heat-Affected Zone (HAZ)")
rho_o_haz = Symbol(r"\rho_{o,haz}", "Strength reduction factor for 0.2% proof strength in HAZ (rho_o_haz = f_{o,haz} / f_o)")
rho_u_haz = Symbol(r"\rho_{u,haz}", "Strength reduction factor for ultimate strength in HAZ (rho_u_haz = f_{u,haz} / f_u)")
b_haz = Symbol(r"b_{haz}", "Extent of the Heat-Affected Zone measured from the weld toe or centerline")

# Elastic & Physical Constants
E = Symbol(r"E", "Modulus of elasticity of aluminium (E = 70 000 MPa)")
G = Symbol(r"G", "Shear modulus of aluminium (G = 27 000 MPa)")
nu = Symbol(r"\nu", "Poisson's ratio of aluminium (nu = 0.3)")
alpha_T = Symbol(r"\alpha", "Linear thermal expansion coefficient of aluminium (alpha = 23 * 10^-6 K^-1)")
rho_al = Symbol(r"\rho", "Unit mass / density of aluminium (rho = 2700 kg/m^3)")

# Cross-section and Slenderness Parameters
A = Symbol(r"A", "Gross cross-sectional area")
A_eff = Symbol(r"A_{eff}", "Effective cross-sectional area taking into account local buckling and HAZ softening")
W_el = Symbol(r"W_{el}", "Elastic section modulus of gross cross-section")
W_pl = Symbol(r"W_{pl}", "Plastic section modulus of cross-section")
W_eff = Symbol(r"W_{eff}", "Effective section modulus accounting for plate local buckling and HAZ effects")
t_eff = Symbol(r"t_{eff}", "Effective thickness of slender plate element in Class 4 sections (t_eff = rho_c * t)")
beta_slend = Symbol(r"\beta", "Slenderness parameter of an element (beta = b / t)")
epsilon = Symbol(r"\varepsilon", "Material slenderness factor (epsilon = sqrt(250 / f_o))")

# Buckling & Stability Parameters
lambda_bar = Symbol(r"\bar{\lambda}", "Relative slenderness for flexural or lateral-torsional column buckling")
chi = Symbol(r"\chi", "Reduction factor for column flexural buckling")
chi_LT = Symbol(r"\chi_{LT}", "Reduction factor for lateral-torsional buckling of beams")
alpha_buckling = Symbol(r"\alpha", "Imperfection factor for column buckling curves (Class A: alpha=0.20; Class B: alpha=0.32)")
N_b_Rd = Symbol(r"N_{b,Rd}", "Design buckling resistance of a compression member")
M_b_Rd = Symbol(r"M_{b,Rd}", "Design buckling resistance moment of a laterally unrestrained beam")

# Partial Safety Factors
gamma_M0 = Symbol(r"\gamma_{M0}", "Partial factor for resistance of cross-sections to yielding (recommended 1.10)")
gamma_M1 = Symbol(r"\gamma_{M1}", "Partial factor for resistance of members to buckling (recommended 1.10)")
gamma_M2 = Symbol(r"\gamma_{M2}", "Partial factor for resistance of cross-sections to ultimate tensile fracture (recommended 1.25)")
gamma_Mw = Symbol(r"\gamma_{Mw}", "Partial factor for resistance of welded connections (recommended 1.25)")
