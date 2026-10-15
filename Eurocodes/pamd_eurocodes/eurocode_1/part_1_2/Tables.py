try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table E.1
factors_delta_q1_delta_q2 = Table(
    ["Floor area $A_f$ [m2]", "Danger of fire activation $\\delta_{q1}$", "Examples of Occupancies", "Danger of fire activation $\\delta_{q2}$"],
    [
        ["25", 0.78, "artgallery, museum, swimming pool", 0.78],
        ["250", 1.00, "offices, residence, hotel, paper industry", 1.00],
        ["2500", 1.22, "manufactory for machinery & engines", 1.22],
        ["5000", 1.44, "chemical laboratory, painting workshop", 1.44],
        ["10000", 1.66, "manufactory of fireworks or paints", 1.66]
    ],
    "Factors $\\delta_{q1}$, $\\delta_{q2}$",
    "Factors taking into account the fire activation risk due to the size of the compartment (delta_q1) and the type of occupancy (delta_q2)."
)

# Table E.2
factors_delta_ni = Table(
    ["Active Fire Fighting Measure", "Symbol", "Factor $\\delta_{ni}$"],
    [
        ["Automatic Water Extinguishing System (sprinklers)", "$\\delta_{n1}$", 0.61],
        ["Independent Water Supplies", "$\\delta_{n2}$", "0.87 or 0.73"],
        ["Automatic fire detection & alarm by heat", "$\\delta_{n3}$", 0.87],
        ["Automatic fire detection & alarm by smoke", "$\\delta_{n4}$", 0.73],
        ["Automatic alarm transmission to fire brigade", "$\\delta_{n5}$", 0.87],
        ["Work fire brigade", "$\\delta_{n6}$", "0.61 or 0.78"],
        ["Off site fire brigade", "$\\delta_{n7}$", 0.78],
        ["Safe access routes", "$\\delta_{n8}$", "0.9 or 1.0 or 1.5"],
        ["Fire fighting devices", "$\\delta_{n9}$", "1.0 or 1.5"],
        ["Smoke exhaust system", "$\\delta_{n10}$", "1.0 or 1.5"]
    ],
    "Factors $\\delta_{ni}$ for active fire fighting measures",
    "NOTE: For normal fire fighting measures (safe access routes, devices, smoke exhaust) take 1.0; if not foreseen, take 1.5."
)

# Table E.3
net_calorific_values_Hu_of_combustible_materials = Table(
    ["Material", "Net calorific value $H_u$ [MJ/kg]"],
    [
        ["Wood", 17.5],
        ["Other cellulosic materials (clothes, cork, cotton, paper, silk, straw, wool)", 20.0],
        ["Carbon (anthracite, charcoal, coal)", 30.0],
        ["Chemicals: Paraffin series (methane, ethane, propane, butane)", 50.0],
        ["Chemicals: Olefin series (ethylene, propylene, butene)", 45.0],
        ["Chemicals: Aromatic series (benzene, toluene)", 40.0],
        ["Alcohols (methanol, ethanol, ethyl alcohol)", 30.0],
        ["Fuels (gasoline, petroleum, diesel)", 45.0],
        ["Pure hydrocarbons plastics (polyethylene, polystyrene, polypropylene)", 40.0],
        ["Other products: ABS (plastic)", 35.0],
        ["Other products: Polyester (plastic)", 30.0],
        ["Other products: Polyurethane (plastic)", 25.0],
        ["Other products: Polyvinylchloride, PVC (plastic)", 20.0],
        ["Other products: Bitumen, asphalt", 40.0],
        ["Other products: Leather", 20.0],
        ["Other products: Linoleum", 20.0],
        ["Other products: Rubber tyre", 30.0]
    ],
    "Net calorific values $H_u$ [MJ/kg] of combustible materials for calculation of fire loads",
    "Values not applicable for calculating energy content of fuels."
)

# Table E.4
fire_load_densities_qfk_for_different_occupancies = Table(
    ["Occupancy", "Average $q_{f,k}$ [MJ/m2]", "80% Fractile $q_{f,k}$ [MJ/m2]"],
    [
        ["Dwelling", 780, 948],
        ["Hospital (room)", 230, 280],
        ["Hotel (room)", 310, 377],
        ["Library", 1500, 1824],
        ["Office", 420, 511],
        ["Classroom of a school", 285, 347],
        ["Shopping centre", 600, 730],
        ["Theatre (cinema)", 300, 365],
        ["Transport (public space)", 100, 122]
    ],
    "Fire load densities $q_{f,k}$ [MJ/m2] for different occupancies",
    "Gumbel distribution is assumed for the 80% fractile."
)

# Table E.5
fire_growth_rate_and_RHRf_for_different_occupancies = Table(
    ["Occupancy", "Fire growth rate", "$t_\\alpha$ [s]", "Max Rate of heat release $RHR_f$ [kW/m2]"],
    [
        ["Dwelling", "Medium", 300, 250],
        ["Hospital (room)", "Medium", 300, 250],
        ["Hotel (room)", "Medium", 300, 250],
        ["Library", "Fast", 150, 500],
        ["Office", "Medium", 300, 250],
        ["Classroom of a school", "Medium", 300, 250],
        ["Shopping centre", "Fast", 150, 250],
        ["Theatre (cinema)", "Fast", 150, 500],
        ["Transport (public space)", "Slow", 600, 250]
    ],
    "Fire growth rate and $RHR_f$ for different occupancies",
    "t_alpha is time needed to reach a rate of heat release of 1 MW."
)

# Table F.1
correction_factor_kc = Table(
    ["Cross-section material", "Correction factor $k_c$"],
    [
        ["Reinforced concrete", "1.0"],
        ["Protected steel", "1.0"],
        ["Not protected steel", "13.7 * O"]
    ],
    "Correction factor $k_c$ in order to cover various materials",
    "O is the opening factor defined in Annex A."
)

# Table F.2
conversion_factor_kb = Table(
    ["Thermal absorptivity $b = \\sqrt{\\rho c \\lambda}$ [J/(m2 s1/2 K)]", "Conversion factor $k_b$ [min m2/MJ]"],
    [
        ["b > 2500", 0.04],
        ["720 <= b <= 2500", 0.055],
        ["b < 720", 0.07]
    ],
    "Conversion factor $k_b$ depending on thermal properties of enclosure",
    ""
)

# Table G.1
limits_for_configuration_factor_Phi = Table(
    ["Effect", "Configuration", "Localised fire", "Fully developed fire"],
    [
        ["Position effect", "-", "$\\Phi \\le 1$", "$\\Phi = 1$"],
        ["Shadow effect", "Convex", "$\\Phi = 1$", "$\\Phi = 1$"],
        ["Shadow effect", "Concave", "$\\Phi \\le 1$", "$\\Phi \\le 1$"]
    ],
    "Limits for configuration factor $\\Phi$",
    ""
)
