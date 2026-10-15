try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 3.1
reduction_factors_for_carbon_steel_at_elevated_temperatures = Table(
    [
        "Steel temperature [deg C]",
        r"Effective yield strength factor $k_{y,\theta} = f_{y,\theta} / f_y$",
        r"Proportional limit factor $k_{p,\theta} = f_{p,\theta} / f_y$",
        r"Elastic modulus factor $k_{E,\theta} = E_{a,\theta} / E_a$"
    ],
    [
        ["20", 1.000, 1.000, 1.000],
        ["100", 1.000, 1.000, 1.000],
        ["200", 1.000, 0.807, 0.900],
        ["300", 1.000, 0.613, 0.800],
        ["400", 1.000, 0.420, 0.700],
        ["500", 0.780, 0.360, 0.600],
        ["600", 0.470, 0.180, 0.310],
        ["700", 0.230, 0.075, 0.130],
        ["800", 0.110, 0.050, 0.090],
        ["900", 0.060, 0.0375, 0.0675],
        ["1000", 0.040, 0.025, 0.045],
        ["1100", 0.020, 0.0125, 0.0225],
        ["1200", 0.000, 0.000, 0.000]
    ],
    "Reduction factors for stress-strain relationship of carbon steel at elevated temperatures",
    "For intermediate values of steel temperature, linear interpolation may be used."
)

# Table 4.1
critical_temperature_for_utilisation_factor = Table(
    [r"Utilisation factor $\mu_0$", r"Critical temperature $\theta_{a,cr}$ [deg C]"],
    [
        [0.22, 711],
        [0.24, 698],
        [0.26, 685],
        [0.28, 674],
        [0.30, 664],
        [0.32, 654],
        [0.34, 645],
        [0.36, 636],
        [0.38, 628],
        [0.40, 620],
        [0.42, 612],
        [0.44, 605],
        [0.46, 598],
        [0.48, 591],
        [0.50, 585],
        [0.52, 578],
        [0.54, 572],
        [0.56, 566],
        [0.58, 560],
        [0.60, 554],
        [0.62, 549],
        [0.64, 543],
        [0.66, 537],
        [0.68, 531],
        [0.70, 526],
        [0.72, 520],
        [0.74, 514],
        [0.76, 508],
        [0.78, 502],
        [0.80, 496]
    ],
    "Critical temperature theta_a,cr for values of the utilisation factor mu_0",
    "Default values for critical temperatures in accordance with prEN 1993-1-2."
)

# Table D.1
strength_reduction_factors_for_bolts_and_welds_in_fire = Table(
    ["Temperature [deg C]", r"Reduction factor for bolts $k_b$ (Tension and shear)", r"Reduction factor for welds $k_w$"],
    [
        ["20", 1.000, 1.000],
        ["100", 0.968, 1.000],
        ["150", 0.952, 1.000],
        ["200", 0.935, 1.000],
        ["300", 0.903, 1.000],
        ["400", 0.775, 0.876],
        ["500", 0.550, 0.627],
        ["600", 0.220, 0.378],
        ["700", 0.100, 0.130],
        ["800", 0.067, 0.074],
        ["900", 0.033, 0.018],
        ["1000", 0.000, 0.000]
    ],
    "Strength Reduction Factors for Bolts and Welds in fire",
    "For full penetration butt welds at temperatures up to 700 deg C, use structural steel reduction factors."
)
