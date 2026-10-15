try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 2.1
reliability_classes_for_towers_and_masts = Table(
    ["Reliability Class", "Description", "Consequences of failure", "Return period of wind"],
    [
        ["Class 3", "Towers or masts erected in urban areas, major telecommunications installations, or heights > 100m", "Major economic loss or severe risk to life", "50 years (with increased safety factors)"],
        ["Class 2", "All normal towers and masts not falling into Class 1 or Class 3", "Moderate economic loss, normal risk to life", "50 years"],
        ["Class 1", "Towers or masts in open country or unmanned rural sites, height < 20m", "Minor economic loss, low risk of injury", "10 to 25 years"]
    ],
    "Reliability classes for towers and masts (EN 1993-3-1 Table 2.1)",
    "Towers and masts are classified into three reliability classes depending on consequences of failure."
)

# Table 2.2
partial_safety_factors_for_towers_and_masts = Table(
    ["Resistance type", r"Symbol $\gamma_M$", "Reliability Class 1", "Reliability Class 2", "Reliability Class 3"],
    [
        ["Cross-section resistance", r"\gamma_{M0}", 1.00, 1.00, 1.00],
        ["Member buckling resistance", r"\gamma_{M1}", 1.00, 1.00, 1.10],
        ["Cross-section fracture in tension", r"\gamma_{M2}", 1.25, 1.25, 1.25],
        ["Guy ropes (pre-stretched / proof loaded)", r"\gamma_{Mg}", 1.10, 1.20, 1.35],
        ["Guy ropes (non-prestretched)", r"\gamma_{Mg}", 1.20, 1.40, 1.60],
        ["Insulators", r"\gamma_{Mi}", 1.80, 2.00, 2.30]
    ],
    "Partial safety factors gamma_M for towers and masts (EN 1993-3-1 Table 2.2)",
    "Values may be defined in the National Annex."
)

# Table B.1
logarithmic_decrement_of_structural_damping = Table(
    ["Structure type", r"Minimum $\delta_s$", r"Nominal $\delta_s$", r"Maximum $\delta_s$"],
    [
        ["Welded lattice steel tower (un-guyed)", 0.015, 0.025, 0.035],
        ["Bolted lattice steel tower (un-guyed)", 0.030, 0.040, 0.060],
        ["Guyed steel lattice mast", 0.040, 0.050, 0.080],
        ["Steel cylindrical chimney (unlined)", 0.010, 0.015, 0.020],
        ["Steel cylindrical chimney (refractory/brick lined)", 0.030, 0.040, 0.060]
    ],
    "Approximate values of logarithmic decrement of structural damping delta_s (EN 1993-3-1 Annex B)",
    "Total damping delta = delta_s + delta_a, where delta_a is aerodynamic damping."
)

# Table B.2.1
aerodynamic_force_coefficients_for_lattice_towers = Table(
    ["Solidity ratio phi", "Square tower (flat-sided members)", "Square tower (circular members)", "Triangular tower (flat-sided)", "Triangular tower (circular)"],
    [
        [0.1, 3.8, 1.8, 3.1, 1.4],
        [0.2, 3.3, 1.7, 2.7, 1.3],
        [0.3, 2.8, 1.6, 2.3, 1.2],
        [0.4, 2.4, 1.5, 1.9, 1.1],
        [0.5, 2.1, 1.4, 1.6, 1.0]
    ],
    "Aerodynamic overall force coefficients c_f for lattice towers as a function of solidity ratio (EN 1993-3-1)",
    "Solidity ratio phi = A_projected / A_enclosed; wind normal to tower face."
)

# Table B.3.1
drag_coefficients_for_guy_ropes = Table(
    ["Cable condition", r"Cable Reynolds number $Re$", r"Normal drag coefficient $c_{N0}$"],
    [
        ["Stranded wire rope (bare)", BRange(0, 20000, 10000), 1.20],
        ["Stranded wire rope (bare)", BRange(20000, 100000, 50000), 1.10],
        ["Spiral strand cable (smooth)", BRange(0, 100000, 50000), 1.00],
        ["Ice-coated guy cable (cylindrical ice)", BRange(0, 100000, 50000), 1.20]
    ],
    "Drag coefficients c_N0 for guy ropes and stay cables under normal wind flow (EN 1993-3-1 Annex B)",
    "Reynolds number Re = v * d / nu, where d is the outer cable diameter."
)
