try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 2.1
partial_factors_for_fire_design = Table(
    ["Material / Limit state", r"Symbol $\gamma_{M,fi}$", "Recommended value"],
    [
        ["Structural steel in fire", r"\gamma_{M,fi,a}", 1.00],
        ["Concrete in fire", r"\gamma_{M,fi,c}", 1.00],
        ["Reinforcing steel in fire", r"\gamma_{M,fi,s}", 1.00],
        ["Shear connection in fire", r"\gamma_{M,fi,v}", 1.00]
    ],
    "Partial safety factors gamma_M,fi for accidental fire design situation (EN 1994-1-2 Table 2.1)",
    "In accidental fire situations, partial safety factors for material properties are normally taken as 1.00."
)

# Table 3.1
reduction_factors_for_concrete_at_elevated_temperatures = Table(
    [r"Concrete temperature $\theta_c$ [°C]", r"Compressive strength factor $k_{c,\theta}$ (siliceous)", r"Strain $\varepsilon_{c1,\theta}$ [‰]", r"Ultimate strain $\varepsilon_{cu1,\theta}$ [‰]"],
    [
        [20, 1.00, 2.5, 20.0],
        [100, 1.00, 4.0, 22.5],
        [200, 0.95, 5.5, 25.0],
        [300, 0.85, 7.0, 27.5],
        [400, 0.75, 10.0, 30.0],
        [500, 0.60, 15.0, 32.5],
        [600, 0.45, 25.0, 35.0],
        [700, 0.30, 25.0, 37.5],
        [800, 0.15, 25.0, 40.0],
        [900, 0.08, 25.0, 42.5],
        [1000, 0.04, 25.0, 45.0],
        [1100, 0.01, 25.0, 47.5],
        [1200, 0.00, None, None]
    ],
    "Reduction factors for cylinder compressive strength and strain parameters of siliceous concrete at elevated temperatures (EN 1994-1-2 Table 3.2)",
    "fc,theta = kc,theta * fck. Applicable for normal-weight siliceous aggregate concrete."
)

# Table 4.1
minimum_cross_section_dimensions_composite_columns = Table(
    ["Column type", "Standard Fire Resistance", "Min width b / diameter d [mm]", "Min axis distance us [mm]", "Min reinforcement ratio rho_s [%]"],
    [
        ["Concrete-filled circular hollow section", "R30", 140, 20, 1.0],
        ["Concrete-filled circular hollow section", "R60", 220, 25, 1.5],
        ["Concrete-filled circular hollow section", "R90", 300, 30, 2.0],
        ["Concrete-filled circular hollow section", "R120", 350, 40, 3.0],
        ["Concrete-filled rectangular hollow section", "R30", 150, 20, 1.0],
        ["Concrete-filled rectangular hollow section", "R60", 250, 30, 2.0],
        ["Concrete-filled rectangular hollow section", "R90", 350, 40, 3.0],
        ["Concrete-filled rectangular hollow section", "R120", 400, 50, 4.0],
        ["Partially concrete-encased I-section", "R30", 150, 20, 1.0],
        ["Partially concrete-encased I-section", "R60", 200, 30, 1.5],
        ["Partially concrete-encased I-section", "R90", 260, 40, 2.0],
        ["Partially concrete-encased I-section", "R120", 340, 50, 3.0]
    ],
    "Minimum cross-sectional dimensions and reinforcement axis distances for composite columns (EN 1994-1-2 Table 4.4 - 4.7)",
    "Tabulated data for standard fire resistance classes R30 to R120 under load level eta_fi <= 0.5."
)

# Table 4.2
minimum_dimensions_for_partially_encased_composite_beams = Table(
    ["Standard Fire Resistance", "Min section width bc [mm]", "Min web thickness tw [mm]", "Min axis distance u [mm]"],
    [
        ["R30", 120, 6, 20],
        ["R60", 160, 8, 30],
        ["R90", 200, 10, 40],
        ["R120", 300, 12, 50]
    ],
    "Minimum dimensions and axis distance for composite beams with partially encased steel sections (EN 1994-1-2 Table 4.1)",
    "Valid for simply supported or continuous composite beams with concrete cast between flanges."
)

# Table 4.3
minimum_effective_thickness_composite_slabs = Table(
    ["Standard Fire Resistance (Insulation I)", "Effective thickness heff [mm]", "Minimum axis distance us [mm]"],
    [
        ["I 30", 60, 10],
        ["I 60", 80, 15],
        ["I 90", 100, 25],
        ["I 120", 120, 35],
        ["I 180", 150, 45]
    ],
    "Minimum effective slab thickness heff for thermal insulation of composite slabs with profiled steel sheeting (EN 1994-1-2 Table 4.3)",
    "heff is calculated taking into account the rib geometry and concrete thickness above the ribs."
)
