try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 1
simplified_capacity_reduction_factor_c_A = Table(
    ["Slenderness ratio hef / tef", "Floor span Lf <= 4.0 m", "Floor span 4.0 m < Lf <= 5.0 m", "Floor span 5.0 m < Lf <= 6.0 m", "Floor span 6.0 m < Lf <= 7.0 m"],
    [
        ["hef / tef <= 10", 0.85, 0.80, 0.75, 0.70],
        ["10 < hef / tef <= 14", 0.75, 0.70, 0.65, 0.60],
        ["14 < hef / tef <= 18", 0.65, 0.60, 0.55, 0.50],
        ["18 < hef / tef <= 21", 0.55, 0.50, 0.45, 0.40],
        ["21 < hef / tef <= 27", 0.45, 0.40, 0.35, 0.30]
    ],
    "Simplified capacity reduction factor c_A for vertical load resistance of unreinforced walls (EN 1996-3 Clause 4.2 Table 1)",
    "Vertical load resistance N_Rd = c_A * f_d * A. Applies where floor loads are supported directly."
)

# Table 2
limiting_dimensions_for_walls_in_simplified_method = Table(
    ["Structural element / Parameter", "Limiting value", "Conditions / Scope"],
    [
        ["Maximum number of storeys", 3, "Up to 4 storeys under favorable National Annex conditions"],
        ["Maximum clear storey height h", "3.0 m", "May be increased to 3.5 m for single-storey halls"],
        ["Maximum floor span Lf", "7.0 m", "Reinforced concrete or timber floor slabs"],
        ["Minimum thickness of external loadbearing wall", "175 mm (or 100 mm inner leaf of cavity)", "Unreinforced masonry units"],
        ["Minimum thickness of internal loadbearing wall", "100 mm", "Single-leaf wall"],
        ["Maximum slenderness ratio hef / tef", 27, "For all unreinforced walls in simplified method"]
    ],
    "Geometric boundary limits for application of simplified calculation method (EN 1996-3 Clause 2.1 Table 2)",
    "If any of these conditions are exceeded, detailed calculation according to EN 1996-1-1 is required."
)

# Table 3
limiting_backfill_height_for_basement_walls = Table(
    ["Wall thickness t [mm]", "Clear wall height h <= 2.6 m", "Clear wall height 2.6 m < h <= 3.0 m", "Minimum vertical design load N_Ed [kN/m]"],
    [
        ["t >= 200 mm", "hb <= 1.5 m", "Not permitted", 15.0],
        ["t >= 240 mm", "hb <= 2.0 m", "hb <= 1.8 m", 20.0],
        ["t >= 300 mm", "hb <= 2.4 m", "hb <= 2.2 m", 25.0],
        ["t >= 365 mm", "hb <= 2.7 m", "hb <= 2.5 m", 30.0]
    ],
    "Maximum allowable backfill height hb for unreinforced basement masonry walls (EN 1996-3 Clause 4.5 Table 3)",
    "Valid for level ground backfill, granular soil without hydrostatic water pressure, and concrete floor slab providing top horizontal restraint."
)

# Table 4
minimum_shear_wall_area_ratio = Table(
    ["Number of storeys n", "Wind zone with q_p <= 0.8 kN/m2", "Wind zone with 0.8 < q_p <= 1.1 kN/m2", "Wind zone with 1.1 < q_p <= 1.4 kN/m2"],
    [
        ["1 storey", "1.0% of floor area", "1.2% of floor area", "1.5% of floor area"],
        ["2 storeys", "1.5% of floor area", "1.8% of floor area", "2.2% of floor area"],
        ["3 storeys", "2.0% of floor area", "2.5% of floor area", "3.0% of floor area"],
        ["4 storeys", "2.5% of floor area", "3.2% of floor area", "4.0% of floor area"]
    ],
    "Minimum cross-sectional area ratio of shear walls Asw / Afloor in each orthogonal direction (EN 1996-3 Annex A)",
    "Ensures global horizontal building stability against lateral wind action without individual shear wall calculations."
)
