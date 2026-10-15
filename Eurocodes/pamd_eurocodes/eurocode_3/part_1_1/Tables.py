try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 3.1
nominal_values_of_yield_and_ultimate_strength_for_structural_steel = Table(
    [
        "Standard and steel grade",
        r"$f_y$ ($t \le 40$ mm) [N/mm2]",
        r"$f_u$ ($t \le 40$ mm) [N/mm2]",
        r"$f_y$ ($40 < t \le 100$ mm) [N/mm2]",
        r"$f_u$ ($40 < t \le 100$ mm) [N/mm2]"
    ],
    [
        ["EN 10025: Fe 360 / S 235", 235, 360, 215, 340],
        ["EN 10025: Fe 430 / S 275", 275, 430, 255, 410],
        ["EN 10025: Fe 510 / S 355", 355, 510, 335, 490],
        ["prEN 10113: Fe E 275 / S 275 N/NL", 275, 390, 255, 370],
        ["prEN 10113: Fe E 355 / S 355 N/NL", 355, 490, 335, 470],
        ["EN 10025-6: S 420", 420, 520, 390, 520],
        ["EN 10025-6: S 460", 460, 540, 430, 540]
    ],
    "Nominal values of yield strength fy and ultimate tensile strength fu for structural steel",
    "t is the nominal thickness of the element."
)

# Table 3.3
nominal_values_of_yield_and_ultimate_strength_for_bolts = Table(
    ["Bolt grade", r"$f_{yb}$ [N/mm2]", r"$f_{ub}$ [N/mm2]"],
    [
        ["4.6", 240, 400],
        ["4.8", 320, 400],
        ["5.6", 300, 500],
        ["5.8", 400, 500],
        ["6.8", 480, 600],
        ["8.8", 640, 800],
        ["10.9", 900, 1000]
    ],
    "Nominal values of yield strength fyb and ultimate tensile strength fub for bolts",
    "Bolts of grades lower than 4.6 or higher than 10.9 shall not be used without test verification."
)

# Table 4.1
recommended_limiting_values_for_vertical_deflections = Table(
    ["Conditions", r"Limit $\delta_{max}$", r"Limit $\delta_2$"],
    [
        ["Roofs generally", "L/200", "L/250"],
        ["Roofs frequently carrying personnel other than for maintenance", "L/250", "L/300"],
        ["Floors generally", "L/250", "L/300"],
        ["Floors and roofs supporting plaster or brittle finish or non-flexible partitions", "L/250", "L/350"],
        ["Floors supporting columns (unless deflection included in global analysis)", "L/400", "L/500"],
        ["Where deflection can impair the appearance of the building", "L/250", "-"]
    ],
    "Recommended limiting values for vertical deflections",
    "delta_max is the total sag relative to the straight line joining the supports. delta_2 is the sag due to the variable actions plus time-dependent deformations."
)

# Table 5.1 / Partial safety factors
partial_safety_factors_for_buildings = Table(
    ["Case / Failure mode", "Symbol", "Recommended value"],
    [
        ["Resistance of cross-sections to yielding (Class 1, 2, 3)", r"$\gamma_{M0}$", 1.0],
        ["Resistance of members to instability (buckling)", r"$\gamma_{M1}$", 1.0],
        ["Resistance of cross-sections in tension to fracture", r"$\gamma_{M2}$", 1.25]
    ],
    "Partial safety factors for buildings",
    "Values may be set by the National Annex."
)

# Table 5.2 / 5.3.1
maximum_width_to_thickness_ratios_for_compression_elements = Table(
    ["Type of element", "Stress state", r"Class 1 limit ($\varepsilon = \sqrt{235/f_y}$)", "Class 2 limit", "Class 3 limit"],
    [
        ["Internal compression element (Web)", "Bending", r"$d/t \le 72\varepsilon$", r"$d/t \le 83\varepsilon$", r"$d/t \le 124\varepsilon$"],
        ["Internal compression element (Web)", "Compression", r"$d/t \le 33\varepsilon$", r"$d/t \le 38\varepsilon$", r"$d/t \le 42\varepsilon$"],
        ["Outstand compression element (Flange)", "Compression", r"$c/t \le 10\varepsilon$", r"$c/t \le 11\varepsilon$", r"$c/t \le 15\varepsilon$"],
        ["Tubular section (CHS)", "Bending / Compression", r"$d/t \le 50\varepsilon^2$", r"$d/t \le 70\varepsilon^2$", r"$d/t \le 90\varepsilon^2$"]
    ],
    "Maximum width-to-thickness ratios for compression elements",
    "Elements which fail to satisfy Class 3 limits should be classified as Class 4."
)

# Table 5.5.1
imperfection_factors_for_buckling_curves = Table(
    ["Buckling curve", r"Imperfection factor $\alpha$"],
    [
        ["a0", 0.13],
        ["a", 0.21],
        ["b", 0.34],
        ["c", 0.49],
        ["d", 0.76]
    ],
    "Imperfection factors for buckling curves",
    "Used to determine the reduction factor chi for column flexural buckling."
)

# Table 5.5.2 / 5.5.3
selection_of_buckling_curve_for_cross_sections = Table(
    ["Cross section", "Limits", "Buckling about axis", "Buckling curve (S 235 - S 420)", "Buckling curve (S 460)"],
    [
        ["Rolled I-sections", "h/b > 1.2, tf <= 40 mm", "y - y", "a", "a0"],
        ["Rolled I-sections", "h/b > 1.2, tf <= 40 mm", "z - z", "b", "a0"],
        ["Rolled I-sections", "h/b > 1.2, 40 < tf <= 100 mm", "y - y", "b", "a"],
        ["Rolled I-sections", "h/b > 1.2, 40 < tf <= 100 mm", "z - z", "c", "a"],
        ["Rolled I-sections", "h/b <= 1.2, tf <= 100 mm", "y - y", "b", "a"],
        ["Rolled I-sections", "h/b <= 1.2, tf <= 100 mm", "z - z", "c", "a"],
        ["Rolled I-sections", "tf > 100 mm", "y - y", "d", "c"],
        ["Rolled I-sections", "tf > 100 mm", "z - z", "d", "c"],
        ["Welded I-sections", "tf <= 40 mm", "y - y", "b", "b"],
        ["Welded I-sections", "tf <= 40 mm", "z - z", "c", "c"],
        ["Welded I-sections", "tf > 40 mm", "y - y", "c", "c"],
        ["Welded I-sections", "tf > 40 mm", "z - z", "d", "d"],
        ["Hot rolled hollow sections", "Any", "Any", "a", "a0"],
        ["Cold formed hollow sections", "Any", "Any", "c", "c"],
        ["L, U, T and solid sections", "Any", "Any", "c", "c"]
    ],
    "Selection of buckling curve for a cross-section",
    "Buckling curve selection determines the imperfection factor alpha to be used in calculation."
)

# Table 6.5.2
categories_of_bolted_connections = Table(
    ["Category", "Design criteria", "Remarks"],
    [
        ["Category A: Bearing type", "Fv,Ed <= Fv,Rd and Fv,Ed <= Fb,Rd", "No preloading required. Bolt grades 4.6 to 10.9."],
        ["Category B: Slip-resistant at serviceability", "Fv,Ed,ser <= Fs,Rd,ser and Fv,Ed <= Fv,Rd and Fv,Ed <= Fb,Rd", "Preloaded high strength bolts (8.8 or 10.9). No slip at SLS."],
        ["Category C: Slip-resistant at ultimate", "Fv,Ed <= Fs,Rd and Fv,Ed <= Fb,Rd", "Preloaded high strength bolts (8.8 or 10.9). No slip at ULS."],
        ["Category D: Tension, non-preloaded", "Ft,Ed <= Ft,Rd and Ft,Ed <= Bp,Rd", "No preloading required. Bolt grades 4.6 to 10.9."],
        ["Category E: Tension, preloaded", "Ft,Ed <= Ft,Rd and Ft,Ed <= Bp,Rd", "Preloaded high strength bolts (8.8 or 10.9)."]
    ],
    "Categories of bolted connections",
    "Fv,Ed is design shear load per bolt; Fb,Rd is bearing resistance; Fs,Rd is slip resistance; Ft,Ed is tensile load."
)
