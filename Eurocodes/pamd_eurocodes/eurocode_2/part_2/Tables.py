try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 1
values_to_be_used_in_referenced_clauses_for_bridges = Table(
    ["Clause reference", "Parameter definition", "Recommended bridge value"],
    [
        ["3.2.5.1 (5)", "Minimum shear strength of welds", "25 % of the tensile strength of the bar"],
        ["4.1.3.3 (8)", "Allowance for tolerance Delta_h in cover for precast elements", "Delta_h = 5 mm"],
        ["4.1.3.3 (8)", "Allowance for tolerance Delta_h in cover for in situ concrete", "Delta_h = 5 mm"],
        ["4.2.1.3.3 (12)", "Reduction factor for long-term loading effects on maximum compressive stress", "0.85"],
        ["4.2.3.4.1 (2)", "Ratio of long-term relaxation to 1000 h relaxation", "2.0"],
        ["4.3.2.4.4 (1)", "Limit to cot(theta) in variable strut inclination method for beams with constant reinforcement", "0.5 < cot(theta) < 2.0"],
        ["4.3.3.1 (6)", "Limits to cot(theta) in torsion calculation", "0.5 < cot(theta) < 2.0"],
        ["4.3.4.5.2 (1)", "VRd2 limitation factor", "2.0"],
        ["4.4.2.2.1 (103)", "Maximum bar spacing for crack control", "300 mm"],
        ["4.5.2 (103)", "Limit to average bearing stress", "0.8 fcd"]
    ],
    "Values to be used in referenced clauses instead of boxed values for concrete bridges",
    "Specific modifications and boxed value replacements for bridge structures."
)

# Table 3
bridge_exposure_classes = Table(
    ["Exposure class", "Description of environment", "Informative examples for bridges"],
    [
        ["1", "Dry interior", "Interior surfaces of box girders or superstructures with low air humidity"],
        ["2a", "Humidity without frost", "Exterior surfaces not exposed to de-icing salts or severe freezing"],
        ["2b", "Humidity with frost", "Exterior bridge components exposed to freezing but not to de-icing agents"],
        ["3", "Severe humidity with de-icing agents", "Bridge decks, parapet beams, pier columns, and abutments exposed to de-icing salt spray"],
        ["4a", "Seawater without frost", "Marine bridge substructures in contact with sea water or sea spray without freezing"],
        ["4b", "Seawater with frost", "Marine bridge substructures in splash/tidal zones exposed to frost"],
        ["5a", "Slightly aggressive chemical environment", "Bridge foundations in slightly contaminated soil or ground water"],
        ["5b", "Moderately aggressive chemical environment", "Bridge foundations in moderately aggressive industrial ground or water"],
        ["5c", "Highly aggressive chemical environment", "Bridge elements exposed to highly aggressive chemical agents"]
    ],
    "Exposure classes related to environmental conditions for concrete bridges",
    "Chemically aggressive environments are classified in ISO/DP9690."
)

# Table 4
nominal_cover_requirements_for_bridges = Table(
    ["Exposure class", "Location", "C20/25 [mm]", "C25/30 [mm]", "C30/37 [mm]", r"$\ge$ C40/50 [mm]"],
    [
        ["Class 1", "Other locations (3)", 55, 45, 40, 35],
        ["Class 2a", "Cast against earth face (2)", 80, 80, 80, 80],
        ["Class 2a", "Other locations (3)", "-", 55, 45, 40],
        ["Class 2b", "Cast against earth face (2)", "-", "80*", 80, 80],
        ["Class 2b", "Other locations (3)", "-", "55*", 45, 40],
        ["Class 3", "Directly exposed to de-icing agents (1)", "-", "-", "85*", 85],
        ["Class 3", "Cast against earth face (2)", "-", "-", "80*", 80],
        ["Class 3", "Other locations (3)", "-", "-", "60*", 50],
        ["Class 4a", "Directly exposed (1)", "-", "-", 85, 85],
        ["Class 4a", "Cast against earth face (2)", "-", "-", 80, 80],
        ["Class 4a", "Other locations (3)", "-", "-", 75, 65],
        ["Class 4b", "Directly exposed (1)", "-", "-", "85*", 85],
        ["Class 4b", "Cast against earth face (2)", "-", "-", "80*", 80],
        ["Class 4b", "Other locations (3)", "-", "-", "75*", 65]
    ],
    "Nominal cover requirements for normal weight concrete in bridges (mm)",
    "* Air entrained concrete should be specified. - indicates concrete grade not permitted. For pretensioned precast units tabulated values may be reduced by 10 mm. Parapet beams nominal cover = 70 mm."
)

# Table 5
effective_height_for_columns_in_bridges = Table(
    ["Case", "Top restraint (Position / Rotation)", "Bottom restraint (Position / Rotation)", r"Effective height $l_0$"],
    [
        ["Case 1", "Full / Full", "Full / Full", r"0.70 l_{col}"],
        ["Case 2", "Full / None", "Full / Full", r"0.85 l_{col}"],
        ["Case 3", "Full / None", "Full / None", r"1.00 l_{col}"],
        ["Case 4", "None / None (Elastomeric bearing)", "Full / Full", r"1.30 l_{col}"],
        ["Case 5", "None / None", "Full / Full", r"1.40 l_{col}"],
        ["Case 6", "None / Full", "Full / Full", r"1.50 l_{col}"],
        ["Case 7", "None / None (Cantilever pier)", "Full / Full", r"2.30 l_{col}"]
    ],
    "Effective height, l_0, for bridge columns and piers",
    "lcol is the clear height of the column between structural restraints."
)

# Table 6a
limiting_stress_ranges_longitudinal_bending_road_bridges = Table(
    [
        "Span [m]",
        r"Adjacent spans loaded ($\le 16$ mm) [N/mm2]",
        r"Adjacent spans loaded (> 16 mm) [N/mm2]",
        r"Alternate spans loaded ($\le 16$ mm) [N/mm2]",
        r"Alternate spans loaded (> 16 mm) [N/mm2]"
    ],
    [
        ["< 3.5", 150, 115, 210, 160],
        ["3.5 to 5.0", 125, 95, 175, 135],
        ["5.0 to 10.0", 110, 85, 175, 135],
        ["10.0 to 20.0", 110, 85, 140, 110],
        ["20.0 to 100.0", 90, 70, 110, 85],
        ["100.0 to 200.0", 115, 90, 135, 105],
        ["> 200.0", 190, 145, 200, 155]
    ],
    "Limiting stress ranges (N/mm2) - Longitudinal bending for unwelded reinforcing bars in road bridges",
    ""
)

# Table 6b
limiting_stress_ranges_transverse_bending_road_bridges = Table(
    ["Span [m]", r"Bars $\le 16$ mm [N/mm2]", r"Bars > 16 mm [N/mm2]"],
    [
        ["< 3.5", 210, 160],
        ["3.5 to 5.0", 120, 90],
        ["5.0 to 10.0", 70, 55]
    ],
    "Limiting stress ranges (N/mm2) - Transverse bending for unwelded reinforcing bars in road bridges",
    "Applies to deck slabs spanning transversely between longitudinal girders."
)

# Table 7
minimum_mandrel_diameters_for_bridges = Table(
    [
        "Type of reinforcement",
        r"Bar diameter $\phi < 20$ mm",
        r"Bar diameter $\phi \ge 20$ mm",
        r"Bent-up bars ($c > 100$ mm and $> 7\phi$)",
        r"Bent-up bars ($c > 50$ mm and $> 3\phi$)",
        r"Bent-up bars ($c \le 50$ mm and $\le 3\phi$)"
    ],
    [
        ["Plain bars S 250", r"4\phi", r"4\phi", r"7\phi", r"8.5\phi", r"11.4\phi"],
        ["High bond bars S 460", r"6\phi", r"8\phi", r"13\phi", r"15.7\phi", r"20.9\phi"]
    ],
    "Minimum diameters of mandrels for plain and high bond bars in bridges",
    "c is the minimum concrete cover perpendicular to the plane of curvature."
)

# Table 4.121
maximum_bar_spacing_for_high_bond_bars_in_bridges = Table(
    [
        r"Steel stress $\sigma_s$ or $\sigma_p$ [N/mm2]",
        "Pure flexure (reinforced sections) [mm]",
        "Pure tension (reinforced sections) [mm]",
        "Prestressed sections [mm]"
    ],
    [
        [80, "-", 300, 300],
        [120, "-", 250, 250],
        [160, 300, 200, 200],
        [200, 250, 150, 150],
        [240, 200, 125, 100],
        [280, 150, 75, 50],
        [320, 100, "-", "-"],
        [360, 50, "-", "-"]
    ],
    "Maximum bar spacing for high bond bars in concrete bridges",
    "Steel stress should be calculated under the relevant quasi-permanent load combination."
)
