try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 2.1
maximum_permissible_element_thickness_to_avoid_brittle_fracture = Table(
    [
        "Steel grade",
        "Sub-grade (Charpy test T / J)",
        r"T_Ed = 10 deg C ($\sigma = 0.75 f_y$)",
        r"T_Ed = 0 deg C ($\sigma = 0.75 f_y$)",
        r"T_Ed = -10 deg C ($\sigma = 0.75 f_y$)",
        r"T_Ed = -20 deg C ($\sigma = 0.75 f_y$)",
        r"T_Ed = -30 deg C ($\sigma = 0.75 f_y$)",
        r"T_Ed = -40 deg C ($\sigma = 0.75 f_y$)",
        r"T_Ed = -50 deg C ($\sigma = 0.75 f_y$)"
    ],
    [
        ["S 235", "JR (+20 deg C / 27 J)", 60, 50, 40, 35, 30, 25, 20],
        ["S 235", "J0 (0 deg C / 27 J)", 90, 75, 60, 50, 40, 35, 30],
        ["S 235", "J2 (-20 deg C / 27 J)", 125, 105, 90, 75, 60, 50, 40],
        ["S 275", "JR (+20 deg C / 27 J)", 55, 45, 35, 30, 25, 20, 15],
        ["S 275", "J0 (0 deg C / 27 J)", 75, 65, 55, 45, 35, 30, 25],
        ["S 275", "J2 (-20 deg C / 27 J)", 110, 95, 75, 65, 55, 45, 35],
        ["S 275", "M, N (-20 deg C / 40 J)", 135, 110, 95, 75, 65, 55, 45],
        ["S 275", "ML, NL (-50 deg C / 27 J)", 185, 160, 135, 110, 95, 75, 65],
        ["S 355", "JR (+20 deg C / 27 J)", 40, 35, 25, 20, 15, 15, 10],
        ["S 355", "J0 (0 deg C / 27 J)", 60, 50, 40, 35, 25, 20, 15],
        ["S 355", "J2 (-20 deg C / 27 J)", 90, 75, 60, 50, 40, 35, 25],
        ["S 355", "K2, M, N (-20 deg C / 40 J)", 110, 90, 75, 60, 50, 40, 35],
        ["S 355", "ML, NL (-50 deg C / 27 J)", 155, 130, 110, 90, 75, 60, 50],
        ["S 460", "Q, N (-20 deg C / 40 J)", 70, 55, 45, 35, 30, 20, 15],
        ["S 460", "QL, NL (-50 deg C / 27 J)", 105, 90, 70, 55, 45, 35, 30]
    ],
    "Maximum permissible element thickness t (mm) to avoid brittle fracture",
    "Tabulated for stress level sigma_Ed = 0.75 fy(t). For lower stress levels (0.50 fy or 0.25 fy), permissible thickness increases."
)

# Table 3.1
choice_of_quality_class_for_through_thickness_properties = Table(
    ["Target value Z_Ed", "Required quality class according to EN 10164"],
    [
        [r"$Z_{Ed} \le 10$", "No special requirement (-)"],
        [r"$10 < Z_{Ed} \le 20$", "Z15"],
        [r"$20 < Z_{Ed} \le 30$", "Z25"],
        [r"$Z_{Ed} > 30$", "Z35"]
    ],
    "Choice of quality class for through-thickness properties",
    "ZEd is the target value determined from ZEd = Za + Zb + Zc + Zd + Ze to avoid lamellar tearing."
)

# Table 3.2
target_value_components_for_z_ed = Table(
    ["Influencing factor", "Parameter range / Joint detail", "Component value"],
    [
        ["Weld throat depth (Za)", "a <= 7 mm", 0],
        ["Weld throat depth (Za)", "7 < a <= 14 mm", 3],
        ["Weld throat depth (Za)", "14 < a <= 21 mm", 6],
        ["Weld throat depth (Za)", "21 < a <= 28 mm", 9],
        ["Weld throat depth (Za)", "28 < a <= 35 mm", 12],
        ["Weld throat depth (Za)", "a > 35 mm", 15],
        ["Joint shape (Zb)", "Cruciform or T-joints (full penetration)", 3],
        ["Joint shape (Zb)", "Corner joints", 6],
        ["Material thickness s (Zc)", "s <= 10 mm", 0],
        ["Material thickness s (Zc)", "10 < s <= 20 mm", 2],
        ["Material thickness s (Zc)", "20 < s <= 30 mm", 4],
        ["Material thickness s (Zc)", "30 < s <= 40 mm", 6],
        ["Material thickness s (Zc)", "s > 70 mm", 10],
        ["Structural restraint (Zd)", "Low restraint (free shrinkage)", 0],
        ["Structural restraint (Zd)", "Medium restraint", 3],
        ["Structural restraint (Zd)", "High restraint", 6],
        ["Preheating (Ze)", "No preheat", 0],
        ["Preheating (Ze)", "Preheat T > 100 deg C", -8]
    ],
    "Target value components for ZEd (Za, Zb, Zc, Zd, Ze)",
    "Used in Expression ZEd = Za + Zb + Zc + Zd + Ze to specify steel through-thickness ductility."
)
