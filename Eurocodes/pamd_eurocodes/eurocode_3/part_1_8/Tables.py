try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 2.1
partial_safety_factors_for_joints = Table(
    ["Joint component / Resistance", "Symbol", "Recommended value"],
    [
        ["Resistance of bolts, rivets, pins, welds and plates in bearing", r"$\gamma_{M2}$", 1.25],
        ["Slip resistance at ultimate limit state (Category C)", r"$\gamma_{M3}$", 1.25],
        ["Slip resistance at serviceability limit state (Category B)", r"$\gamma_{M3,ser}$", 1.10],
        ["Bearing resistance of an injection bolt", r"$\gamma_{M4}$", 1.00],
        ["Resistance of joints in hollow section lattice girders", r"$\gamma_{M5}$", 1.00],
        ["Resistance of pins at SLS", r"$\gamma_{M6,ser}$", 1.00],
        ["Preload of high strength bolts", r"$\gamma_{M7}$", 1.10]
    ],
    "Partial safety factors for joints",
    "Recommended values in accordance with EN 1993-1-8."
)

# Table 3.1
minimum_and_maximum_spacings_and_edge_distances = Table(
    ["Distance / Spacing", "Minimum", "Maximum (Steels conforming to EN 10025)", "Maximum (Steels conforming to EN 10025-5)"],
    [
        ["End distance e1 (direction of load transfer)", r"$1.2 d_0$", r"$4 t + 40 \text{ mm}$", r"$\max(8t, 125 \text{ mm})$"],
        ["Edge distance e2 (perpendicular to load transfer)", r"$1.2 d_0$", r"$4 t + 40 \text{ mm}$", r"$\max(8t, 125 \text{ mm})$"],
        ["Spacing p1 (direction of load transfer)", r"$2.2 d_0$", r"$\min(14t, 200 \text{ mm})$", r"$\min(14t, 175 \text{ mm})$"],
        ["Spacing p2 (perpendicular to load transfer)", r"$2.4 d_0$", r"$\min(14t, 200 \text{ mm})$", r"$\min(14t, 175 \text{ mm})$"]
    ],
    "Minimum and maximum spacings, end and edge distances",
    "d0 is the hole diameter, t is the thickness of the thinner outer connected part."
)

# Table 3.4
design_resistance_for_individual_fasteners = Table(
    ["Failure mode", "Fastener / Criterion", "Design resistance formula"],
    [
        ["Shear resistance per shear plane", "Shear plane passes through unthreaded shank", r"$F_{v,Rd} = 0.6 f_{ub} A / \gamma_{M2}$"],
        ["Shear resistance per shear plane", "Shear plane passes through threads (classes 4.6, 5.6, 8.8)", r"$F_{v,Rd} = 0.6 f_{ub} A_s / \gamma_{M2}$"],
        ["Shear resistance per shear plane", "Shear plane passes through threads (classes 4.8, 5.8, 6.8, 10.9)", r"$F_{v,Rd} = 0.5 f_{ub} A_s / \gamma_{M2}$"],
        ["Bearing resistance", "Bolts in normal holes", r"$F_{b,Rd} = k_1 \alpha_b f_u d t / \gamma_{M2}$"],
        ["Tension resistance", "Bolt loaded in tension", r"$F_{t,Rd} = 0.9 f_{ub} A_s / \gamma_{M2}$"],
        ["Punching shear resistance", "Bolt head or nut punching through plate", r"$B_{p,Rd} = 0.6 \pi d_m t_p f_u / \gamma_{M2}$"]
    ],
    "Design resistance for individual fasteners subject to shear and/or tension",
    "alpha_b = min(alpha_d, fub/fu, 1.0); k1 = min(2.8 * e2/d0 - 1.7, 2.5) for edge bolts; dm is the mean diameter of the bolt head or nut."
)

# Table 4.1
correlation_factor_beta_w_for_fillet_welds = Table(
    ["Standard and steel grade", r"Ultimate tensile strength $f_u$ [N/mm2]", r"Correlation factor $\beta_w$"],
    [
        ["EN 10025: S 235", 360, 0.80],
        ["EN 10025: S 275", 430, 0.85],
        ["EN 10025: S 355", 510, 0.90],
        ["EN 10025: S 420", 520, 1.00],
        ["EN 10025: S 460", 540, 1.00]
    ],
    "Correlation factor beta_w for fillet welds",
    "Used in the directional method for fillet weld resistance: sigma_eq = sqrt(sigma_perp^2 + 3*(tau_perp^2 + tau_par^2)) <= fu / (beta_w * gamma_M2)."
)

# Table 5.1
joint_classification_boundaries_by_rotational_stiffness = Table(
    ["Zone / Joint type", "Classification boundary", "Condition"],
    [
        ["Zone 1: Rigid", r"$S_{j,ini} \ge k_b E I_b / L_b$", "kb = 8 for frames with bracing reducing sway by at least 80%; kb = 25 for other frames"],
        ["Zone 2: Semi-rigid", r"$0.5 E I_b / L_b < S_{j,ini} < k_b E I_b / L_b$", "Rotational stiffness modifies frame moments and sway"],
        ["Zone 3: Nominally pinned", r"$S_{j,ini} \le 0.5 E I_b / L_b$", "Capable of transmitting forces without developing significant moments"]
    ],
    "Joint classification boundaries by rotational stiffness",
    "Ib is the second moment of area of the connected beam, Lb is the beam span."
)
