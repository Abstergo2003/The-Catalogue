"""Eurocode 8 - Part 5: Foundations, retaining structures and geotechnical aspects - Tables.
EN 1998-5 (2004).
"""
try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange


# Table 4.1
soil_damping_and_modulus_reduction = Table(
    ["Ground acceleration ratio alpha * S", "Damping ratio xi", "Velocity ratio vs / vs,max", "Modulus ratio G / Gmax"],
    [
        [0.10, 0.03, "0.90 (+/- 0.07)", "0.80 (+/- 0.10)"],
        [0.20, 0.06, "0.70 (+/- 0.15)", "0.50 (+/- 0.20)"],
        [0.30, 0.10, "0.60 (+/- 0.15)", "0.36 (+/- 0.20)"]
    ],
    "Average soil damping ratios and average reduction factors for vs and G within 20 m depth (EN 1998-5 Table 4.1)",
    "Applied for equivalent linear soil-structure interaction and site response analyses when specific tests are unavailable."
)

# Table 7.1
retaining_structure_factor_r = Table(
    ["Type of retaining structure", "Factor r", "Permissible displacement dr"],
    [
        ["Free gravity walls that can accept large displacement", 2.0, "dr <= 300 * alpha * S (mm)"],
        ["Free gravity walls that can accept moderate displacement", 1.5, "dr <= 200 * alpha * S (mm)"],
        ["Flexural RC walls, anchored/braced walls, walls on vertical piles, basement walls, bridge abutments", 1.0, "Near zero permanent displacement"]
    ],
    "Values of factor r for calculation of horizontal seismic coefficient kh = alpha * S / r (EN 1998-5 Table 7.1)",
    "Accounts for wall ductility and tolerable permanent displacement under seismic lateral earth pressure."
)

# Annex A Table
topographic_amplification_factors = Table(
    ["Topographic feature", "Average slope angle", "Recommended amplification factor ST"],
    [
        ["Flat terrain or gentle slope", "< 15 deg", 1.0],
        ["Isolated cliffs and slopes (near top edge)", "> 15 deg", "ST >= 1.2"],
        ["Ridges with crest width significantly less than base width", "15 deg - 30 deg", "ST >= 1.2"],
        ["Steep ridges with narrow crest", "> 30 deg", "ST >= 1.4"],
        ["Presence of loose surface layer", "Any", "Increase base ST by at least 20%"]
    ],
    "Topographic amplification factor ST for ground slope stability and crest structures (EN 1998-5 Annex A)",
    "Multiplies the ordinates of the elastic response spectrum to account for wave focusing at geometric surface features."
)

# Table F.2
bearing_capacity_model_partial_factors = Table(
    ["Soil type / condition", "Model partial factor gamma_Rd"],
    [
        ["Medium-dense to dense sand", 1.00],
        ["Loose dry sand", 1.15],
        ["Loose saturated sand", 1.50],
        ["Non-sensitive clay", 1.00],
        ["Sensitive clay", 1.15]
    ],
    "Values of the model partial factor gamma_Rd for foundation seismic bearing capacity (EN 1998-5 Table F.2)",
    "Used in the general non-linear interaction verification formula for shallow foundations under seismic actions."
)
