try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 3.105
density_classes_and_design_densities_of_lightweight_concrete = Table(
    ["Density class", r"Oven-dry density $\rho$ [kg/m3]", "Design density plain concrete [kg/m3]", "Design density reinforced concrete [kg/m3]"],
    [
        ["1.0", "901 - 1000", 1050, 1150],
        ["1.2", "1001 - 1200", 1250, 1350],
        ["1.4", "1201 - 1400", 1450, 1550],
        ["1.6", "1401 - 1600", 1650, 1750],
        ["1.8", "1601 - 1800", 1850, 1950],
        ["2.0", "1801 - 2000", 2050, 2150]
    ],
    "Density classes and corresponding design densities of lightweight aggregate concrete according to ENV 206",
    "Densities for plain and reinforced concrete with normal percentages of reinforcement for calculating self-weight."
)

# Table 3.106
strength_classes_and_compressive_strengths_of_lightweight_concrete = Table(
    ["Strength class", r"$f_{lck}$ [N/mm2]"],
    [
        ["LC 12/15", 12],
        ["LC 16/20", 16],
        ["LC 20/25", 20],
        ["LC 25/30", 25],
        ["LC 30/37", 30],
        ["LC 35/45", 35],
        ["LC 40/50", 40],
        ["LC 45/55", 45],
        ["LC 50/60", 50]
    ],
    "Strength classes and characteristic compressive strengths flck of lightweight aggregate concrete",
    "For prestressed concrete, classes lower than LC 30/37 should not be used for pre-tensioned and lower than LC 25/30 for post-tensioned work."
)

# Table 3.107
creep_and_shrinkage_factors_for_lightweight_concrete = Table(
    ["Concrete strength class", r"Factor for Creep $\eta_3$", r"Factor for Shrinkage $\eta_4$"],
    [
        ["LC 12/15, LC 16/20", 1.3, 1.5],
        ["LC 20/25 to LC 50/60", 1.0, 1.2]
    ],
    "Factors for the evaluation of the creep coefficients and shrinkage strains of lightweight aggregate concrete",
    ""
)

# Table 4.114
basic_ratios_of_span_effective_depth_for_lightweight_concrete = Table(
    ["Structural system", "Concrete highly stressed", "Concrete lightly stressed"],
    [
        ["Simply supported beam, one- or two-way spanning simply supported slab", 15, 21],
        ["End span of continuous beam or one-way continuous slab or two-way spanning slab continuous over one long side", 20, 27],
        ["Interior span of beam or one-way or two-way spanning slab", 21, 30],
        ["Slab supported on columns without beams (Flat slab) (based on longer span)", 18, 25],
        ["Cantilever", 6, 8]
    ],
    "Basic ratios of span/effective depth for reinforced lightweight aggregate concrete members without axial compression",
    ""
)
