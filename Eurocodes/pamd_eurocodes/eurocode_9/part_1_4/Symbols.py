try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Section 1.6 Symbols used in EN 1999-1-4 (Cold-formed structural sheeting)

# Profile Geometry and Dimensions
b = Symbol(r"b", "Nominal flat width of a plane element (flange or web)")
b_eff = Symbol(r"b_{eff}", "Effective width of compression flange or web taking local buckling into account")
t = Symbol(r"t", "Nominal core thickness of the profiled aluminium sheet")
h_w = Symbol(r"h_w", "Web depth between flange flat portions measured along the web plane")
s_s = Symbol(r"s_s", "Nominal length of stiff bearing support")

# Resistances & Buckling Factors
R_w_Rd = Symbol(r"R_{w,Rd}", "Design resistance of web to local transverse force (web crippling)")
M_c_Rd = Symbol(r"M_{c,Rd}", "Design bending moment resistance of the effective profiled cross-section")
lambda_bar_dp = Symbol(r"\bar{\lambda}_{dp}", "Relative slenderness for distortional buckling of flange stiffeners")
chi_d = Symbol(r"\chi_d", "Reduction factor for distortional buckling of stiffened elements")

# Partial Safety Factors
gamma_M0 = Symbol(r"\gamma_{M0}", "Partial factor for resistance of cross-sections (recommended 1.10)")
gamma_M1 = Symbol(r"\gamma_{M1}", "Partial factor for resistance to buckling and stability failure (recommended 1.10)")
gamma_M2 = Symbol(r"\gamma_{M2}", "Partial factor for resistance of connection fasteners (recommended 1.25)")
