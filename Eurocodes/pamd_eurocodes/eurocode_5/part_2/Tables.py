try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 2.1
partial_safety_factors_for_timber_bridges = Table(
    ["Material / Component", r"Symbol $\gamma_M$", "Fundamental combination (ULS)", "Accidental combination", "Fatigue verification"],
    [
        ["Solid timber", r"\gamma_M", 1.30, 1.00, 1.00],
        ["Glued laminated timber (glulam)", r"\gamma_M", 1.25, 1.00, 1.00],
        ["Laminated veneer lumber (LVL)", r"\gamma_M", 1.20, 1.00, 1.00],
        ["Steel parts in joints and connectors", r"\gamma_M", 1.15, 1.00, 1.00],
        ["High-strength prestressing steel bars", r"\gamma_S", 1.15, 1.00, 1.00]
    ],
    "Partial safety factors gamma_M for timber bridge structures (EN 1995-2 Clause 2.4)",
    "Recommended values for persistent and transient design situations in highway and pedestrian bridges."
)

# Table 2.2
modification_factors_k_mod_for_service_class_3_bridges = Table(
    ["Material", "Action duration class", r"Modification factor $k_{mod}$ (Service Class 3)", r"Deformation factor $k_{def}$ (Service Class 3)"],
    [
        ["Solid timber (EN 338)", "Permanent", 0.50, 2.00],
        ["Solid timber (EN 338)", "Long-term", 0.55, 1.50],
        ["Solid timber (EN 338)", "Medium-term", 0.65, 0.75],
        ["Solid timber (EN 338)", "Short-term (traffic)", 0.70, 0.30],
        ["Solid timber (EN 338)", "Instantaneous (wind/braking)", 0.90, 0.00],
        ["Glued laminated timber", "Permanent", 0.50, 2.00],
        ["Glued laminated timber", "Long-term", 0.55, 1.50],
        ["Glued laminated timber", "Medium-term", 0.65, 0.75],
        ["Glued laminated timber", "Short-term (traffic)", 0.70, 0.30],
        ["Glued laminated timber", "Instantaneous (wind/braking)", 0.90, 0.00]
    ],
    "Modification factors k_mod and creep factors k_def for Service Class 3 bridge environments (EN 1995-2 Clause 2.3)",
    "Accounts for outdoor exposure to humidity, rain, and cyclic vehicular traffic loads."
)

# Table 5.1
transverse_prestressing_requirements_for_stress_laminated_decks = Table(
    ["Design parameter", "Recommended design value", "Limiting criterion"],
    [
        ["Initial prestress level sigma_p,0", "0.70 to 1.00 N/mm2", "Compensates for long-term creep and moisture relaxation"],
        ["Minimum residual prestress sigma_p,min", ">= 0.35 N/mm2", "Prevents interlaminar joint separation and water entry"],
        ["Tendon bar spacing a_s", "<= 600 mm to 900 mm", "Ensures uniform transverse compressive stress distribution"],
        ["Maximum bearing stress under anchor plate", "<= 1.25 * fc,90,d", "Prevents local crushing of edge timber laminations"]
    ],
    "Design rules and prestress criteria for stress-laminated timber bridge decks (EN 1995-2 Clause 5.2)",
    "Ensures friction shear transfer and durability of timber plate decks under moving wheel loads."
)

# Table 6.1
limiting_deflection_values_for_timber_bridges = Table(
    ["Bridge type / Loading condition", "Limiting deflection u_net,freq", "Notes"],
    [
        ["Road bridges under characteristic traffic load", "L / 400 to L / 500", "Main longitudinal girders and deck panels"],
        ["Railway bridges under LM71 / train loading", "L / 600", "Strict limitation to avoid ballast degradation"],
        ["Footbridges and cycle bridges under pedestrian load", "L / 300 to L / 400", "Includes comfort and vibrational verification"],
        ["Cantilever decks and walkways", "L_c / 200", "Measured at the cantilever tip"]
    ],
    "Recommended limiting deflection values for timber bridges (EN 1995-2 Clause 7.2)",
    "Evaluated under the frequent combination of actions without dynamic amplification."
)

# Table 7.1
fatigue_strength_parameters_for_timber_bridges = Table(
    ["Material / Detail", r"Fatigue limit ratio $f_{fat} / f_k$", "Number of cycles N", "Notes"],
    [
        ["Solid timber in bending", 0.45, "N = 2 * 10^6", "R-ratio = 0 (pulsating tension)"],
        ["Glued laminated timber in bending", 0.50, "N = 2 * 10^6", "R-ratio = 0 (pulsating tension)"],
        ["Timber in shear parallel to grain", 0.40, "N = 2 * 10^6", "Longitudinal shear in beam webs"],
        ["Dowel-type steel fasteners in shear", 0.50, "N = 2 * 10^6", "Connection fatigue verification under axle spectra"]
    ],
    "Fatigue verification parameters for timber bridge members and fasteners (EN 1995-2 Clause 6.4)",
    "Verified using cumulative damage calculation where cyclic stress range Delta_sigma exceeds fatigue threshold."
)
