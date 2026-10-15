try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Symbols used in EN 1993-1-3

f_yb = Symbol(r"f_{yb}", "Basic yield strength of steel sheet material before cold forming")
f_ya = Symbol(r"f_{ya}", "Average yield strength of cold-formed cross-section after forming")
t_nom = Symbol(r"t", "Nominal steel sheet thickness")
t_cor = Symbol(r"t_{cor}", "Core metallic thickness excluding zinc and organic coatings")
b_eff = Symbol(r"b_{eff}", "Effective width of a compression plate element")
s_eff = Symbol(r"s_{eff}", "Effective width of an edge or intermediate stiffener")
k_sigma = Symbol(r"k_\sigma", "Plate buckling coefficient for normal stress")
chi_d = Symbol(r"\chi_d", "Reduction factor for distortional buckling")
F_b_Rd = Symbol(r"F_{b,Rd}", "Design bearing resistance of fasteners in thin gauge steel")
R_w_Rd = Symbol(r"R_{w,Rd}", "Design resistance of web to local transverse forces (web crippling)")
gamma_M0 = Symbol(r"\gamma_{M0}", "Partial safety factor for resistance of cold-formed cross-sections")
gamma_M1 = Symbol(r"\gamma_{M1}", "Partial safety factor for resistance of cold-formed members to instability")
gamma_M2 = Symbol(r"\gamma_{M2}", "Partial safety factor for resistance of connections")
