"""Eurocode 9 - Part 1-1: General structural rules - Tables.
EN 1999-1-1 / ENV 1999-1-1.
"""
try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange


# Table 3.1
partial_safety_factors = Table(
    ["Resistance type", "Symbol", "Recommended value", "UK NAD value"],
    [
        ["Resistance of cross-sections to yielding", "gamma_M0", 1.10, 1.10],
        ["Resistance of members to buckling", "gamma_M1", 1.10, 1.10],
        ["Resistance of net sections to tensile fracture", "gamma_M2", 1.25, 1.25],
        ["Resistance of welded connections", "gamma_Mw", 1.25, 1.30]
    ],
    "Partial safety factors gamma_M for aluminium structures (EN 1999-1-1 Clause 6.1.3 / NAD Table 1)",
    "Applied to characteristic cross-sectional, member, and joint capacities in ultimate limit state design."
)

# Table 3.2
physical_properties_aluminium = Table(
    ["Property", "Symbol", "Value", "Unit"],
    [
        ["Modulus of elasticity", "E", 70000, "MPa (N/mm^2)"],
        ["Shear modulus", "G", 27000, "MPa (N/mm^2)"],
        ["Poisson's ratio", "nu", 0.30, "-"],
        ["Coefficient of linear thermal expansion", "alpha", "23 * 10^-6", "K^-1"],
        ["Unit mass / density", "rho", 2700, "kg/m^3"]
    ],
    "Fundamental physical and elastic properties of structural aluminium alloys (EN 1999-1-1 Clause 3.2.3)",
    "Nominal elastic constants applicable to all standard wrought structural aluminium alloys."
)

# Table 3.3
structural_aluminium_alloys_strengths = Table(
    ["Alloy designation & temper", "Product form", "0.2% proof strength fo [MPa]", "Ultimate strength fu [MPa]", "HAZ proof strength fo,haz [MPa]", "HAZ softening rho_o"],
    [
        ["EN AW-6060 T6", "Extruded profile (t <= 3 mm)", 150, 190, 65, 0.43],
        ["EN AW-6063 T6", "Extruded profile (t <= 10 mm)", 170, 215, 85, 0.50],
        ["EN AW-6005A T6", "Extruded profile (open/hollow)", 225, 270, 115, 0.51],
        ["EN AW-6082 T6", "Extruded profile (t <= 5 mm)", 260, 310, 125, 0.48],
        ["EN AW-6082 T6", "Extruded profile (5 < t <= 15 mm)", 250, 290, 125, 0.50],
        ["EN AW-6082 T6", "Sheet / Plate (t <= 6 mm)", 255, 305, 125, 0.49],
        ["EN AW-5083 H111/O", "Sheet / Plate (marine grade)", 125, 275, 125, 1.00],
        ["EN AW-7020 T6", "Extrusions / plate (high strength)", 280, 350, 190, 0.68]
    ],
    "Characteristic strength values and HAZ softening factors for structural aluminium alloys (EN 1999-1-1 Tables 3.2a-d)",
    "Defines virgin yield and tensile strengths together with strength reduction in the heat-affected zone of welds."
)

# Table 5.1
column_buckling_classes = Table(
    ["Buckling class", "Imperfection factor alpha", "Limit slenderness lambda_0_bar", "Applicable cross-sections and alloys"],
    [
        ["Class A", 0.20, 0.10, "Plain extrusions, symmetric profiles without welding in 6000/7000 heat-treated alloys"],
        ["Class B", 0.32, 0.00, "Welded sections, hollow sections with longitudinal welds, unsymmetric sections, 5000 series alloys"]
    ],
    "Selection of buckling class and parameters for column flexural buckling curves (EN 1999-1-1 Table 6.6)",
    "Accounts for initial geometric out-of-straightness and residual stresses in aluminium compression members."
)

# Table 6.1
haz_extent_dimensions = Table(
    ["Welding process", "Parent metal thickness t [mm]", "Extent of HAZ b_haz (butt weld)", "Extent of HAZ b_haz (fillet weld)"],
    [
        ["MIG (GMAW)", "t <= 6 mm", "20 mm", "20 mm"],
        ["MIG (GMAW)", "6 < t <= 12 mm", "30 mm", "25 mm"],
        ["MIG (GMAW)", "12 < t <= 25 mm", "35 mm", "30 mm"],
        ["TIG (GTAW)", "t <= 6 mm", "30 mm", "30 mm"],
        ["TIG (GTAW)", "t > 6 mm", "35 mm - 40 mm", "35 mm"]
    ],
    "Extent of the heat-affected zone b_haz measured from weld boundary (EN 1999-1-1 Clause 6.5.2)",
    "Determines the boundary of reduced mechanical strength around fusion welded joints in aluminium alloys."
)
