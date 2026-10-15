try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 2.3.3.2
partial_safety_factors_for_timber_structures = Table(
    ["Material / State", r"Symbol $\gamma_M$", "Fundamental combination (ULS)", "Accidental combination"],
    [
        ["Solid timber", r"\gamma_M", 1.30, 1.00],
        ["Glued laminated timber (glulam)", r"\gamma_M", 1.25, 1.00],
        ["Laminated veneer lumber (LVL)", r"\gamma_M", 1.20, 1.00],
        ["Plywood", r"\gamma_M", 1.20, 1.00],
        ["Particleboards (OSB)", r"\gamma_M", 1.20, 1.00],
        ["Fibreboards", r"\gamma_M", 1.30, 1.00],
        ["Steel in joints / connections", r"\gamma_M", 1.10, 1.00],
        ["Serviceability limit states", r"\gamma_M", 1.00, 1.00]
    ],
    "Partial coefficients for material properties gamma_M (EN 1995-1-1 Table 2.3.3.2)",
    "Recommended values for persistent and transient design situations in building structures."
)

# Table 3.1.6
load_duration_classes = Table(
    ["Load-duration class", "Order of accumulated duration", "Examples of loading"],
    [
        ["Permanent", "More than 10 years", "Self-weight, permanent equipment"],
        ["Long-term", "6 months to 10 years", "Storage, water tanks"],
        ["Medium-term", "1 week to 6 months", "Imposed floor loads, snow in heavy prolonged areas"],
        ["Short-term", "Less than one week", "Snow, wind loads"],
        ["Instantaneous", "A few seconds / dynamic", "Accidental impact, explosion, wind gust"]
    ],
    "Load-duration classes for timber structures (EN 1995-1-1 Table 3.1.6)",
    "Duration of action governs the selection of strength modification factor k_mod."
)

# Table 3.1.7
modification_factors_k_mod_for_service_classes = Table(
    ["Material", "Load-duration class", "Service Class 1", "Service Class 2", "Service Class 3"],
    [
        ["Solid and glued laminated timber", "Permanent", 0.60, 0.60, 0.50],
        ["Solid and glued laminated timber", "Long-term", 0.70, 0.70, 0.55],
        ["Solid and glued laminated timber", "Medium-term", 0.80, 0.80, 0.65],
        ["Solid and glued laminated timber", "Short-term", 0.90, 0.90, 0.70],
        ["Solid and glued laminated timber", "Instantaneous", 1.10, 1.10, 0.90],
        ["Plywood", "Permanent", 0.60, 0.60, 0.50],
        ["Plywood", "Long-term", 0.70, 0.70, 0.55],
        ["Plywood", "Medium-term", 0.80, 0.80, 0.65],
        ["Plywood", "Short-term", 0.90, 0.90, 0.70],
        ["Plywood", "Instantaneous", 1.10, 1.10, 0.90],
        ["OSB (Grade 3 and 4)", "Permanent", 0.40, 0.30, None],
        ["OSB (Grade 3 and 4)", "Long-term", 0.50, 0.40, None],
        ["OSB (Grade 3 and 4)", "Medium-term", 0.70, 0.55, None],
        ["OSB (Grade 3 and 4)", "Short-term", 0.90, 0.70, None],
        ["OSB (Grade 3 and 4)", "Instantaneous", 1.10, 0.90, None]
    ],
    "Values of modification factor k_mod for service class and load duration (EN 1995-1-1 Table 3.1.7)",
    "For combinations with different load durations, k_mod corresponding to the shortest duration action is used."
)

# Table 4.1
deformation_factors_k_def_for_timber_and_wood_materials = Table(
    ["Material", "Service Class 1", "Service Class 2", "Service Class 3"],
    [
        ["Solid timber (EN 338)", 0.60, 0.80, 2.00],
        ["Glued laminated timber (glulam)", 0.60, 0.80, 2.00],
        ["Plywood", 0.80, 1.00, 2.50],
        ["OSB (Grades 3 and 4)", 1.50, 2.25, None],
        ["Particleboards (EN 312)", 2.25, 3.00, None],
        ["Hard fibreboards (EN 622-5)", 2.25, 3.00, None]
    ],
    "Values of deformation factor k_def for creep deflection evaluation (EN 1995-1-1 Table 4.1)",
    "Final deformation u_fin = u_inst * (1 + k_def)."
)

# Table 4.2
slip_moduli_K_ser_for_dowel_type_fasteners = Table(
    ["Fastener type", "Timber-to-timber", "Panel-to-timber", "Steel-to-timber"],
    [
        ["Dowels and fitted bolts", r"\rho_m^{1.5} \cdot d / 20", r"\rho_m^{1.5} \cdot d / 25", r"\rho_m^{1.5} \cdot d / 10"],
        ["Screws (with predrilling)", r"\rho_m^{1.5} \cdot d / 20", r"\rho_m^{1.5} \cdot d / 25", r"\rho_m^{1.5} \cdot d / 10"],
        ["Nails (with predrilling)", r"\rho_m^{1.5} \cdot d / 20", r"\rho_m^{1.5} \cdot d / 25", r"\rho_m^{1.5} \cdot d / 10"],
        ["Nails (without predrilling)", r"\rho_m^{1.5} \cdot d^{0.8} / 25", r"\rho_m^{1.5} \cdot d^{0.8} / 30", r"\rho_m^{1.5} \cdot d^{0.8} / 12.5"],
        ["Staples", r"\rho_m^{1.5} \cdot d^{0.8} / 60", r"\rho_m^{1.5} \cdot d^{0.8} / 80", r"\rho_m^{1.5} \cdot d^{0.8} / 40"]
    ],
    "Values of slip modulus K_ser in N/mm for dowel-type fasteners per shear plane per fastener (EN 1995-1-1 Table 4.2)",
    "rho_m is mean wood density in kg/m3; d is fastener diameter in mm."
)

# Table 4.3
limiting_values_of_deflection_for_timber_beams = Table(
    ["Deflection component", "Simply supported beams", "Cantilevers"],
    [
        ["Instantaneous deflection u_inst due to variable load", "L / 300 to L / 500", "L / 150 to L / 250"],
        ["Final deflection u_fin due to variable load", "L / 200 to L / 300", "L / 100 to L / 150"],
        ["Net final deflection u_net,fin", "L / 250 to L / 350", "L / 125 to L / 175"]
    ],
    "Recommended limiting values of deflections for timber beams (EN 1995-1-1 Clause 4.3 Table 4.3)",
    "Precamber u_0 may be subtracted to obtain u_net,fin = u_fin - u_0."
)

# Table 5.1.5
compression_perpendicular_to_grain_factor_kc_90 = Table(
    ["Support configuration / Loaded length", r"Bearing length $\ell \le 150$ mm", r"Bearing length $\ell > 150$ mm"],
    [
        ["Support at member end (a < 100 mm)", 1.00, 1.00],
        ["Internal support (a >= 100 mm, l <= 15 mm)", 1.80, 1.00],
        ["Internal support (a >= 100 mm, 15 < l <= 150 mm)", r"1 + \frac{150 - \ell}{170}", 1.00]
    ],
    "Values of factor kc,90 for compression perpendicular to the grain (EN 1995-1-1 Table 5.1.5)",
    "Accounts for redistribution and confinement of compressive stresses perpendicular to grain."
)

# Table 6.3.1.2
minimum_spacings_and_edge_distances_for_nails = Table(
    ["Spacing / Distance", "Without pre-drilling (alpha = 0°)", "With pre-drilling (alpha = 0°)", "Angle alpha = 90°"],
    [
        ["Spacing a1 parallel to grain", "10 * d", "5 * d", "5 * d"],
        ["Spacing a2 perpendicular to grain", "5 * d", "5 * d", "5 * d"],
        ["End distance a3,t (loaded end)", "15 * d", "12 * d", "10 * d"],
        ["End distance a3,c (unloaded end)", "10 * d", "7 * d", "7 * d"],
        ["Edge distance a4,t (loaded edge)", "7 * d", "5 * d", "7 * d"],
        ["Edge distance a4,c (unloaded edge)", "5 * d", "3 * d", "3 * d"]
    ],
    "Minimum spacings and edge distances for nails (EN 1995-1-1 Table 6.3.1.2 / Table 8.2)",
    "d is nominal nail diameter; alpha is the angle between force and grain direction."
)

# Table 6.5.1.2
minimum_spacings_and_edge_distances_for_bolts = Table(
    ["Spacing / Distance", "Angle alpha = 0° (parallel to grain)", "Angle alpha = 90° (perpendicular)", "General angle alpha"],
    [
        ["Spacing a1 parallel to grain", "4 * d", "4 * d", r"(4 + |\cos\alpha|) \cdot d"],
        ["Spacing a2 perpendicular to grain", "4 * d", "4 * d", "4 * d"],
        ["End distance a3,t (loaded end)", "7 * d", "7 * d", r"\max(7d, 80\text{ mm})"],
        ["End distance a3,c (unloaded end)", "4 * d", "4 * d", "4 * d"],
        ["Edge distance a4,t (loaded edge)", "4 * d", "4 * d", r"\max(2 + 2\sin\alpha, 3) \cdot d"],
        ["Edge distance a4,c (unloaded edge)", "3 * d", "3 * d", "3 * d"]
    ],
    "Minimum spacings and edge/end distances for bolts and dowels (EN 1995-1-1 Table 6.5.1.2 / Table 8.5)",
    "d is nominal bolt or dowel diameter in mm."
)

# Table EN 338
strength_classes_for_structural_timber = Table(
    ["Strength Class", "fm,k [N/mm2]", "ft,0,k [N/mm2]", "fc,0,k [N/mm2]", "E0,mean [kN/mm2]", "rho_k [kg/m3]"],
    [
        ["C14", 14, 8.0, 16, 7.0, 290],
        ["C16", 16, 10.0, 17, 8.0, 310],
        ["C18", 18, 11.0, 18, 9.0, 320],
        ["C24", 24, 14.0, 21, 11.0, 350],
        ["C27", 27, 16.0, 22, 11.5, 370],
        ["C30", 30, 18.0, 23, 12.0, 380],
        ["C35", 35, 21.0, 25, 13.0, 400],
        ["C40", 40, 24.0, 26, 14.0, 420],
        ["D30 (Hardwood)", 30, 18.0, 23, 11.0, 530],
        ["D40 (Hardwood)", 40, 24.0, 26, 13.0, 590],
        ["D50 (Hardwood)", 50, 30.0, 29, 14.0, 650],
        ["GL24h (Glulam)", 24, 16.5, 24, 11.5, 380],
        ["GL28h (Glulam)", 28, 19.5, 26.5, 12.6, 410],
        ["GL32h (Glulam)", 32, 22.5, 29, 13.7, 430],
        ["GL36h (Glulam)", 36, 26.0, 31, 14.7, 450]
    ],
    "Characteristic strength, stiffness, and density properties for timber strength classes (EN 338 / EN 1194)",
    "fm,k: bending strength; ft,0,k: tension parallel; fc,0,k: compression parallel; E0,mean: mean MOE; rho_k: characteristic density."
)
