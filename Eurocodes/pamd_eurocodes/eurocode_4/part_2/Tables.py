try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 2.1
partial_safety_factors_for_composite_bridges = Table(
    ["Component / Limit state", r"Symbol $\gamma_M$", "Fundamental combination (ULS)", "Accidental combination", "Fatigue assessment"],
    [
        ["Concrete", r"\gamma_C", 1.50, 1.20, 1.00],
        ["Reinforcing steel", r"\gamma_S", 1.15, 1.00, 1.00],
        ["Structural steel (cross-sections)", r"\gamma_{a0}", 1.05, 1.00, None],
        ["Structural steel (instability)", r"\gamma_{a1}", 1.10, 1.00, None],
        ["Shear connection (headed studs)", r"\gamma_V", 1.25, 1.00, None],
        ["Fatigue of shear connection (damage tolerant)", r"\gamma_{Mf}", None, None, 1.00],
        ["Fatigue of shear connection (safe life)", r"\gamma_{Mf}", None, None, 1.15]
    ],
    "Partial safety factors for composite bridges (EN 1994-2 Clause 2.3.3.2 / DD ENV 1994-2)",
    "Recommended values for highway and railway composite bridges."
)

# Table 5.1
effective_span_length_parameters_for_shear_lag = Table(
    ["Span position / Boundary condition", r"Effective span length $L_e$", "Comment"],
    [
        ["Simply supported span (length L)", r"1.0 \cdot L", "Bending moment maximum at mid-span"],
        ["End span of continuous girder (length L1)", r"0.85 \cdot L_1", "Between end support and internal support"],
        ["Intermediate span of continuous girder (length Li)", r"0.70 \cdot L_i", "Between adjacent internal supports"],
        ["Internal support region (adjacent spans L1 and L2)", r"0.25 \cdot (L_1 + L_2)", "Negative hogging moment region"],
        ["Cantilever (length Lc)", r"2.0 \cdot L_c", "Fixed at support, free at end"]
    ],
    "Effective span length Le for shear lag effective width calculation in composite bridge girders (EN 1994-2 Figure 5.1)",
    "Effective width beff = b0 + sum(beta_i * b_i), where beta_i is determined as a function of Le / b_i."
)

# Table 6.1
fatigue_detail_categories_for_shear_connectors_in_bridges = Table(
    ["Fatigue detail / verification", r"Detail category $\Delta\tau_c$ or $\Delta\sigma_c$ [N/mm2]", "Inverse slope m", "Cut-off limit / Endurance limit"],
    [
        ["Headed studs in concrete slab (shear stress range)", 90, 8, r"\Delta\tau_L \text{ at } 10^8 \text{ cycles}"],
        ["Base metal in tension with automatic welded stud", 80, 3, r"\Delta\sigma_D \text{ at } 5 \cdot 10^6 \text{ cycles (m=5 beyond)}"],
        ["Base metal in tension with manual welded stud", 63, 3, r"\Delta\sigma_D \text{ at } 5 \cdot 10^6 \text{ cycles (m=5 beyond)}"]
    ],
    "Fatigue detail categories for shear connectors in composite bridges (EN 1994-2 Clause 6.8 / Table 6.8)",
    "Nominal stress ranges should be verified using cumulative damage according to Palmgren-Miner rule."
)

# Table 7.1
limiting_values_of_crack_width_for_composite_bridges = Table(
    ["Exposure Class", "Reinforced members (Frequent combination)", "Prestressed members with bonded tendons (Frequent)", "Prestressed members with bonded tendons (Quasi-permanent)"],
    [
        ["X0, XC1 (Dry / permanently wet)", "wk <= 0.3 mm", "wk <= 0.2 mm", "No tensile stress (decompression)"],
        ["XC2, XC3, XC4 (Moist / cycling)", "wk <= 0.3 mm", "wk <= 0.2 mm", "No tensile stress (decompression)"],
        ["XD1, XD2, XD3 (De-icing salts)", "wk <= 0.2 mm", "No tensile stress (decompression)", "No tensile stress (decompression)"],
        ["XS1, XS2, XS3 (Seawater / airborne salts)", "wk <= 0.2 mm", "No tensile stress (decompression)", "No tensile stress (decompression)"]
    ],
    "Recommended values of maximum crack width w_max for composite bridge decks (EN 1994-2 Clause 7.4 / EN 1992-2)",
    "For bridge decks subjected to de-icing salt sprays, crack width limitation to 0.2 mm or decompression is strictly enforced."
)

# Table 8.1
minimum_deck_slab_thickness_for_composite_bridges = Table(
    ["Bridge structure type", "Minimum slab thickness [mm]", "Minimum cover cnom [mm]", "Notes"],
    [
        ["Highway bridge deck (cast-in-situ)", 200, 35, "May be increased to 220 mm where waterproofing is applied directly"],
        ["Railway bridge deck (with ballast)", 250, 40, "Includes dynamic allowance for ballast maintenance tamping"],
        ["Footbridge deck (pedestrian / cycle)", 120, 25, "Minimum thickness governed by punching shear under maintenance vehicle"]
    ],
    "Minimum deck slab thickness and nominal concrete cover for composite bridges (EN 1994-2 Clause 8)",
    "Ensures structural durability, punching shear resistance, and cover to top and bottom reinforcement grids."
)
