try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 2.1
recommended_values_of_partial_safety_factors_for_materials_gamma_M = Table(
    ["Material / Construction category", "Class 1", "Class 2", "Class 3", "Class 4", "Class 5"],
    [
        ["Units of Category I, designed mortar", 1.5, 1.7, 2.0, 2.2, 2.5],
        ["Units of Category I, prescribed mortar", 1.7, 2.0, 2.2, 2.5, 2.7],
        ["Units of Category II, any mortar", 2.0, 2.2, 2.5, 2.7, 3.0],
        ["Anchorage of reinforcing steel", 1.7, 2.0, 2.2, 2.5, 2.7],
        ["Reinforcing steel and prestressing steel", 1.15, 1.15, 1.15, 1.15, 1.15],
        ["Ancillary components (wall ties, brackets)", 1.7, 2.0, 2.2, 2.5, 2.7],
        ["Lintels (EN 845-2)", 1.5, 1.5, 1.5, 1.5, 1.5],
        ["Serviceability limit states (all materials)", 1.0, 1.0, 1.0, 1.0, 1.0]
    ],
    "Recommended values of partial safety factors for materials gamma_M (EN 1996-1-1 Table 2.3)",
    "Classes 1 to 5 relate to the level of quality control in manufacturing of units and site execution control."
)

# Table 3.1
geometrical_requirements_for_grouping_of_masonry_units = Table(
    ["Material type", "Group 1 (Solid)", "Group 2 (Hollow/perforated)", "Group 3 (High perforations)", "Group 4 (Cellular blocks)"],
    [
        ["Clay units", "Holes <= 25%", "25% < Holes <= 55%", "55% < Holes <= 70%", "Holes <= 70%"],
        ["Calcium silicate units", "Holes <= 25%", "25% < Holes <= 55%", "Not used", "Not used"],
        ["Aggregate concrete units", "Holes <= 25%", "25% < Holes <= 60%", "Not used", "Holes <= 60%"],
        ["Autoclaved aerated concrete (AAC)", "Holes <= 5%", "Not used", "Not used", "Not used"]
    ],
    "Geometrical requirements for grouping of masonry units (EN 1996-1-1 Table 3.1)",
    "Percentage of gross volume formed by vertical or horizontal holes."
)

# Table 3.3
values_of_K_for_compressive_strength_of_masonry = Table(
    ["Masonry Unit Type", "Unit Group", "General purpose mortar", "Thin layer mortar (<= 3 mm)", "Lightweight mortar (600-700 kg/m3)", "Lightweight mortar (700-1500 kg/m3)"],
    [
        ["Clay", "Group 1", 0.50, 0.75, 0.30, 0.40],
        ["Clay", "Group 2", 0.45, 0.55, 0.30, 0.40],
        ["Clay", "Group 3", 0.35, 0.25, 0.20, 0.25],
        ["Clay", "Group 4", 0.30, None, None, None],
        ["Calcium silicate", "Group 1", 0.50, 0.80, None, None],
        ["Calcium silicate", "Group 2", 0.45, 0.55, None, None],
        ["Aggregate concrete", "Group 1", 0.50, 0.80, 0.45, None],
        ["Aggregate concrete", "Group 2", 0.50, 0.80, 0.45, None],
        ["Autoclaved aerated concrete", "Group 1", 0.50, 0.85, 0.45, None],
        ["Manufactured stone", "Group 1", 0.50, 0.75, None, None],
        ["Dimensioned natural stone", "Group 1", 0.50, None, None, None]
    ],
    "Values of constant K for characteristic compressive strength fk = K * fb^0.70 * fm^0.30 (EN 1996-1-1 Table 3.3)",
    "For thin layer mortar (<= 3 mm bed joint) with Group 1 units, fk = K * fb^0.85."
)

# Table 3.4
characteristic_initial_shear_strength_f_vk0 = Table(
    ["Masonry Unit Type", "Mortar Strength Class", "General purpose mortar [N/mm2]", "Thin layer mortar [N/mm2]", "Lightweight mortar [N/mm2]"],
    [
        ["Clay", "M10 to M20", 0.30, None, None],
        ["Clay", "M2.5 to M9", 0.20, 0.30, 0.20],
        ["Clay", "M1 to M2", 0.10, None, None],
        ["Calcium silicate", "M10 to M20", 0.20, 0.40, 0.20],
        ["Calcium silicate", "M2.5 to M9", 0.15, 0.40, 0.20],
        ["Aggregate concrete", "M10 to M20", 0.20, 0.30, 0.20],
        ["Aggregate concrete", "M2.5 to M9", 0.15, 0.30, 0.20],
        ["Autoclaved aerated concrete", "All classes", 0.15, 0.30, 0.20],
        ["Dimensioned natural stone", "M2.5 to M9", 0.15, None, None]
    ],
    "Values of characteristic initial shear strength f_vk0 under zero compressive stress (EN 1996-1-1 Table 3.4)",
    "Characteristic shear strength f_vk = f_vk0 + 0.4 * sigma_d, limited to 0.065 * f_b or f_vk,max."
)

# Table 6.1
stiffness_coefficient_rho_t_for_walls_stiffened_by_piers = Table(
    ["Ratio of pier spacing to pier width", "Pier thickness / Wall thickness = 1", "Pier thickness / Wall thickness = 2", "Pier thickness / Wall thickness = 3"],
    [
        ["Spacing / Width = 6", 1.0, 1.4, 2.0],
        ["Spacing / Width = 10", 1.0, 1.2, 1.4],
        ["Spacing / Width = 20", 1.0, 1.0, 1.0]
    ],
    "Stiffness coefficient rho_t for walls stiffened by piers (EN 1996-1-1 Table 6.1)",
    "Effective thickness t_ef = rho_t * t. Linear interpolation between values is permitted."
)

# Table 6.2
limiting_ratios_of_effective_span_to_effective_depth = Table(
    ["Support condition", "Wall subjected to out-of-plane bending", "Reinforced masonry beam"],
    [
        ["Simply supported", 35, 20],
        ["Continuous", 45, 26],
        ["Spanning in two directions", 45, None],
        ["Cantilever", 18, 7]
    ],
    "Limiting ratios of effective span to effective depth (lef / d) for out-of-plane bending (EN 1996-1-1 Table 6.2)",
    "Prevents excessive cracking and deflections in reinforced masonry walls and beams."
)
