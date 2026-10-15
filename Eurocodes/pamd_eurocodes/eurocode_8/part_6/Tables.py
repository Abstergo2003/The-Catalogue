"""Eurocode 8 - Part 6: Towers, masts and chimneys - Tables.
EN 1998-6 (2005).
"""
try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange


# Table 4.1
importance_factors_towers_chimneys = Table(
    ["Structural category / consequence class", "Recommended importance factor gamma_I"],
    [
        ["Strategic importance: vital component of water supply, electric power plant, or communication network", 1.4],
        ["Height greater than distance to surrounding buildings, crowded area, or collapse causes industrial shutdown", 1.2],
        ["Structures taller than 80 m not pertaining to the above categories", 1.1],
        ["Standard structures (remaining cases)", 1.0]
    ],
    "Recommended values of importance factor gamma_I for towers, masts and chimneys (EN 1998-6 Clause 4.1(1)P)",
    "Scales seismic action according to structural height, proximity to public, and essential network function."
)

# Table 4.2
regularity_factor_kr = Table(
    ["Type of structural irregularity", "Modification factor kr"],
    [
        ["Horizontal mass eccentricity at a section exceeding 5% of relevant dimension", 0.8],
        ["Opening in shaft causing 30% or larger reduction in cross-sectional moment of inertia", 0.8],
        ["Concentrated mass within top third elevation contributing >= 50% to base overturning moment", 0.7],
        ["Multiple irregularities present simultaneously", "Product of the two lowest kr values"]
    ],
    "Values of modification factor kr reflecting departure from regular mass, stiffness or strength (EN 1998-6 Clause 4.15.2)",
    "Reduces the basic behaviour factor q0 to account for localized stress concentrations and torsional dynamic effects."
)

# Table 5.1
basic_behaviour_factors_q0 = Table(
    ["Structure type", "Structural detailing / system", "Basic behaviour factor q0"],
    [
        ["Reinforced concrete chimneys", "Curvature ductility mu >= 9 at critical sections", 3.0],
        ["Reinforced concrete chimneys", "Standard detailing without confirmed high ductility", 1.5],
        ["Steel chimneys / support frames", "Moment resisting frames or eccentric bracings", 5.0],
        ["Steel chimneys / support frames", "Concentric diagonal bracings", 4.0],
        ["Steel chimneys / support frames", "V-bracings", 2.0],
        ["Steel chimneys / support frames", "Non-dissipative or K-bracings", 1.5],
        ["Steel shell-type chimneys", "Class 1 cross-section for plastic global analysis", 2.0],
        ["Steel shell-type chimneys", "Standard elastic shell", 1.5],
        ["Steel lattice towers", "Cross-braced trussed towers (DCM / DCH)", "2.0 - 4.0"]
    ],
    "Basic behaviour factor q0 for chimneys, masts and towers (EN 1998-6 Clauses 5.1, 6.1, 7.1, Figure 1)",
    "Reflects the intrinsic energy dissipation and ductility capacity of the lateral load resisting system."
)
