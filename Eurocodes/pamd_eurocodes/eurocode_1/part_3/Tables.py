try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 2.1
dynamic_factors_phi_i = Table(
    ["Dynamic factor", "Effects considered", "Applied to"],
    [
        ["$\\varphi_1$", "Vibrational excitation of crane structure due to lifting off ground", "Selfweight of crane $Q_c$"],
        ["$\\varphi_2$", "Dynamic increment on hoist load from lifting ungrounded payload", "Hoistload $Q_h$"],
        ["$\\varphi_3$", "Dynamic increment from sudden release of payload (grabs, magnets)", "Hoistload $Q_h$"],
        ["$\\varphi_4$", "Dynamic effects caused by travelling on uneven runway rails", "Selfweight $Q_c$ and Hoistload $Q_h$"],
        ["$\\varphi_5$", "Dynamic effects from acceleration or deceleration of drive forces", "Drive forces $K$ and inertia forces"]
    ],
    "Dynamic factors $\\varphi_i$",
    "Dynamic factors account for vibrational pulses and inertial effects."
)

# Table 2.4
dynamic_factors_for_vertical_loads = Table(
    ["Dynamic factor", "Formula / Value", "Remarks"],
    [
        ["$\\varphi_1$", BRange(0.9, 1.1, 1.1), "Reflects upper and lower values of vibrational pulses"],
        ["$\\varphi_2$", "$\\varphi_{2,min} + \\beta_2 v_h$", "vh is steady hoisting speed [m/s]; beta2, phi_2,min from Table 2.5"],
        ["$\\varphi_3$", "$1 - (\\Delta m / m)(1 + \\beta_3)$", "beta3 = 0.5 for grabs, beta3 = 1.0 for magnets"],
        ["$\\varphi_4$", 1.0, "Provided rail tolerances comply with specifications"]
    ],
    "Dynamic factors $\\varphi_i$ for vertical loads",
    ""
)

# Table 2.5
values_of_beta2_and_phi2_min = Table(
    ["Hoisting class", "$\\beta_2$", "$\\varphi_{2,min}$"],
    [
        ["HC1", 0.17, 1.05],
        ["HC2", 0.34, 1.10],
        ["HC3", 0.51, 1.15],
        ["HC4", 0.68, 1.20]
    ],
    "Values of $\\beta_2$ and $\\varphi_{2,min}$ according to hoisting classes",
    "Hoisting classes HC1 to HC4 defined in EN 13001-1."
)

# Table A.2
psi_factors_for_crane_loads = Table(
    ["Action", "Symbol", "$\\psi_0$", "$\\psi_1$", "$\\psi_2$"],
    [
        ["Single crane or groups of loads induced by cranes", "$Q_r$", 1.0, 0.9, "Permanent / total ratio"]
    ],
    "$\\psi$ factors for crane loads",
    "psi_2 is ratio between permanent crane action and total crane action."
)
