try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 1
bending_moment_coefficients_for_laterally_loaded_walls = Table(
    ["Support condition", "Aspect ratio h/L = 0.5", "Aspect ratio h/L = 0.75", "Aspect ratio h/L = 1.0", "Aspect ratio h/L = 1.5", "Aspect ratio h/L = 2.0"],
    [
        ["4 sides simply supported (orthogonal ratio mu = 0.3)", 0.031, 0.045, 0.055, 0.069, 0.077],
        ["4 sides simply supported (orthogonal ratio mu = 0.5)", 0.025, 0.041, 0.051, 0.064, 0.071],
        ["3 sides supported, top edge free (mu = 0.3)", 0.050, 0.069, 0.085, 0.107, 0.118],
        ["3 sides supported, top edge free (mu = 0.5)", 0.042, 0.061, 0.077, 0.098, 0.110],
        ["3 sides supported, one vertical edge free (mu = 0.3)", 0.060, 0.080, 0.095, 0.115, 0.125],
        ["Top and bottom supported only (vertical span)", 0.125, 0.125, 0.125, 0.125, 0.125]
    ],
    "Bending moment coefficients alpha for walls subjected to lateral wind loads (DD ENV 1996-1-3 Clause 4.1 / Annex A)",
    "Design moment M_Ed1 = alpha * W_Ed * L^2. mu is the orthogonal ratio f_xk1 / f_xk2."
)

# Table 2
limiting_slenderness_ratios_for_arching_action = Table(
    ["Masonry unit type", "Maximum height-to-thickness ratio h / t", "Notes"],
    [
        ["Solid clay or calcium silicate units", 25, "Rigid abutments with arching thrust"],
        ["Perforated clay bricks (Group 2)", 20, "Verify bearing stress at abutment contact"],
        ["Aggregate concrete blocks (solid or hollow)", 20, "Ensure sufficient rigid floor/roof thrust restraint"],
        ["Autoclaved aerated concrete (AAC)", 18, "Restricted due to lower compressive strength under arching thrust"]
    ],
    "Limiting slenderness ratios h/t for masonry walls resisting lateral loads by arching action (DD ENV 1996-1-3 Clause 4.2)",
    "Supports must be capable of resisting horizontal thrust without displacement."
)

# Table 3
characteristic_flexural_strength_values = Table(
    ["Masonry unit type", "Mortar type", r"Parallel to bed joints $f_{xk1}$ [N/mm2]", r"Perpendicular to bed joints $f_{xk2}$ [N/mm2]"],
    [
        ["Clay units", "General purpose (>= M5)", 0.10, 0.40],
        ["Clay units", "Thin layer mortar", 0.15, 0.50],
        ["Calcium silicate units", "General purpose (>= M5)", 0.10, 0.30],
        ["Aggregate concrete units (solid)", "General purpose (>= M5)", 0.15, 0.45],
        ["Autoclaved aerated concrete (AAC)", "Thin layer mortar", 0.15, 0.30]
    ],
    "Characteristic flexural strengths fxk1 and fxk2 of unreinforced masonry (DD ENV 1996-1-3 Clause 3.2)",
    "fxk1 represents flexural tension across bed joints; fxk2 represents failure perpendicular to bed joints involving unit shear/tension."
)
