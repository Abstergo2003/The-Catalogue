"""Eurocode 9 - Part 1-3: Structures susceptible to fatigue - Tables.
EN 1999-1-3 / ENV 1999-2.
"""
try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange


# Table 3.1
fatigue_partial_safety_factors = Table(
    ["Assessment method", "Low consequence of failure", "High consequence of failure"],
    [
        ["Damage tolerant method", 1.00, 1.15],
        ["Safe life method", 1.15, 1.35]
    ],
    "Recommended values for partial factor gamma_Mf for fatigue strength (EN 1999-1-3 Table 2.1)",
    "Applied to detail category stress ranges depending on inspectability and structural consequence of failure."
)

# Table 5.1
detail_categories_plain_and_bolted = Table(
    ["Constructional detail description", "Detail category Delta_sigma_c [MPa]", "Inverse slope m1"],
    [
        ["Continuously extruded plain profile, smooth rolled edges, no notches", 100, 4.0],
        ["Plain parent metal with ground flame-cut edges or drilled holes", 80, 4.0],
        ["Preloaded high-strength friction-grip bolted connection (slip resistant)", 71, 4.0],
        ["Non-preloaded bolted connection with fitted bolts in reamed holes", 63, 4.0],
        ["Standard clearance bolted bearing-type connection (double shear)", 56, 4.0]
    ],
    "Fatigue detail categories for non-welded aluminium details (EN 1999-1-3 Table J.1)",
    "Characteristic fatigue reference strength at 2 * 10^6 cycles for plain material and mechanical fasteners."
)

# Table 5.2
detail_categories_welded = Table(
    ["Welded detail description", "Detail category Delta_sigma_c [MPa]", "Inverse slope m1"],
    [
        ["Full penetration transverse butt weld, ground flush to plate surface", 50, 3.5],
        ["Full penetration transverse butt weld, as-welded with weld overfill", 45, 3.5],
        ["Continuous longitudinal automatic weld without stops and starts", 40, 3.5],
        ["Transverse non-load-carrying attachment fillet weld (length < 50 mm)", 36, 3.0],
        ["Transverse load-carrying cruciform or tee fillet-welded joint", 28, 3.0],
        ["Longitudinal load-carrying lap joint with fillet welds", 20, 3.0]
    ],
    "Fatigue detail categories for welded aluminium joints (EN 1999-1-3 Table J.2 - J.4)",
    "Characteristic fatigue reference strength at 2 * 10^6 cycles for fusion welded connections in aluminium alloys."
)

# Table 6.1
sn_curve_slope_parameters = Table(
    ["Stress cycle range", "Endurance cycles N", "Inverse slope m", "Fatigue limit relation"],
    [
        ["High cyclic stresses", "N <= 5 * 10^6", "m1 (typically 3.0 to 4.0)", "Delta_sigma^m1 * N = Delta_sigma_c^m1 * 2*10^6"],
        ["Intermediate variable amplitude stresses", "5 * 10^6 < N <= 10^8", "m2 = m1 + 2 (typically 5.0 to 6.0)", "Delta_sigma^m2 * N = Delta_sigma_D^m2 * 5*10^6"],
        ["Low non-damaging stress cycles", "N > 10^8", "Infinite (horizontal)", "Cycles below cut-off limit Delta_sigma_L produce no damage"]
    ],
    "Standard parameters and slopes defining the bilinear S-N fatigue curves (EN 1999-1-3 Clause 6.1)",
    "Governs cumulative damage calculations under both constant and variable amplitude cyclic stress spectra."
)
