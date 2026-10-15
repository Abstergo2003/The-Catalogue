"""Eurocode 9 - Part 1-5: Shell structures - Tables.
EN 1999-1-5.
"""
try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange


# Table 2.1
partial_factors_shells = Table(
    ["Resistance type", "Symbol", "Recommended value"],
    [
        ["Resistance of shell wall to plastic yield limit state", "gamma_M0", 1.10],
        ["Resistance of shell wall to buckling instability", "gamma_M1", 1.10],
        ["Resistance of welded or bolted joints in shell", "gamma_M2", 1.25]
    ],
    "Partial safety factors gamma_M for aluminium shell structures (EN 1999-1-5 Clause 2)",
    "Applied in ultimate and stability limit state verifications of thin aluminium shells."
)

# Table 3.1
tolerance_quality_classes = Table(
    ["Tolerance quality class", "Description / quality standard", "Dimple imperfection parameter U_0x", "Out-of-roundness tolerance U_r"],
    [
        ["Class A", "Excellent quality (precision fabrication, aerospace / specialized vessels)", 0.010, 0.005],
        ["Class B", "High quality (carefully controlled shop fabrication)", 0.016, 0.010],
        ["Class C", "Normal quality (standard commercial tank and silo construction)", 0.025, 0.015]
    ],
    "Fabrication tolerance quality classes and initial imperfection parameters (EN 1999-1-5 Table 5.1)",
    "Defines the magnitude of initial geometric imperfections Delta_w_k governing shell buckling capacity."
)

# Table 4.1
knock_down_imperfection_factors = Table(
    ["Stress state / buckling mode", "Quality Class A alpha", "Quality Class B alpha", "Quality Class C alpha"],
    [
        ["Meridional (axial) compression alpha_x", "0.83 / (1 + 0.01 * (r/t))", "0.70 / (1 + 0.014 * (r/t))", "0.55 / (1 + 0.02 * (r/t))"],
        ["Circumferential (hoop) compression alpha_theta", 0.75, 0.65, 0.50],
        ["In-plane shear buckling alpha_tau", 0.80, 0.70, 0.60]
    ],
    "Elastic knock-down imperfection reduction factors alpha for shell buckling (EN 1999-1-5 Section 8)",
    "Reduces classical linear critical buckling stresses to account for severe post-buckling imperfection sensitivity."
)
