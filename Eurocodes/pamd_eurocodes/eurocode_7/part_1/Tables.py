try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table A.1
partial_factors_on_actions_for_EQU = Table(
    ["Action type", r"Symbol $\gamma_F$", "Unfavourable (Destabilising)", "Favourable (Stabilising)"],
    [
        ["Permanent action", r"\gamma_G", 1.10, 0.90],
        ["Variable action", r"\gamma_Q", 1.50, 0.00]
    ],
    "Partial factors on actions (gamma_F) for equilibrium limit state EQU (EN 1997-1 Table A.1)",
    "Applied for checking static equilibrium of rigid structures against overturning or sliding."
)

# Table A.2
partial_factors_for_soil_parameters_for_EQU = Table(
    ["Soil parameter", r"Symbol $\gamma_M$", "Value"],
    [
        ["Angle of shearing resistance (applied to tan phi')", r"\gamma_{\phi'}", 1.25],
        ["Effective cohesion", r"\gamma_{c'}", 1.25],
        ["Undrained shear strength", r"\gamma_{cu}", 1.40],
        ["Unconfined compressive strength", r"\gamma_{qu}", 1.40],
        ["Weight density", r"\gamma_\gamma", 1.00]
    ],
    "Partial factors for ground properties gamma_M for equilibrium limit state EQU (EN 1997-1 Table A.2)",
    "Applied to characteristic values to obtain design values in equilibrium checks."
)

# Table A.3
partial_factors_on_actions_for_STR_and_GEO = Table(
    ["Action type", r"Symbol $\gamma_F$", "Set A1 (Unfavourable)", "Set A1 (Favourable)", "Set A2 (Unfavourable)", "Set A2 (Favourable)"],
    [
        ["Permanent action", r"\gamma_G", 1.35, 1.00, 1.00, 1.00],
        ["Variable action", r"\gamma_Q", 1.50, 0.00, 1.30, 0.00]
    ],
    "Partial factors on actions (gamma_F) or effects of actions (gamma_E) for STR and GEO (EN 1997-1 Table A.3)",
    "Set A1 represents upper action factors; Set A2 represents service/moderate action factors used in DA1 Combination 2 and DA3."
)

# Table A.4
partial_factors_for_soil_parameters_for_STR_and_GEO = Table(
    ["Ground parameter", r"Symbol $\gamma_M$", "Set M1 (Unfactored)", "Set M2 (Factored)"],
    [
        ["Angle of shearing resistance (applied to tan phi')", r"\gamma_{\phi'}", 1.00, 1.25],
        ["Effective cohesion", r"\gamma_{c'}", 1.00, 1.25],
        ["Undrained shear strength", r"\gamma_{cu}", 1.00, 1.40],
        ["Unconfined compressive strength", r"\gamma_{qu}", 1.00, 1.40],
        ["Weight density", r"\gamma_\gamma", 1.00, 1.00]
    ],
    "Partial factors for ground properties gamma_M for STR and GEO limit states (EN 1997-1 Table A.4)",
    "Design value tan phi'_d = tan phi'_k / gamma_phi'; c'_d = c'_k / gamma_c'; cu_d = cu_k / gamma_cu."
)

# Table A.5
partial_resistance_factors_for_spread_foundations = Table(
    ["Resistance type", r"Symbol $\gamma_R$", "Set R1", "Set R2", "Set R3"],
    [
        ["Bearing capacity resistance", r"\gamma_{R,v}", 1.00, 1.40, 1.00],
        ["Sliding resistance", r"\gamma_{R,h}", 1.00, 1.10, 1.00]
    ],
    "Partial resistance factors gamma_R for spread foundations (EN 1997-1 Table A.5)",
    "Design bearing resistance R_v,d = R_v,k / gamma_R,v; design sliding resistance R_h,d = R_h,k / gamma_R,h."
)

# Table A.6
partial_resistance_factors_for_pile_foundations = Table(
    ["Pile category", "Resistance component", r"Symbol $\gamma_R$", "Set R1", "Set R2", "Set R3", "Set R4"],
    [
        ["Driven piles", "Base resistance", r"\gamma_b", 1.00, 1.10, 1.00, 1.30],
        ["Driven piles", "Shaft resistance (compression)", r"\gamma_s", 1.00, 1.10, 1.00, 1.30],
        ["Driven piles", "Total compression resistance", r"\gamma_t", 1.00, 1.10, 1.00, 1.30],
        ["Driven piles", "Shaft resistance in tension", r"\gamma_{s,t}", 1.25, 1.15, 1.10, 1.60],
        ["Bored piles", "Base resistance", r"\gamma_b", 1.25, 1.10, 1.00, 1.60],
        ["Bored piles", "Shaft resistance (compression)", r"\gamma_s", 1.00, 1.10, 1.00, 1.30],
        ["Bored piles", "Total compression resistance", r"\gamma_t", 1.15, 1.10, 1.00, 1.50],
        ["Bored piles", "Shaft resistance in tension", r"\gamma_{s,t}", 1.25, 1.15, 1.10, 1.60],
        ["CFA piles", "Base resistance", r"\gamma_b", 1.10, 1.10, 1.00, 1.45],
        ["CFA piles", "Shaft resistance (compression)", r"\gamma_s", 1.00, 1.10, 1.00, 1.30],
        ["CFA piles", "Total compression resistance", r"\gamma_t", 1.10, 1.10, 1.00, 1.40],
        ["CFA piles", "Shaft resistance in tension", r"\gamma_{s,t}", 1.25, 1.15, 1.10, 1.60]
    ],
    "Partial resistance factors for pile foundations in compression and tension (EN 1997-1 Tables A.6 - A.8)",
    "Applied in Design Approach 1 (Set R1 or R4) and Design Approach 2 (Set R2)."
)

# Table A.7
correlation_factors_xi_for_static_pile_tests = Table(
    ["Number of test piles n", r"Correlation factor $\xi_1$ (mean)", r"Correlation factor $\xi_2$ (minimum)"],
    [
        ["n = 1", 1.40, 1.40],
        ["n = 2", 1.30, 1.20],
        ["n = 3", 1.20, 1.05],
        ["n = 4", 1.10, 1.00],
        ["n >= 5", 1.00, 1.00]
    ],
    "Correlation factors xi to derive characteristic pile resistance from static pile load tests (EN 1997-1 Table A.9)",
    "R_k = min(mean(R_measured) / xi_1, min(R_measured) / xi_2)."
)

# Table A.8
partial_resistance_factors_for_retaining_structures = Table(
    ["Resistance type", r"Symbol $\gamma_R$", "Set R1", "Set R2", "Set R3"],
    [
        ["Bearing capacity", r"\gamma_{R,v}", 1.00, 1.40, 1.00],
        ["Sliding resistance", r"\gamma_{R,h}", 1.00, 1.10, 1.00],
        ["Earth resistance (passive)", r"\gamma_{R,e}", 1.00, 1.40, 1.00]
    ],
    "Partial resistance factors for retaining structures (EN 1997-1 Table A.13)",
    "Used in verification of overall stability, base sliding, and passive earth resistance against walls."
)

# Table A.9
partial_factors_for_uplift_limit_state_UPL = Table(
    ["Action / Parameter", r"Symbol $\gamma$", "Unfavourable / Destabilising", "Favourable / Stabilising"],
    [
        ["Permanent vertical action", r"\gamma_{G,dst} / \gamma_{G,stb}", 1.00, 0.90],
        ["Variable vertical action", r"\gamma_{Q,dst}", 1.50, 0.00],
        ["Shearing resistance (tan phi')", r"\gamma_{\phi'}", 1.25, None],
        ["Effective cohesion", r"\gamma_{c'}", 1.25, None],
        ["Undrained shear strength", r"\gamma_{cu}", 1.40, None],
        ["Tensile pile shaft resistance", r"\gamma_{s,t}", 1.40, None],
        ["Anchorage tensile resistance", r"\gamma_R", 1.40, None]
    ],
    "Partial factors for uplift limit state UPL verifications (EN 1997-1 Table A.15)",
    "Verifies that destabilising uplift actions V_dst,d <= stabilizing resistance V_stb,d + R_d."
)

# Table A.10
partial_factors_for_hydraulic_heave_limit_state_HYD = Table(
    ["Action type", r"Symbol $\gamma_F$", "Unfavourable (Destabilising)", "Favourable (Stabilising)"],
    [
        ["Permanent total pore water pressure / seepage", r"\gamma_{G,dst} / \gamma_{G,stb}", 1.35, 0.90],
        ["Variable seepage / water pressure", r"\gamma_{Q,dst}", 1.50, 0.00]
    ],
    "Partial factors for hydraulic heave limit state HYD verification (EN 1997-1 Table A.16)",
    "Verifies safety against ground boiling and hydraulic heave below excavations."
)

# Table D.1
bearing_capacity_factors_N_factors = Table(
    [r"Friction angle $\phi'$ [°]", r"Overburden factor $N_q$", r"Cohesion factor $N_c$", r"Unit weight factor $N_\gamma$"],
    [
        [0, 1.00, 5.14, 0.00],
        [5, 1.57, 6.49, 0.10],
        [10, 2.47, 8.35, 0.52],
        [15, 3.94, 10.98, 1.58],
        [20, 6.40, 14.83, 3.93],
        [25, 10.66, 20.72, 8.95],
        [28, 14.72, 25.80, 14.83],
        [30, 18.40, 30.14, 20.72],
        [32, 23.18, 35.49, 28.77],
        [35, 33.30, 46.12, 45.23],
        [38, 48.93, 61.35, 74.07],
        [40, 64.20, 75.31, 106.05],
        [42, 85.38, 93.71, 153.98],
        [45, 134.88, 133.88, 271.76]
    ],
    "Analytical bearing capacity factors Nq, Nc, and N_gamma for shallow spread foundations (EN 1997-1 Annex D)",
    "Nq = e^(pi * tan phi') * tan^2(45 + phi'/2); Nc = (Nq - 1) * cot phi'; N_gamma = 2 * (Nq - 1) * tan phi'."
)
