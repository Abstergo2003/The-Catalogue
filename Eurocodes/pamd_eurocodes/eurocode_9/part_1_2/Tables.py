"""Eurocode 9 - Part 1-2: Structural fire design - Tables.
EN 1999-1-2 / ENV 1999-1-2.
"""
try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange


# Table 3.1
strength_reduction_factors_fire = Table(
    ["Temperature theta_a [deg C]", "Proof strength factor k_theta,p0.2", "Tensile strength factor k_theta,u", "Elastic modulus factor k_theta,E"],
    [
        [20, 1.00, 1.00, 1.00],
        [100, 0.95, 0.95, 0.95],
        [150, 0.80, 0.82, 0.88],
        [200, 0.50, 0.55, 0.77],
        [250, 0.25, 0.32, 0.60],
        [300, 0.12, 0.18, 0.40],
        [350, 0.05, 0.08, 0.20],
        [400, 0.02, 0.03, 0.05]
    ],
    "Reduction factors for strength and elasticity of structural aluminium alloys at elevated temperatures (EN 1999-1-2 Table 3.1)",
    "Shows rapid degradation of strength and stiffness in aluminium starting above 150 deg C."
)

# Table 3.2
thermal_properties_aluminium_fire = Table(
    ["Property", "Symbol", "Representative value / expression", "Unit"],
    [
        ["Thermal conductivity", "lambda_a", "160 to 210", "W/(m*K)"],
        ["Specific heat capacity", "c_a", "900 to 1100", "J/(kg*K)"],
        ["Surface emissivity (uncoated aluminium)", "epsilon_m", 0.30, "-"],
        ["Surface emissivity (coated/anodised/painted)", "epsilon_m", 0.70, "-"]
    ],
    "Thermal material properties of structural aluminium alloys at elevated temperatures (EN 1999-1-2 Clause 3.3)",
    "Governs convective and radiative transient heat transfer into aluminium cross-sections during fire."
)

# Table 2.1
fire_partial_safety_factors = Table(
    ["Design situation", "Symbol", "Design value"],
    [
        ["Fire design situation (mechanical resistance)", "gamma_M,fi", 1.00]
    ],
    "Partial factor for fire design situation (EN 1999-1-2 Clause 2.3)",
    "Accidental limit state design value for verifying load-bearing capacity under fire exposure."
)
