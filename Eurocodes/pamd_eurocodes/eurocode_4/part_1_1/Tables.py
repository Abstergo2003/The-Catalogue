try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 2.1
partial_safety_factors_for_materials_and_resistances = Table(
    ["Material / Component", r"Symbol $\gamma_M$", "Persistent and Transient Situations", "Accidental Situations"],
    [
        ["Concrete", r"\gamma_C", 1.50, 1.20],
        ["Reinforcing steel", r"\gamma_S", 1.15, 1.00],
        ["Structural steel (cross-sections)", r"\gamma_{M0}", 1.00, 1.00],
        ["Structural steel (member instability)", r"\gamma_{M1}", 1.00, 1.00],
        ["Structural steel (fracture)", r"\gamma_{M2}", 1.25, 1.25],
        ["Headed stud shear connection", r"\gamma_V", 1.25, 1.00],
        ["Longitudinal shear in composite slabs", r"\gamma_{VS}", 1.25, 1.00],
        ["Fatigue of headed studs in shear", r"\gamma_{Mf,s}", 1.00, 1.00]
    ],
    "Partial safety factors for materials and resistances in buildings (EN 1994-1-1 2.4.1.2)",
    "Recommended values for ultimate limit states design in building structures."
)

# Table 5.1
limits_to_redistribution_of_hogging_moments = Table(
    ["Analysis method", "Class 1 cross-section", "Class 2 cross-section", "Class 3 cross-section", "Class 4 cross-section"],
    [
        ["Un-cracked elastic analysis", "40%", "30%", "20%", "10%"],
        ["Cracked elastic analysis", "25%", "15%", "10%", "0%"]
    ],
    "Limits to redistribution of hogging moments, per cent of initial bending moment to be reduced (EN 1994-1-1 Table 5.1)",
    "For grades of structural steel higher than S355, redistribution should only be applied to beams with Class 1 and 2 sections (max 30% un-cracked, 15% cracked)."
)

# Table 5.2
classification_of_steel_flanges_in_compression_for_partially_encased_sections = Table(
    ["Cross-section Class", "Stress distribution", r"Width-to-thickness limit $c/t$"],
    [
        ["Class 1", "Tip in compression, partially encased", r"c/t \le 9\varepsilon"],
        ["Class 2", "Tip in compression, partially encased", r"c/t \le 14\varepsilon"],
        ["Class 3", "Tip in compression, rolled or welded", r"c/t \le 20\varepsilon"]
    ],
    "Classification of steel flanges in compression for partially-encased sections (EN 1994-1-1 Table 5.2)",
    r"epsilon = sqrt(235 / f_y) with f_y in N/mm2. Ratio b_c / b must be >= 0.85."
)

# Table 6.1
maximum_depth_of_uncased_steel_member = Table(
    ["Steel member type", "S 235 [mm]", "S 275 [mm]", "S 355 [mm]", "S 420 and S 460 [mm]"],
    [
        ["IPE section", 600, 550, 400, 270],
        ["HE section", 800, 700, 650, 500]
    ],
    "Maximum depth h (mm) of uncased steel member for simplified lateral-torsional buckling verification (EN 1994-1-1 Table 6.1)",
    "If partially encased in concrete, depth h may exceed the limit by up to 200 mm for S235-S355 and 150 mm for S420-S460."
)

# Table 6.2
upper_limits_kt_max_for_reduction_factor_kt = Table(
    ["Number of stud connectors per rib nr", "Sheeting thickness t [mm]", "Studs <= 20 mm welded through profiled sheeting", "Profiled sheeting with holes and studs 19 mm or 22 mm"],
    [
        ["nr = 1", "<= 1.0", 0.85, 0.75],
        ["nr = 1", "> 1.0", 1.00, 0.75],
        ["nr = 2", "<= 1.0", 0.70, 0.60],
        ["nr = 2", "> 1.0", 0.80, 0.60]
    ],
    "Upper limits kt,max for the reduction factor kt for ribs transverse to the beam (EN 1994-1-1 Table 6.2)",
    "Applicable for ribs with hp <= 85 mm and b0 >= hp."
)

# Table 6.3
maximum_cross_section_slenderness_values_for_composite_columns = Table(
    ["Cross-section type", r"Maximum slenderness ratio with $f_y$ in N/mm2"],
    [
        ["Circular hollow steel sections (CHS)", r"\max(d/t) = 90 \cdot (235 / f_y)"],
        ["Rectangular hollow steel sections (RHS)", r"\max(h/t) = 52 \cdot \sqrt{235 / f_y}"],
        ["Partially encased I-sections", r"\max(b/t_f) = 44 \cdot \sqrt{235 / f_y}"]
    ],
    "Maximum values of (d/t), (h/t), and (b/tf) for composite columns (EN 1994-1-1 Table 6.3)",
    "Values ensure local buckling does not occur before plastic resistance is reached."
)

# Table 6.4
moment_factors_beta_for_second_order_theory = Table(
    ["Moment distribution", r"Moment factor $\beta$", "Comment"],
    [
        ["First-order bending moments from member imperfection or lateral load", r"\beta = 1.0", "M_Ed is maximum bending moment within column length ignoring second-order effects"],
        ["End moments", r"\beta = 0.66 + 0.44r \ge 0.44", "M_Ed and r*M_Ed are end moments from first-order global analysis (-1 <= r <= 1)"]
    ],
    "Factors beta for the determination of moments according to second order theory (EN 1994-1-1 Table 6.4)",
    "Used in verification of composite columns under axial compression and uniaxial or biaxial bending."
)

# Table 6.5
buckling_curves_and_member_imperfections_for_composite_columns = Table(
    ["Cross-section type", "Reinforcement ratio rho_s", "Axis of buckling", "Buckling curve", "Member imperfection"],
    [
        ["Completely concrete encased I-section", "Any", "y-y", "b", "L/200"],
        ["Completely concrete encased I-section", "Any", "z-z", "c", "L/150"],
        ["Partially concrete encased I-section", "Any", "y-y", "b", "L/200"],
        ["Partially concrete encased I-section", "Any", "z-z", "c", "L/150"],
        ["Circular or rectangular hollow section", "rho_s <= 3%", "Any", "a", "L/300"],
        ["Circular or rectangular hollow section", "3% < rho_s <= 6%", "Any", "b", "L/200"],
        ["Circular hollow section with embedded I-section", "Any", "y-y", "b", "L/200"],
        ["Circular hollow section with embedded I-section", "Any", "z-z", "b", "L/200"],
        ["Partially encased cross-section with crossed I-sections", "Any", "Any", "b", "L/200"]
    ],
    "Buckling curves and member imperfections for composite columns (EN 1994-1-1 Table 6.5)",
    "rho_s = A_s / A_c. L is column system length."
)

# Table 6.6
design_shear_strength_tau_Rd = Table(
    ["Type of cross-section", r"Design shear strength $\tau_{Rd}$ [N/mm2]"],
    [
        ["Completely concrete encased steel sections", 0.30],
        ["Concrete filled circular hollow sections", 0.55],
        ["Concrete filled rectangular hollow sections", 0.40],
        ["Flanges of partially encased sections", 0.20],
        ["Webs of partially encased sections", 0.00]
    ],
    "Design shear strength tau_Rd for mechanical shear and friction connection (EN 1994-1-1 Table 6.6)",
    "Values apply where the steel surface is unpainted and free from oil, grease, and loose scale or rust."
)

# Table 7.1
maximum_bar_diameters_for_high_bond_bars = Table(
    ["Steel stress sigma_s [N/mm2]", r"Max bar diameter $\phi^*$ for $w_k = 0.4$ mm", r"Max bar diameter $\phi^*$ for $w_k = 0.3$ mm", r"Max bar diameter $\phi^*$ for $w_k = 0.2$ mm"],
    [
        [160, 40, 32, 25],
        [200, 32, 25, 16],
        [240, 20, 16, 12],
        [280, 16, 12, 8],
        [320, 12, 10, 6],
        [360, 10, 8, 5],
        [400, 8, 6, 4],
        [450, 6, 5, None]
    ],
    "Maximum bar diameters for high bond bars for crack control (EN 1994-1-1 Table 7.1)",
    "phi = phi* * (f_ct,eff / 2.9) where f_ct,eff is effective tensile strength of concrete."
)

# Table 7.2
maximum_bar_spacing_for_high_bond_bars = Table(
    ["Steel stress sigma_s [N/mm2]", "Max bar spacing for wk = 0.4 mm [mm]", "Max bar spacing for wk = 0.3 mm [mm]", "Max bar spacing for wk = 0.2 mm [mm]"],
    [
        [160, 300, 300, 200],
        [200, 300, 250, 150],
        [240, 250, 200, 100],
        [280, 200, 150, 50],
        [320, 150, 100, None],
        [360, 100, 50, None]
    ],
    "Maximum bar spacing for high bond bars for crack control (EN 1994-1-1 Table 7.2)",
    "Used for crack limitation in composite slabs and composite beam concrete flanges."
)
