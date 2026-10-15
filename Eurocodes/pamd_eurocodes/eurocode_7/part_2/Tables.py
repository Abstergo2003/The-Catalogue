try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 1
soil_classification_particle_size_ranges = Table(
    ["Soil fraction", "Sub-fraction", "Particle size range [mm]"],
    [
        ["Very coarse soil", "Boulders", "> 200 mm"],
        ["Very coarse soil", "Cobbles", "63 mm to 200 mm"],
        ["Coarse soil (Gravel)", "Coarse gravel", "20 mm to 63 mm"],
        ["Coarse soil (Gravel)", "Medium gravel", "6.3 mm to 20 mm"],
        ["Coarse soil (Gravel)", "Fine gravel", "2.0 mm to 6.3 mm"],
        ["Coarse soil (Sand)", "Coarse sand", "0.63 mm to 2.0 mm"],
        ["Coarse soil (Sand)", "Medium sand", "0.20 mm to 0.63 mm"],
        ["Coarse soil (Sand)", "Fine sand", "0.063 mm to 0.20 mm"],
        ["Fine soil (Silt)", "Coarse silt", "0.020 mm to 0.063 mm"],
        ["Fine soil (Silt)", "Medium silt", "0.0063 mm to 0.020 mm"],
        ["Fine soil (Silt)", "Fine silt", "0.002 mm to 0.0063 mm"],
        ["Fine soil (Clay)", "Clay", "<= 0.002 mm"]
    ],
    "Particle size ranges for soil classification according to ISO 14688-1 (EN 1997-2 Table 1)",
    "Defines the boundary diameters for laboratory sieve and sedimentation hydrometer analysis."
)

# Table 2
plasticity_classification_of_fine_grained_soils = Table(
    ["Plasticity designation", "Plasticity Index IP [%]", "Liquid Limit wL [%]", "Behavior / Workability"],
    [
        ["Non-plastic (silt)", "IP < 4", "wL < 30", "Friable, low cohesion, sensitive to moisture changes"],
        ["Low plasticity (clayey silt)", "4 <= IP <= 10", "30 <= wL <= 35", "Slight cohesion, low shrink-swell potential"],
        ["Medium plasticity (clay)", "10 < IP <= 20", "35 < wL <= 50", "Moderate cohesion and plasticity"],
        ["High plasticity (fat clay)", "20 < IP <= 40", "50 < wL <= 70", "High cohesion, significant shrink-swell potential"],
        ["Extremely high plasticity", "IP > 40", "wL > 70", "Very high volume change on drying or wetting"]
    ],
    "Classification of fine-grained cohesive soils according to plasticity (EN 1997-2 / ISO 14688-2)",
    "Plasticity index IP = wL - wP. Evaluated from standard Casagrande or fall-cone liquid limit tests."
)

# Table 3
typical_ranges_of_permeability_k_for_soils = Table(
    ["Soil type / Material", "Degree of permeability", "Coefficient of permeability k [m/s]"],
    [
        ["Clean gravel", "Very high permeability", "> 10^-2 m/s"],
        ["Clean sand, sand and gravel mixtures", "High permeability", "10^-4 to 10^-2 m/s"],
        ["Fine sand, silty sand", "Medium permeability", "10^-6 to 10^-4 m/s"],
        ["Silt, sandy silt, loess", "Low permeability", "10^-8 to 10^-6 m/s"],
        ["Homogeneous intact clay", "Very low permeability (impervious)", "10^-11 to 10^-8 m/s"]
    ],
    "Typical ranges of coefficient of permeability k for soils (EN 1997-2 Annex A)",
    "Measured by constant head (coarse soils) or falling head / triaxial cell (fine soils) laboratory tests."
)

# Table 4
typical_ranges_of_effective_friction_angle_and_cohesion = Table(
    ["Soil description", r"Effective friction angle $\phi'$ [°]", r"Effective cohesion $c'$ [kPa]", "Undrained shear strength cu [kPa]"],
    [
        ["Dense well-graded sand and gravel", BRange(36, 44, 40), 0, None],
        ["Medium dense quartz sand", BRange(32, 36, 34), 0, None],
        ["Loose uniform sand", BRange(28, 32, 30), 0, None],
        ["Inorganic silt", BRange(26, 32, 28), BRange(0, 10, 5), BRange(20, 60, 40)],
        ["Stiff overconsolidated clay", BRange(22, 28, 25), BRange(10, 30, 15), BRange(80, 180, 120)],
        ["Soft normally consolidated clay", BRange(18, 24, 20), BRange(0, 5, 0), BRange(15, 40, 25)]
    ],
    "Indicative typical values of shear strength parameters for preliminary design (EN 1997-2)",
    "Derived from consolidated-drained (CD) or consolidated-undrained (CU) triaxial compression and direct shear tests."
)

# Table 5
sample_quality_classes_for_laboratory_testing = Table(
    ["Quality Class", "Permitted testing / Properties measured", "Soil state / Sampling method"],
    [
        ["Quality Class 1", "Compressibility (E_oed), shear strength (phi', c', cu), density (rho), permeability (k)", "Undisturbed sample: no change in fabric, water content, or void ratio"],
        ["Quality Class 2", "Density (rho), water content (w), consistency limits, shear strength (cu remoulded)", "Undisturbed sample: fabric slightly disturbed, water content and density intact"],
        ["Quality Class 3", "Water content (w), particle size distribution, Atterberg limits, compaction (Proctor)", "Disturbed sample: fabric remoulded, natural water content preserved"],
        ["Quality Class 4", "Particle size distribution, organic content, chemical composition, plastic limits", "Disturbed sample: water content altered, natural constituents preserved"],
        ["Quality Class 5", "Soil identification and strata boundaries only", "Heavily disturbed cuttings or washings"]
    ],
    "Sample quality classes and applicability to laboratory tests according to EN ISO 22475-1 (EN 1997-2 Table 2.1)",
    "Only Quality Class 1 samples are valid for determining undisturbed strength and consolidation parameters."
)
