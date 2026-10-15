try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 2.1
classification_of_actions_during_execution_stages = Table(
    ["Action", "Type of action", "Reference"],
    [
        ["Self-weight of structure and auxiliary works", "Permanent", "EN 1991-1-1"],
        ["Prestressing", "Permanent", "EN 1992 to EN 1996"],
        ["Geotechnical actions / ground pressure", "Permanent / Variable", "EN 1997"],
        ["Pre-deformations", "Permanent", "EN 1990"],
        ["Temperature, wind, snow, water actions", "Variable", "EN 1991-1-3 to EN 1991-1-5"],
        ["Construction loads Qc", "Variable", "Section 4, Table 4.1"],
        ["Accidental actions (impact, falls, human impact)", "Accidental", "4.12, EN 1991-1-7"],
        ["Seismic actions", "Seismic", "EN 1998"]
    ],
    "Classification of actions (other than construction loads) during execution stages",
    ""
)

# Table 2.2
classification_of_construction_loads = Table(
    ["Type of Construction Load", "Symbol", "Classification"],
    [
        ["Personnel, staff, visitors and handtools", "$Q_{ca}$", "Variable, free action"],
        ["Storage of moveable items", "$Q_{cb}$", "Variable, free action"],
        ["Non-permanent equipment (static or travelling)", "$Q_{cc}$", "Variable, fixed or free action"],
        ["Moveable heavy machinery and equipment", "$Q_{cd}$", "Variable, free action"],
        ["Accumulation of waste materials", "$Q_{ce}$", "Variable, free action"],
        ["Parts of structure in temporary states (e.g. fresh concrete)", "$Q_{cf}$", "Variable, fixed action"]
    ],
    "Classification of construction loads",
    ""
)

# Table 3.1
recommended_return_periods_for_climatic_actions_during_execution = Table(
    ["Nominal duration of execution stage", "Recommended return period [years]"],
    [
        ["<= 3 days", 2],
        ["<= 3 months (but > 3 days)", 5],
        ["<= 1 year (but > 3 months)", 10],
        ["> 1 year", 50]
    ],
    "Recommended return periods for the assessment of the characteristic values of climatic actions",
    "Recommended basic wind velocity for durations up to 3 months is 20 m/s."
)

# Table 4.1
representation_of_construction_loads = Table(
    ["Type", "Symbol", "Description", "Representation", "Recommended Characteristic Value"],
    [
        ["Personnel and handtools", "$Q_{ca}$", "Working personnel, staff and visitors with handtools", "Uniformly distributed load $q_{ca}$", "$q_{ca,k} = 1.0$ kN/m2"],
        ["Storage of movable items", "$Q_{cb}$", "Building materials, precast elements, equipment", "Uniformly distributed $q_{cb}$ or concentrated $F_{cb}$", "Bridges: $q_{cb,k} = 0.2$ kN/m2; $F_{cb,k} = 100$ kN"],
        ["Non-permanent equipment", "$Q_{cc}$", "Formwork panels, scaffolding, falsework, machinery", "Uniformly distributed load $q_{cc}$", "$q_{cc,k} = 0.5$ kN/m2"],
        ["Moveable heavy machinery", "$Q_{cd}$", "Cranes, lifts, vehicles, lift trucks, jacks", "Wheel/track load models", "See EN 1991-2 and EN 1991-3"],
        ["Accumulation of waste", "$Q_{ce}$", "Surplus materials, excavated soil, demolition debris", "Mass effects on elements", "According to planned site build-up"],
        ["Parts in temporary states", "$Q_{cf}$", "Loads from lifting operations, fresh concrete", "Planned execution sequence", "See 4.11.2 and Table 4.2"]
    ],
    "Representation of construction loads ($Q_c$)",
    ""
)

# Table 4.2
characteristic_values_of_loads_during_casting_of_concrete = Table(
    ["Action", "Loaded area", "Load in [kN/m2]"],
    [
        ["(a) Working area", "Inside working area 3 m x 3 m (or span length if less)", "10% self-weight of concrete, BRange(0.75, 1.5, 0.75) (covering Qca and Qcf)"],
        ["(b) Other area", "Outside the working area", "0.75 (covering Qca)"],
        ["(c) Actual area", "Actual area", "Self-weight of formwork (Qcc) + weight of fresh concrete (Qcf)"]
    ],
    "Recommended characteristic values of actions due to construction loads during casting of concrete",
    "Density of fresh concrete is typically 25 kN/m3 (unhardened concrete)."
)
