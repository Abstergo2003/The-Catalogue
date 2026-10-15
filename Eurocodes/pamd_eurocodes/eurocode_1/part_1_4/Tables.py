try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 4.1
terrain_categories_and_terrain_parameters = Table(
    ["Terrain category", "Description", "Roughness length $z_0$ [m]", "Minimum height $z_{min}$ [m]"],
    [
        ["0", "Sea or coastal area exposed to the open sea", 0.003, 1],
        ["I", "Lakes or flat and horizontal area with negligible vegetation and without obstacles", 0.01, 1],
        ["II", "Area with low vegetation such as grass and isolated obstacles with separations of at least 20 obstacle heights", 0.05, 2],
        ["III", "Area with regular cover of vegetation or buildings (suburban, forest)", 0.3, 5],
        ["IV", "Area in which at least 15 % of surface is covered with buildings with average height exceeding 15 m", 1.0, 10]
    ],
    "Terrain categories and terrain parameters",
    "Terrain factor kr = 0.19 * (z0 / z0_II)^0.07 where z0_II = 0.05 m."
)

# Table 5.1
calculation_procedures_for_the_determination_of_wind_actions = Table(
    ["Parameter", "Description", "Subject Reference"],
    [
        ["Peak velocity pressure $q_p$", "Basic wind velocity vb, terrain category, turbulence intensity Iv", "4.2, 4.4, 4.5, Table 4.1"],
        ["Wind pressures on surfaces", "External wind pressure we = qp * cpe; Internal wind pressure wi = qp * cpi", "5.2, Section 7"],
        ["Wind forces on structures", "Resultant wind force Fw = cs cd * cf * qp * Aref or from pressure integration", "5.3, Section 6, Section 7"]
    ],
    "Calculation procedures for the determination of wind actions",
    "Summary of calculation procedures according to EN 1991-1-4."
)

# Table 7.1
external_pressure_coefficients_for_vertical_walls_of_rectangular_buildings = Table(
    ["Zone / Ratio h/d", "Zone A ($c_{pe,10}$ / $c_{pe,1}$)", "Zone B ($c_{pe,10}$ / $c_{pe,1}$)", "Zone C ($c_{pe,10}$)", "Zone D ($c_{pe,10}$ / $c_{pe,1}$)", "Zone E ($c_{pe,10}$)"],
    [
        ["h/d >= 5", "-1.2 / -1.4", "-0.8 / -1.1", -0.5, "+0.8 / +1.0", -0.7],
        ["h/d = 1", "-1.2 / -1.4", "-0.8 / -1.1", -0.5, "+0.8 / +1.0", -0.5],
        ["h/d <= 0.25", "-1.2 / -1.4", "-0.8 / -1.1", -0.5, "+0.7 / +1.0", -0.3]
    ],
    "External pressure coefficients for vertical walls of rectangular plan buildings",
    "cpe,10 gives pressure coefficients for loaded areas > 10 m2; cpe,1 for loaded areas <= 1 m2."
)

# Table 7.2
external_pressure_coefficients_for_flat_roofs = Table(
    ["Roof type", "Zone F ($c_{pe,10}$ / $c_{pe,1}$)", "Zone G ($c_{pe,10}$ / $c_{pe,1}$)", "Zone H ($c_{pe,10}$ / $c_{pe,1}$)", "Zone I ($c_{pe,10}$ / $c_{pe,1}$)"],
    [
        ["Sharp eaves", "-1.8 / -2.5", "-1.2 / -2.0", "-0.7 / -1.2", "+0.2 / -0.2"],
        ["With Parapets (hp/h = 0.025)", "-1.6 / -2.2", "-1.1 / -1.8", "-0.7 / -1.2", "+0.2 / -0.2"],
        ["With Parapets (hp/h = 0.05)", "-1.4 / -2.0", "-0.9 / -1.6", "-0.7 / -1.2", "+0.2 / -0.2"],
        ["With Parapets (hp/h = 0.10)", "-1.2 / -1.8", "-0.8 / -1.4", "-0.7 / -1.2", "+0.2 / -0.2"],
        ["Curved Eaves (r/h = 0.05)", "-1.0 / -1.5", "-1.2 / -1.8", "-0.4", "+0.2 / -0.2"],
        ["Curved Eaves (r/h = 0.10)", "-0.7 / -1.2", "-0.8 / -1.4", "-0.3", "+0.2 / -0.2"],
        ["Curved Eaves (r/h = 0.20)", "-0.5 / -0.8", "-0.5 / -0.8", "-0.3", "+0.2 / -0.2"],
        ["Mansard Eaves (alpha = 30 deg)", "-1.0 / -1.5", "-1.0 / -1.5", "-0.3", "+0.2 / -0.2"],
        ["Mansard Eaves (alpha = 45 deg)", "-1.2 / -1.8", "-1.3 / -1.9", "-0.4", "+0.2 / -0.2"],
        ["Mansard Eaves (alpha = 60 deg)", "-1.3 / -1.9", "-1.3 / -1.9", "-0.5", "+0.2 / -0.2"]
    ],
    "External pressure coefficients for flat roofs",
    "For roofs with parapets or curved eaves, linear interpolation may be used for intermediate values."
)

# Table 7.10
frictional_coefficients_cfr_for_walls_parapets_and_roof_surfaces = Table(
    ["Surface", "Friction coefficient $c_{fr}$"],
    [
        ["Smooth (i.e. steel, smooth concrete)", 0.01],
        ["Rough (i.e. rough concrete, tar-boards)", 0.02],
        ["Very rough (i.e. ripples, ribs, folds)", 0.04]
    ],
    "Frictional coefficients $c_{fr}$ for walls, parapets and roof surfaces",
    "Friction forces applied on surfaces parallel to wind located beyond 2*b or 4*h from upwind corner."
)

# Table E.1
strouhal_numbers_St_for_different_cross_sections = Table(
    ["Cross-section", "Ratio d/b", "Strouhal number $St$"],
    [
        ["Circular cylinder", "For all Re", 0.18],
        ["Rectangular section", "d/b = 1.0", 0.11],
        ["Rectangular section", "d/b = 1.5", 0.10],
        ["Rectangular section", "d/b = 2.0", 0.14]
    ],
    "Strouhal numbers $St$ for different cross-sections",
    "Extrapolations for Strouhal numbers as function of d/b are not allowed."
)
