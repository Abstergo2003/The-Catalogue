try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 4.1
recommended_values_of_coefficients_psi_for_buildings = Table(
    ["Regions", "$\\psi_0$", "$\\psi_1$", "$\\psi_2$"],
    [
        ["Finland, Iceland, Norway, Sweden", 0.70, 0.50, 0.20],
        ["Remainder of other CEN member states, for sites located at altitude H > 1000 m above sea level", 0.70, 0.50, 0.20],
        ["Remainder of other CEN member states, for sites located at altitude H <= 1000 m above sea level", 0.50, 0.20, 0.00]
    ],
    "Recommended values of coefficients $\\psi_0$, $\\psi_1$ and $\\psi_2$ for different locations for buildings",
    "See EN 1990:2002 Table A1.1."
)

# Table 5.1
recommended_values_of_Ce_for_different_topographies = Table(
    ["Topography", "Exposure coefficient $C_e$"],
    [
        ["Windswept (flat unobstructed areas exposed on all sides)", 0.8],
        ["Normal (no significant removal of snow by wind)", 1.0],
        ["Sheltered (considerably lower than surrounding terrain or trees)", 1.2]
    ],
    "Recommended values of $C_e$ for different topographies",
    "a) Windswept: flat unobstructed areas exposed on all sides.\nb) Normal: areas where there is no significant removal of snow by wind.\nc) Sheltered: areas surrounded by high trees or higher construction works."
)

# Table 5.2
snow_load_shape_coefficients = Table(
    ["Angle of pitch of roof $\\alpha$", "$\\mu_1$", "$\\mu_2$"],
    [
        ["$0^\\circ \\le \\alpha \\le 30^\\circ$", 0.8, "$0.8 + 0.8 \\alpha / 30$"],
        ["$30^\\circ < \\alpha < 60^\\circ$", "$0.8(60 - \\alpha) / 30$", 1.6],
        ["$\\alpha \\ge 60^\\circ$", 0.0, "-"]
    ],
    "Snow load shape coefficients",
    "Values apply when snow is not prevented from sliding off the roof. With snow fences or parapets, mu1 should not be reduced below 0.8."
)

# Table A.1
design_situations_and_load_arrangements_for_different_locations = Table(
    ["Design situation", "Case A (No exceptional falls, no exceptional drift)", "Case B1 (Exceptional falls, no exceptional drift)", "Case B2 (No exceptional falls, exceptional drift)", "Case B3 (Exceptional falls, exceptional drift)"],
    [
        ["Persistent / transient", "Undrifted: mu_i * Ce * Ct * sk; Drifted: mu_i * Ce * Ct * sk", "Undrifted: mu_i * Ce * Ct * sk; Drifted: mu_i * Ce * Ct * sk", "Undrifted: mu_i * Ce * Ct * sk; Drifted: mu_i * Ce * Ct * sk", "Undrifted: mu_i * Ce * Ct * sk; Drifted: mu_i * Ce * Ct * sk"],
        ["Accidental", "None", "Undrifted: mu_i * Ce * Ct * Cesl * sk; Drifted: mu_i * Ce * Ct * Cesl * sk", "Drifted: mu_i * sk (Annex B)", "Undrifted: mu_i * Ce * Ct * Cesl * sk; Drifted: mu_i * sk (Annex B)"]
    ],
    "Design Situations and load arrangements to be used for different locations",
    "Exceptional conditions are defined according to National Annex. Recommended Cesl = 2.0."
)

# Table E.1
mean_bulk_weight_density_of_snow = Table(
    ["Type of snow", "Bulk weight density [kN/m3]"],
    [
        ["Fresh", 1.0],
        ["Settled (several hours or days after its fall)", 2.0],
        ["Old (several weeks or months after its fall)", "2.5 to 3.5"],
        ["Wet", 4.0]
    ],
    "Mean bulk weight density of snow",
    "Indicative values for mean bulk weight density of snow on the ground."
)
