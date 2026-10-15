try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 3.1
recommended_values_for_partial_factors_for_fatigue_strength = Table(
    ["Assessment method", r"Low consequence of failure $\gamma_{Mf}$", r"High consequence of failure $\gamma_{Mf}$"],
    [
        ["Damage tolerant", 1.00, 1.15],
        ["Safe life", 1.15, 1.35]
    ],
    "Recommended values for partial factors for fatigue strength gamma_Mf",
    "Damage tolerant method assumes regular inspection and maintenance to detect crack propagation; safe life method ensures fatigue crack initiation does not occur during design life."
)

# Table 8.1
fatigue_detail_categories_non_welded_details = Table(
    ["Structural detail", r"Detail category $\Delta\sigma_c$ [N/mm2]", "Description / Requirements"],
    [
        ["Rolled plate, flat, section", 160, "Sharp edges removed, free from cracks and severe notches"],
        ["Machined or ground edges", 140, "Cut edges dressed by machining or grinding"],
        ["Machine gas cut edges", 125, "All drag lines ground out, cut edges deburred"],
        ["Double covered symmetric splice", 112, "Preloaded high strength bolts in reamed or drilled holes"],
        ["Shear on preloaded bolts", 100, "Shear stress range based on nominal shank area"],
        ["Single lap joint with bolts", 90, "Two or more bolts in line of force, allowing for local bending"]
    ],
    "Fatigue detail categories for non-welded details and mechanically fastened joints",
    "Stress ranges should be calculated using the nominal net cross-section area."
)

# Table 8.2
fatigue_detail_categories_welded_built_up_sections = Table(
    ["Type of weld / Joint", r"Detail category $\Delta\sigma_c$ [N/mm2]", "Description / Conditions"],
    [
        ["Continuous automatic longitudinal fillet weld", 125, "Welds made from both sides without stop-start positions"],
        ["Continuous manual longitudinal fillet weld", 100, "Welds with stop-start positions inspected for defects"],
        ["Intermittent longitudinal fillet weld", 80, "Gap between welds <= 16*t or 200 mm"],
        ["Cope holes in built-up beams", 71, "Cut edges and corners radiused (r >= 10 mm) and smooth"]
    ],
    "Fatigue detail categories for welded built-up sections",
    "Stress ranges calculated using nominal section properties."
)

# Table 8.3
fatigue_detail_categories_transverse_butt_welds = Table(
    ["Weld configuration", r"Detail category $\Delta\sigma_c$ [N/mm2]", "Requirements / Verification"],
    [
        ["Full penetration butt weld ground flush", 112, "Weld ground flush to plate surface in direction of stress, 100% NDT"],
        ["Full penetration butt weld as-welded", 90, "Reinforcement <= 10% of width with smooth transition, 100% NDT"],
        ["Transverse butt weld with permanent backing bar", 71, "Fillet weld connecting backing bar to plate"],
        ["Partial penetration butt weld", 36, "Root defect treated as non-destructive crack initiator"]
    ],
    "Fatigue detail categories for transverse butt welds",
    "100% non-destructive testing (NDT) required for categories 90 and above."
)

# Table 8.4
fatigue_detail_categories_weld_attachments_and_stiffeners = Table(
    ["Attachment length L", r"Detail category $\Delta\sigma_c$ [N/mm2]", "Description"],
    [
        ["Transverse stiffener welded to flange or web", 80, "Ends of welds cut back and ground smooth"],
        ["Longitudinal attachment L <= 50 mm", 80, "Ends of fillet welds ground smooth"],
        ["Longitudinal attachment 50 < L <= 100 mm", 71, "Fillet or butt welded gusset plates or brackets"],
        ["Longitudinal attachment 100 < L <= 200 mm", 63, "Fillet or butt welded gusset plates or brackets"],
        ["Longitudinal attachment L > 200 mm", 50, "Fillet or butt welded gusset plates or brackets"]
    ],
    "Fatigue detail categories for weld attachments and stiffeners",
    "L is the overall length of the attachment measured parallel to the direction of nominal stress."
)
