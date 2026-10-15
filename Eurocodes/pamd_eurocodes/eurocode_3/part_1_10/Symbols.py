try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Section 1.4 Symbols used in EN 1993-1-10

T_Ed = Symbol(r"T_{Ed}", "Design service temperature for brittle fracture assessment")
T_md = Symbol(r"T_{md}", "Lowest expected ambient air temperature")
Delta_T_r = Symbol(r"\Delta T_r", "Temperature adjustment for radiation loss")
Delta_T_eps = Symbol(r"\Delta T_{\dot{\varepsilon}}", "Temperature adjustment for strain rate")
sigma_Ed = Symbol(r"\sigma_{Ed}", "Maximum tensile stress in element under characteristic load combination")
t_max = Symbol(r"t_{max}", "Maximum permissible element thickness to avoid brittle fracture")
Z_Ed = Symbol(r"Z_{Ed}", "Required design through-thickness reduction of area to avoid lamellar tearing")
Z_Rd = Symbol(r"Z_{Rd}", "Design through-thickness resistance class according to EN 10164 (Z15, Z25, Z35)")
