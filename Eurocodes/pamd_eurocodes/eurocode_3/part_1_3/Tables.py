try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 1
partial_safety_factors_for_cold_formed_members = Table(
    ["Failure mode", "Symbol", "Recommended value"],
    [
        ["Resistance of cross-sections to yielding", r"$\gamma_{M0}$", 1.0],
        ["Resistance of members to instability (buckling)", r"$\gamma_{M1}$", 1.0],
        ["Resistance of connections", r"$\gamma_{M2}$", 1.25]
    ],
    "Partial safety factors for cold-formed members and sheeting",
    "Recommended values for building design in accordance with EN 1993-1-3."
)

# Table 3
values_of_k_factor_for_cold_forming_hardening = Table(
    ["Method of forming", "Factor k"],
    [
        ["Roll forming", 7.0],
        ["Other methods (e.g. press braking)", 5.0]
    ],
    "Values of factor k for calculation of average yield strength fya after cold forming",
    "Used in Expression fya = fyb + (k * n * t^2 / Ag) * (fu - fyb)."
)

# Table 5.1
reduction_factors_for_shear_lag_in_cold_formed_sections = Table(
    ["Ratio L_e / b_0", r"Factor $\psi_1$ (simple support)", r"Factor $\psi_2$ (continuous support)"],
    [
        [r"$\ge 25$", 1.00, 1.00],
        ["20", 0.96, 0.92],
        ["15", 0.91, 0.84],
        ["10", 0.82, 0.71],
        ["5", 0.62, 0.48]
    ],
    "Reduction factors psi for shear lag in thin-walled sections",
    "b0 is the flange outstand or half-width of an internal flange element, Le is the distance between points of zero moment."
)

# Table 8.4
bearing_resistance_of_fasteners_in_thin_gauge_steel = Table(
    ["Fastener type", "Sheet thickness range [mm]", "Design bearing resistance Fb,Rd"],
    [
        ["Self-tapping screws", r"$t < 1.0$", r"$2.5 \alpha f_u d t$"],
        ["Self-tapping screws", r"$1.0 \le t \le 2.0$", r"$2.5 \alpha f_u d t$"],
        ["Blind rivets", r"$t < 1.0$", r"$1.5 f_u d t$"],
        ["Blind rivets", r"$1.0 \le t \le 2.0$", r"$2.0 f_u d t$"]
    ],
    "Design bearing resistance of fasteners in thin-gauge steel",
    "d is the fastener diameter, t is the sheet thickness, fu is the tensile strength of the sheet."
)
