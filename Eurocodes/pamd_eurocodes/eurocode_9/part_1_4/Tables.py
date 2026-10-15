"""Eurocode 9 - Part 1-4: Cold-formed structural sheeting - Tables.
EN 1999-1-4.
"""
try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange


# Table 2.1
partial_factors_cold_formed_sheeting = Table(
    ["Resistance type", "Symbol", "Recommended value"],
    [
        ["Resistance of cross-sections to yielding", "gamma_M0", 1.10],
        ["Resistance to member and panel buckling / web crippling", "gamma_M1", 1.10],
        ["Resistance of connection fasteners (screws, rivets)", "gamma_M2", 1.25]
    ],
    "Partial safety factors gamma_M for cold-formed aluminium sheeting (EN 1999-1-4 Clause 2)",
    "Applied in ultimate limit state design of profiled panels and fastening systems."
)

# Table 5.1
web_crippling_parameters = Table(
    ["Support condition / load application", "Bearing condition", "Coefficient k", "Empirical formula term"],
    [
        ["End support (reaction load)", "Stiff bearing s_s >= 40 mm", 0.075, "alpha_w * (1 - 0.1 * sqrt(r/t)) * (1 + 0.01 * (s_s/t))"],
        ["End support (reaction load)", "Flexible bearing (narrow flange)", 0.057, "alpha_w * (1 - 0.1 * sqrt(r/t)) * (1 + 0.007 * (s_s/t))"],
        ["Internal support (continuous beam)", "Stiff bearing s_s >= 60 mm", 0.150, "alpha_w * (1 - 0.1 * sqrt(r/t)) * (1 + 0.01 * (s_s/t))"],
        ["Interior load application", "Point load on profile span", 0.115, "alpha_w * (1 - 0.1 * sqrt(r/t)) * (1 + 0.008 * (s_s/t))"]
    ],
    "Parameters for local transverse resistance of webs to web crippling (EN 1999-1-4 Clause 6.1.7)",
    "Prevents crushing and crippling failure of thin aluminium profile webs under support reactions."
)

# Table 6.1
minimum_nominal_sheet_thickness = Table(
    ["Application / functional use", "Recommended minimum thickness t_min [mm]"],
    [
        ["Roof sheeting subjected to foot traffic maintenance loads", 0.70],
        ["Roof sheeting not accessible except for normal construction/repair", 0.60],
        ["Wall cladding and vertical facade panels", 0.50],
        ["Liners and interior ceiling panels", 0.40]
    ],
    "Recommended minimum design core thickness for aluminium profiled sheets (EN 1999-1-4 Clause 3)",
    "Ensures structural robustness against local denting, wind suction tearing, and walkability."
)
