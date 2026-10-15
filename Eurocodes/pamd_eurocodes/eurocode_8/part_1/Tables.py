try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 3.1
ground_types_A_to_E_classification = Table(
    ["Ground type", "Description of stratigraphic profile", "Shear wave velocity vs,30 [m/s]", "SPT blow count N_SPT", "Undrained shear strength cu [kPa]"],
    [
        ["Type A", "Rock or other rock-like geological formation with at most 5 m of weaker surface material", "> 800", None, None],
        ["Type B", "Deposits of very dense sand, gravel, or very stiff clay, tens of metres thick", "360 to 800", "> 50", "> 250"],
        ["Type C", "Deep deposits of dense or medium-dense sand, gravel or stiff clay (tens to hundreds of metres)", "180 to 360", "15 to 50", "70 to 250"],
        ["Type D", "Deposits of loose-to-medium cohesionless soil, or predominantly soft-to-firm cohesive soil", "< 180", "< 15", "< 70"],
        ["Type E", "Surface alluvium layer with vs values of type C or D (5-20 m thick) underlain by stiffer rock (vs > 800 m/s)", "Variable", "Variable", "Variable"],
        ["Type S1", "Deposits with >= 10 m of soft clays/silts with high plasticity index (PI > 40) and high moisture content", "< 100", None, "10 to 20"],
        ["Type S2", "Liquefiable soils, sensitive clays, or profiles requiring special geotechnical site response analysis", "Special", "Special", "Special"]
    ],
    "Ground type classification according to stratigraphic profile and shear wave velocity vs,30 (EN 1998-1 Table 3.1)",
    "Governs the selection of soil factor S and corner periods TB, TC, TD in seismic response spectra."
)

# Table 3.2
type_1_elastic_response_spectra_parameters = Table(
    ["Ground type", "Soil factor S", "Lower period TB [s]", "Upper period TC [s]", "Displacement period TD [s]"],
    [
        ["Type A", 1.00, 0.15, 0.40, 2.00],
        ["Type B", 1.20, 0.15, 0.50, 2.00],
        ["Type C", 1.15, 0.20, 0.60, 2.00],
        ["Type D", 1.35, 0.20, 0.80, 2.00],
        ["Type E", 1.40, 0.15, 0.50, 2.00]
    ],
    "Parameters describing recommended Type 1 elastic response spectra for surface-wave magnitude Ms > 5.5 (EN 1998-1 Table 3.2)",
    "Applied for high to moderate seismicity regions across Europe."
)

# Table 3.3
type_2_elastic_response_spectra_parameters = Table(
    ["Ground type", "Soil factor S", "Lower period TB [s]", "Upper period TC [s]", "Displacement period TD [s]"],
    [
        ["Type A", 1.00, 0.05, 0.25, 1.20],
        ["Type B", 1.35, 0.05, 0.25, 1.20],
        ["Type C", 1.50, 0.10, 0.25, 1.20],
        ["Type D", 1.80, 0.10, 0.30, 1.20],
        ["Type E", 1.60, 0.05, 0.25, 1.20]
    ],
    "Parameters describing recommended Type 2 elastic response spectra for surface-wave magnitude Ms <= 5.5 (EN 1998-1 Table 3.3)",
    "Applied for low to moderate intra-plate seismicity regions."
)

# Table 3.4
vertical_elastic_response_spectra_parameters = Table(
    ["Spectrum type", r"Ratio $a_{vg} / a_g$", "Lower period TB [s]", "Upper period TC [s]", "Displacement period TD [s]"],
    [
        ["Type 1 spectrum (Ms > 5.5)", 0.90, 0.05, 0.15, 1.00],
        ["Type 2 spectrum (Ms <= 5.5)", 0.45, 0.05, 0.15, 1.00]
    ],
    "Recommended values of parameters describing vertical elastic response spectra (EN 1998-1 Table 3.4)",
    "Used in verification of prestressed concrete members, long spans, cantilevers, and base-isolated structures."
)

# Table 4.1
importance_classes_and_factors_for_buildings = Table(
    ["Importance Class", "Description of building / Occupancy", r"Recommended importance factor $\gamma_I$"],
    [
        ["Class I", "Buildings of minor importance for public safety (e.g. agricultural sheds, storage buildings)", 0.80],
        ["Class II", "Ordinary buildings, not belonging to other classes (residential, commercial, offices)", 1.00],
        ["Class III", "Buildings whose resistance to earthquakes is of importance in view of collapse consequences (schools, assembly halls)", 1.20],
        ["Class IV", "Buildings whose integrity during earthquakes is vital for civil protection (hospitals, fire stations, power plants)", 1.40]
    ],
    "Importance classes and importance factors gamma_I for buildings (EN 1998-1 Table 4.3)",
    "Design ground acceleration a_g = gamma_I * a_gR."
)

# Table 5.1
basic_behavior_factor_q0_for_concrete_buildings = Table(
    ["Structural system type", "Ductility Class Medium (DCM)", "Ductility Class High (DCH)"],
    [
        ["Frame system, dual system, coupled wall system", r"3.0 \cdot \alpha_u / \alpha_1", r"4.5 \cdot \alpha_u / \alpha_1"],
        ["Uncoupled wall system", 3.0, r"4.0 \cdot \alpha_u / \alpha_1"],
        ["Torsionally flexible system", 2.0, 3.0],
        ["Inverted pendulum system", 1.5, 2.0]
    ],
    "Basic value of the behavior factor q0 for concrete buildings (EN 1998-1 Table 5.1)",
    "alpha_u / alpha_1 represents the overstrength ratio from first plastic hinge to global collapse."
)

# Table 6.1
basic_behavior_factor_q0_for_steel_buildings = Table(
    ["Structural system type", "Ductility Class Medium (DCM)", "Ductility Class High (DCH)"],
    [
        ["Moment resisting frames (MRF)", 4.0, r"5.0 \cdot \alpha_u / \alpha_1"],
        ["Concentrically braced frames (diagonal CBF)", 2.0, 2.5],
        ["Concentrically braced frames (V-braced)", 2.0, 2.5],
        ["Eccentrically braced frames (EBF)", 4.0, r"5.0 \cdot \alpha_u / \alpha_1"],
        ["Inverted pendulum system", 1.5, 2.0]
    ],
    "Basic value of the behavior factor q0 for steel buildings (EN 1998-1 Table 6.2)",
    "Structures designed for Ductility Class Low (DCL) use q = 1.5 to 2.0."
)

# Table 9.1
basic_behavior_factor_q_for_masonry_buildings = Table(
    ["Type of masonry construction", "Behavior factor q"],
    [
        ["Unreinforced masonry to EN 1996-1-1 only", 1.5],
        ["Unreinforced masonry satisfying EN 1998-1 provisions", BRange(1.5, 2.5, 1.75)],
        ["Confined masonry (with reinforced concrete tie-elements)", BRange(2.0, 3.0, 2.5)],
        ["Reinforced masonry (with distributed reinforcement)", BRange(2.5, 3.0, 2.75)]
    ],
    "Recommended values of behavior factor q for masonry buildings (EN 1998-1 Table 9.1)",
    "Confined and reinforced masonry allow significantly higher energy dissipation and ductility."
)
