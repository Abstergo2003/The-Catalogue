try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 2.1
importance_classes_and_factors_for_bridges = Table(
    ["Importance Class", "Description / Function", r"Recommended importance factor $\gamma_I$"],
    [
        ["Class I (Minor)", "Bridges of secondary importance with light traffic, whose destruction does not disrupt communications", 0.80],
        ["Class II (Average)", "Standard highway and railway bridges not categorized in Class I or III", 1.00],
        ["Class III (Critical)", "Major bridges critical for emergency routes, high economic importance, or carrying vital lifelines", 1.30]
    ],
    "Importance classes and importance factors gamma_I for bridges (EN 1998-2 Clause 2.1)",
    "Seismic design acceleration for bridges a_g = gamma_I * a_gR."
)

# Table 2.2
maximum_behavior_factors_q_for_bridge_piers = Table(
    ["Structural type / Substructure", "Ductile behavior (DCH)", "Limited ductile behavior (DCL)"],
    [
        ["Reinforced concrete vertical single-column piers in bending", 3.5, 1.5],
        ["Reinforced concrete framed bents with two or more columns", 3.5, 1.5],
        ["Piers with inclined struts / V-piers", 2.0, 1.2],
        ["Steel piers / columns (moment resisting)", 3.5, 1.5],
        ["Piers designed to resist shear without bending yielding", 1.0, 1.0],
        ["Abutments rigidly connected to the deck", 1.5, 1.0]
    ],
    "Maximum values of behavior factor q for bridge substructures (EN 1998-2 Table 4.1)",
    "Applied in response spectrum analysis of bridge piers subjected to horizontal seismic excitation."
)

# Table 4.1
target_displacement_ductility_factors_for_bridge_piers = Table(
    ["Behavior factor q", r"Fundamental period $T \ge T_C$", r"Short period $T < T_C$"],
    [
        [1.5, 1.5, 1.7],
        [2.0, 2.0, 2.5],
        [3.0, 3.0, 4.2],
        [3.5, 3.5, 5.0]
    ],
    "Target displacement ductility factors mu_d for bridge piers (EN 1998-2 Clause 4.1)",
    "For T >= TC: mu_d = q; for T < TC: mu_d = 1 + (q - 1) * (TC / T)."
)

# Table 7.1
minimum_overlap_length_to_prevent_span_unseating = Table(
    ["Support type", r"Minimum overlap length $L_{ov}$ [mm]", "Formula / Verification"],
    [
        ["Abutment or pier cap bearing seat (standard)", 400, r"L_{ov} \ge 400\text{ mm} + 0.005 \cdot L_{eff}"],
        ["Expansion joint between adjacent spans", 500, r"L_{ov} \ge 500\text{ mm} + 0.005 \cdot (L_1 + L_2)"],
        ["Intermediate hinge in suspended span", 400, r"L_{ov} \ge 400\text{ mm} + 0.008 \cdot L_{eff}"]
    ],
    "Minimum overlap length Lov at bridge expansion joints and bearing seats (EN 1998-2 Clause 6.6)",
    "Prevents unseating failure when longitudinal relative displacements occur under earthquake shaking."
)
