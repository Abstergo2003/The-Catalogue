try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 5.1
indicative_temperatures_of_inner_environment_Tin = Table(
    ["Season", "Temperature $T_{in}$ [deg C]"],
    [
        ["Summer", 20],
        ["Winter", 25]
    ],
    "Indicative temperatures of inner environment $T_{in}$",
    "NOTE: Recommended values when no local data are available: Summer T1 = 20 deg C, Winter T2 = 25 deg C."
)

# Table 5.2
indicative_temperatures_Tout_for_buildings_above_ground = Table(
    ["Season", "Surface absorptivity / colour", "Temperature $T_{out}$ [deg C]"],
    [
        ["Summer", "0.5 (bright light surface)", "$T_{max} + T_3$"],
        ["Summer", "0.7 (light coloured surface)", "$T_{max} + T_4$"],
        ["Summer", "0.9 (dark surface)", "$T_{max} + T_5$"],
        ["Winter", "All surfaces", "$T_{min}$"]
    ],
    "Indicative temperatures $T_{out}$ for buildings above the ground level",
    "For latitudes 45N to 55N: NE facing: T3=0, T4=2, T5=4 deg C; SW or horizontal: T3=18, T4=30, T5=42 deg C."
)

# Table 5.3
indicative_temperatures_Tout_for_underground_parts = Table(
    ["Depth below ground level", "Temperature $T_{out}$ [deg C]"],
    [
        ["Depth < 1.0 m", "Variable according to local seasonal conditions"],
        ["Depth >= 1.0 m", 8.0]
    ],
    "Indicative temperatures $T_{out}$ for underground parts of buildings",
    ""
)

# Table 6.1
recommended_values_of_linear_temperature_difference_component = Table(
    ["Type of Deck", "Top warmer than bottom $\\Delta T_{M,heat}$ [deg C]", "Bottom warmer than top $\\Delta T_{M,cool}$ [deg C]"],
    [
        ["Type 1: Steel deck", 18, 13],
        ["Type 2: Composite deck", 15, 18],
        ["Type 3: Concrete box girder", 10, 5],
        ["Type 3: Concrete beam", 15, 8],
        ["Type 3: Concrete slab", 15, 8]
    ],
    "Recommended values of linear temperature difference component for different types of bridge decks",
    "Based on surfacing depth of 50 mm. For other depths, multiply by ksur (Table 6.2)."
)

# Table 6.2
recommended_values_of_ksur_for_surfacing_depths = Table(
    ["Road / railway bridge deck surfacing depth", "Type 1: Steel deck", "Type 2: Composite deck", "Type 3: Concrete deck"],
    [
        ["Unsurfaced", 1.2, 1.1, 1.3],
        ["Surfaced 50 mm", 1.0, 1.0, 1.0],
        ["Surfaced 100 mm", 0.7, 0.8, 0.8],
        ["Ballasted railway track (100 mm ballast)", 0.6, 0.6, 0.6]
    ],
    "Recommended values of $k_{sur}$ to account for different surfacing depths",
    ""
)

# Table C.1
coefficients_of_linear_expansion = Table(
    ["Material", "Coefficient of linear expansion $\\alpha_T$ [$10^{-6}$ / deg C]"],
    [
        ["Aluminium, aluminium alloy", 24],
        ["Stainless steel", 16],
        ["Structural steel, wrought or cast iron", 12],
        ["Concrete (normal weight)", 10],
        ["Concrete (lightweight aggregate)", 7],
        ["Masonry", "6 to 10"],
        ["Timber, along grain", 5],
        ["Timber, across grain", "30 to 70"]
    ],
    "Coefficients of linear expansion $\\alpha_T$",
    "Values to be used for derivation of thermal actions."
)
