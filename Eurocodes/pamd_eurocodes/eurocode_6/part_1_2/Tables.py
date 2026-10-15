try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 2.1
partial_safety_factors_for_masonry_in_fire = Table(
    ["Material / Limit State", r"Symbol $\gamma_{M,fi}$", "Recommended value"],
    [
        ["Masonry in fire situation", r"\gamma_{M,fi}", 1.00],
        ["Reinforcing steel in masonry in fire", r"\gamma_{s,fi}", 1.00],
        ["Ancillary components in fire", r"\gamma_{a,fi}", 1.00]
    ],
    "Partial safety factors gamma_M,fi for masonry in accidental fire situations (EN 1996-1-2 Clause 2.3)",
    "In accidental fire situations, partial safety factors for material properties are taken as 1.00."
)

# Table N.1
minimum_thickness_of_non_loadbearing_clay_masonry_walls_for_fire_resistance = Table(
    ["Masonry unit type", "EI 30 [mm]", "EI 60 [mm]", "EI 90 [mm]", "EI 120 [mm]", "EI 240 [mm]"],
    [
        ["Clay Group 1 (Solid)", 65, 90, 100, 115, 175],
        ["Clay Group 2 (Vertically perforated)", 70, 90, 100, 140, 200],
        ["Clay Group 3 (Horizontally perforated)", 80, 100, 120, 150, None]
    ],
    "Minimum thickness of non-loadbearing unrendered clay masonry walls for fire resistance classes EI (EN 1996-1-2 Annex N Table N.1.1)",
    "Values apply for unrendered masonry; applying 10 mm gypsum or sand/cement plaster on each side reduces requirements."
)

# Table N.2
minimum_thickness_of_loadbearing_clay_masonry_walls_for_fire_resistance = Table(
    ["Masonry unit type / Loading", "REI 30 [mm]", "REI 60 [mm]", "REI 90 [mm]", "REI 120 [mm]", "REI 240 [mm]"],
    [
        ["Clay Group 1 (Solid, alpha <= 1.0)", 90, 100, 115, 140, 240],
        ["Clay Group 1 (Solid, alpha <= 0.6)", 90, 90, 100, 115, 200],
        ["Clay Group 2 (Vertically perforated, alpha <= 1.0)", 100, 115, 140, 175, 300],
        ["Clay Group 2 (Vertically perforated, alpha <= 0.6)", 100, 100, 115, 140, 240]
    ],
    "Minimum thickness of loadbearing unrendered clay masonry single-leaf walls for fire resistance classes REI (EN 1996-1-2 Annex N Table N.1.2)",
    "alpha is the load level ratio N_Ed,fi / N_Rd."
)

# Table N.3
minimum_thickness_of_concrete_masonry_walls_for_fire_resistance = Table(
    ["Masonry block type", "REI 30 [mm]", "REI 60 [mm]", "REI 90 [mm]", "REI 120 [mm]", "REI 240 [mm]"],
    [
        ["Dense aggregate concrete Group 1 (Solid)", 90, 100, 120, 140, 200],
        ["Dense aggregate concrete Group 2 (Hollow)", 100, 120, 150, 190, 240],
        ["Lightweight aggregate concrete Group 1", 70, 90, 100, 120, 175],
        ["Lightweight aggregate concrete Group 2", 90, 100, 120, 150, 200]
    ],
    "Minimum thickness of loadbearing aggregate concrete masonry single-leaf walls for fire resistance classes REI (EN 1996-1-2 Annex N Table N.3.1)",
    "Lightweight concrete offers superior thermal insulation compared to dense concrete."
)

# Table N.4
minimum_thickness_of_autoclaved_aerated_concrete_walls_for_fire_resistance = Table(
    ["Wall application", "REI 30 [mm]", "REI 60 [mm]", "REI 90 [mm]", "REI 120 [mm]", "REI 240 [mm]"],
    [
        ["Non-loadbearing separating walls (EI)", 50, 75, 75, 100, 150],
        ["Loadbearing single-leaf walls (REI, alpha <= 1.0)", 100, 100, 125, 150, 200],
        ["Loadbearing single-leaf walls (REI, alpha <= 0.6)", 75, 100, 100, 125, 175]
    ],
    "Minimum thickness of autoclaved aerated concrete (AAC) masonry walls for fire resistance (EN 1996-1-2 Annex N Table N.4.1)",
    "Applies to AAC blocks with dry density rho >= 350 kg/m3."
)
