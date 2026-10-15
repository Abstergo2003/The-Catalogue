try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 7.105
classification_of_tightness = Table(
    ["Tightness Class", "Requirements for leakage"],
    [
        ["0", "Some degree of leakage acceptable, or leakage of liquids irrelevant."],
        ["1", "Leakage to be limited to a small amount. Some surface staining or damp patches acceptable."],
        ["2", "Leakage to be minimal. Appearance not to be impaired by staining."],
        ["3", "No leakage permitted."]
    ],
    "Classification of tightness",
    "All concrete will permit the passage of small quantities of liquids and gases by diffusion."
)

# Table K.1
values_of_alpha_for_saturated_and_dry_concrete = Table(
    ["Definition of tensile strength (fctx)", r"Saturated concrete $\alpha$", r"Air dry concrete $\alpha$"],
    [
        ["fctm", 0.56, 0.30],
        ["fctk,0.05", 1.30, 0.21],
        ["fctk,0.95", 2.43, 0.39]
    ],
    "Values of alpha for saturated and dry concrete",
    ""
)

# Table K.2
creep_coefficient_multipliers_for_temperature = Table(
    ["Temperature [deg C]", "Creep coefficient multiplier"],
    [
        [20, 1.00],
        [50, 1.35],
        [100, 1.96],
        [150, 2.58],
        [200, 3.20]
    ],
    "Creep coefficient multipliers to take account of temperature where the concrete is heated prior to loading",
    "The values have been deduced from CEB Bulletin 208 and are in good agreement with multipliers calculated on the basis of an activation energy for creep of 8 kJ/mol."
)

# Table L.1
restraint_factors_for_central_zone_of_walls = Table(
    ["Ratio L/H", "Restraint factor at base", "Restraint factor at top"],
    [
        ["1", 0.5, 0.0],
        ["2", 0.5, 0.0],
        ["3", 0.5, 0.05],
        ["4", 0.5, 0.3],
        ["> 8", 0.5, 0.5]
    ],
    "Restraint factors for central zone of walls",
    "L is the wall length and H is the wall height."
)

# Table N.1
design_of_joints_for_the_control_of_cracking = Table(
    ["Option", "Method of control", "Movement joint spacing", "Reinforcement"],
    [
        ["(a)", "Continuous - full restraint", "Generally no joints, though some widely spaced joints may be desirable where substantial deformation is expected", "Reinforcement in accordance with Chapters 6 and 7.3"],
        ["(b)", "Close movement joints - minimum restraint", "Complete joints at greater of 5 m or 1.5 times wall height", "Reinforcement in accordance with Chapter 6 but not less than minimum given in 9.6.2 to 9.6.4"]
    ],
    "Design of joints for the control of cracking",
    "Complete joints are joints where complete discontinuity is provided in both reinforcement and concrete."
)
