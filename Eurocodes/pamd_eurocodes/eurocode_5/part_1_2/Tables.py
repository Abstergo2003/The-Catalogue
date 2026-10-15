try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 2.1
values_of_k_fi_for_fire_design = Table(
    ["Material type", r"Factor $k_{fi}$", "Application"],
    [
        ["Solid timber", 1.25, "Bending, tension, compression strengths and MOE"],
        ["Glued laminated timber (glulam)", 1.15, "Bending, tension, compression strengths and MOE"],
        ["Laminated veneer lumber (LVL)", 1.10, "Edgewise bending and tension properties"],
        ["Plywood", 1.15, "Bending, tension, compression strengths"],
        ["Other wood-based panels (OSB, particleboards)", 1.15, "Bending and shear properties"]
    ],
    "Values of k_fi factor converting 5th percentile normal properties to 20th percentile fire properties (EN 1995-1-2 Table 2.1)",
    "f_20 = k_fi * f_k and E_20 = k_fi * E_05."
)

# Table 3.1
design_charring_rates_for_timber_and_wood_materials = Table(
    ["Material type", r"1D charring rate $\beta_0$ [mm/min]", r"Notional charring rate $\beta_n$ [mm/min]", "Characteristic density rho_k [kg/m3]"],
    [
        ["Softwood glued laminated timber", 0.65, 0.70, r"\ge 290"],
        ["Softwood solid timber", 0.65, 0.80, r"\ge 290"],
        ["Hardwood solid or glulam timber", 0.50, 0.55, r"\ge 450"],
        ["Laminated veneer lumber (LVL)", 0.65, 0.70, r"\ge 480"],
        ["Wood panelling and claddings", 0.90, 0.90, r"\ge 400"],
        ["Plywood panels", 1.00, 1.00, r"\ge 400"],
        ["Wood-based panels (OSB, particleboard)", 0.90, 0.90, r"\ge 600"]
    ],
    "Design charring rates beta_0 and beta_n of timber, glulam, and wood-based panels (EN 1995-1-2 Table 3.1)",
    "beta_0 applies to planar surfaces without corner effects; beta_n accounts for corner rounding in rectangular sections."
)

# Table 4.1
determination_of_k0_for_unprotected_surfaces = Table(
    ["Fire exposure duration t", r"Zero-strength coefficient $k_0$", r"Effective zero-strength depth $d_0$ [mm]"],
    [
        ["t < 20 minutes", r"t / 20", r"k_0 \cdot 7\text{ mm}"],
        ["t >= 20 minutes", 1.00, 7.0]
    ],
    "Determination of coefficient k0 for unprotected timber surfaces (EN 1995-1-2 Table 4.1)",
    "Effective charring depth d_ef = d_char,n + k_0 * d_0."
)

# Table 4.2
conversion_factors_eta_f_for_reduced_properties_method = Table(
    ["Stress type", "Factor eta_f (Solid timber)", "Factor eta_f (Glulam)"],
    [
        ["Bending strength f_m", 1.00, 1.00],
        ["Compressive strength f_c,0", 1.00, 1.00],
        ["Tensile strength f_t,0", 0.85, 0.90],
        ["Modulus of elasticity E_0", 0.85, 0.90]
    ],
    "Conversion factors eta_f for the reduced properties method (EN 1995-1-2 Table 4.2)",
    "Applied to the strength and stiffness of the residual cross-section."
)

# Table 6.1
fire_resistance_time_for_unprotected_timber_connections = Table(
    ["Fastener type in timber-to-timber joint", "Minimum side member thickness t1 [mm]", r"Standard fire resistance $t_{d,fi}$ [min]"],
    [
        ["Nails (without gap)", 28, 15],
        ["Nails (with extra edge cover >= 10 mm)", 45, 30],
        ["Screws (without gap)", 28, 15],
        ["Bolts (with washers)", 45, 15],
        ["Bolts with timber plugs / recessed", 60, 30],
        ["Dowels (embedded)", 45, 20]
    ],
    "Fire resistance duration t_d,fi of unprotected timber-to-timber connections (EN 1995-1-2 Clause 6.1 Table 6.1)",
    "Fire resistance can be increased up to 60 minutes by using thicker wood side members or fire-rated claddings."
)
