try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 1
soil_type_classification_from_CPT_friction_ratio = Table(
    ["Soil classification zone", "Cone resistance qc [MPa]", "Friction ratio Rf [%]", "Typical soil type"],
    [
        ["Zone 1", "< 1.0", "> 4.0", "Sensitive fine-grained soils / Soft clay"],
        ["Zone 2", "< 1.0", "> 5.0", "Organic soils and peat"],
        ["Zone 3", "0.5 to 2.5", "2.0 to 5.0", "Clay to silty clay"],
        ["Zone 4", "1.0 to 5.0", "1.5 to 3.0", "Silt mixtures: clayey silt to silty sand"],
        ["Zone 5", "3.0 to 12.0", "1.0 to 2.0", "Sand mixtures: silty sand to sandy silt"],
        ["Zone 6", "5.0 to 25.0", "0.5 to 1.5", "Sands: clean sand to silty sand"],
        ["Zone 7", "> 15.0", "< 1.0", "Gravelly sand to dense gravel"],
        ["Zone 8", "1.5 to 6.0", "> 3.0", "Very stiff to hard overconsolidated clay / clay till"]
    ],
    "Soil type behavior classification based on normalized CPT cone resistance and friction ratio Rf (Robertson chart / EN 1997-2 Annex D)",
    "Rf = (fs / qc) * 100%. Measured during continuous push at standard rate of 20 mm/s."
)

# Table 2
correlation_between_SPT_N60_and_density_of_sands = Table(
    ["Relative density state", "Energy-corrected SPT blow count N60", "Relative Density ID [%]", r"Effective friction angle $\phi'$ [°]"],
    [
        ["Very loose", BRange(0, 4, 2), BRange(0, 15, 10), BRange(28, 30, 29)],
        ["Loose", BRange(4, 10, 7), BRange(15, 35, 25), BRange(30, 32, 31)],
        ["Medium dense", BRange(10, 30, 20), BRange(35, 65, 50), BRange(32, 36, 34)],
        ["Dense", BRange(30, 50, 40), BRange(65, 85, 75), BRange(36, 41, 38)],
        ["Very dense", BRange(50, 100, 60), BRange(85, 100, 90), BRange(41, 46, 43)]
    ],
    "Empirical correlation between energy-corrected SPT blow count N60 and density of coarse cohesionless soils (EN 1997-2 Annex E)",
    "N60 represents blow count corrected for 60% of theoretical impact energy."
)

# Table 3
correlation_between_SPT_N60_and_consistency_of_clays = Table(
    ["Consistency", "SPT blow count N60", "Undrained shear strength cu [kPa]"],
    [
        ["Very soft", "< 2", "< 20 kPa"],
        ["Soft", "2 to 4", "20 to 40 kPa"],
        ["Firm", "4 to 8", "40 to 75 kPa"],
        ["Stiff", "8 to 15", "75 to 150 kPa"],
        ["Very stiff", "15 to 30", "150 to 300 kPa"],
        ["Hard", "> 30", "> 300 kPa"]
    ],
    "Empirical correlation between SPT N60 blow count and consistency of fine cohesive soils (EN 1997-2 Annex E)",
    "Approximate rule of thumb: cu approximately equals (4 to 6) * N60 in kPa."
)

# Table 4
menard_pressuremeter_rheological_factor_alpha = Table(
    ["Soil type / Formation", "Condition / Overconsolidation ratio", r"Rheological factor $\alpha$"],
    [
        ["Peat", "Normally consolidated", 1.00],
        ["Clay", "Overconsolidated", 1.00],
        ["Clay", "Normally consolidated", 0.67],
        ["Clay", "Remoulded / soft", 0.50],
        ["Silt", "Overconsolidated", 0.67],
        ["Silt", "Normally consolidated", 0.50],
        ["Sand", "Dense / overconsolidated", 0.50],
        ["Sand", "Normally consolidated", 0.33],
        ["Gravel", "Normally consolidated", 0.25],
        ["Rock", "Fractured or weathered", 0.33]
    ],
    "Ménard pressuremeter rheological structural coefficient alpha for settlement calculations (EN 1997-2 Annex E)",
    "Used in the Ménard settlement equation: s = (2 / (9 * E_M)) * (p - sigma_v0) * (lambda_d * R_d)^alpha + ... ."
)

# Table 5
soil_identification_ranges_from_dilatometer_index_ID = Table(
    ["Material Index ID", "Soil classification", "Representative soil behavior"],
    [
        ["ID < 0.6", "Clay", "Cohesive, fine-grained, undrained response during blade insertion"],
        ["0.6 <= ID <= 1.8", "Silt", "Intermediate behavior, partially drained, sandy/clayey silt"],
        ["ID > 1.8", "Sand", "Cohesionless, drained response, sand to gravelly sand"]
    ],
    "Soil type identification ranges based on Marchetti flat dilatometer material index ID (EN 1997-2 Annex E)",
    "ID = (p1 - p0) / (p0 - u0). p0 is lift-off pressure; p1 is 1.1 mm expansion pressure."
)
