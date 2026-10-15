try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 12.1 (EN 1992-1-1 Section 12 / ENV 1992-1-6)
values_of_beta_for_different_edge_conditions = Table(
    [
        "Lateral restraint",
        r"Ratio $b/l_w = 0.2$",
        r"Ratio $b/l_w = 0.4$",
        r"Ratio $b/l_w = 0.6$",
        r"Ratio $b/l_w = 0.8$",
        r"Ratio $b/l_w = 1.0$",
        r"Ratio $b/l_w = 1.5$",
        r"Ratio $b/l_w = 2.0$",
        r"Ratio $b/l_w = 5.0$"
    ],
    [
        ["Along two edges (top and bottom)", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        ["Along three edges (top, bottom, one transverse wall)", 0.26, 0.59, 0.76, 0.85, 0.90, 0.95, 0.97, 1.00],
        ["Along four edges (top, bottom, two transverse walls)", 0.10, 0.20, 0.30, 0.40, 0.50, 0.69, 0.80, 0.96]
    ],
    "Values of beta for different edge conditions of plain concrete walls",
    "b is the clear horizontal length of the wall, lw is the clear height. For cantilever columns or walls beta = 2.0."
)

# Table 1
values_to_be_used_in_referenced_clauses_for_plain_concrete = Table(
    ["Clause reference", "Parameter definition", "Recommended value"],
    [
        ["5.4.7.1 (101)", "Minimum thickness of plain in-situ walls (depth, hw)", "120 mm (UK NAD recommends 150 mm)"],
        ["5.4.10 (101)", "Ratio of depth to projection of strip footing (hF/a)", "2.0 (UK NAD recommends 1.5)"]
    ],
    "Values to be used in referenced clauses for plain concrete structures",
    "Specific modifications and boxed value replacements for plain and lightly reinforced concrete."
)
