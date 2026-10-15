"""Eurocode 8 - Part 4: Silos, tanks and pipelines - Tables.
EN 1998-4 (2006).
"""
try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange


# Table 2.1N
importance_factors_silos_tanks_pipelines = Table(
    ["Use of the structure/facility", "Importance Class I", "Importance Class II", "Importance Class III"],
    [
        ["Potable water supply, non-toxic, non-inflammable material", "0.8 - 1.0", "1.0", "1.2"],
        ["Fire fighting water, non-volatile toxic material, low flammability petrochemicals", "1.0", "1.2", "1.4"],
        ["Volatile toxic chemicals, explosive and high flammability liquids", "1.2", "1.4", "1.6"]
    ],
    "Recommended importance factors gamma_I for silos, tanks, and pipeline facilities (EN 1998-4 Table 2.1N)",
    "Differentiates reliability based on content hazard and consequences of rupture or functional loss."
)

# Table 3.1
silo_behaviour_factors = Table(
    ["Supporting structure type", "Ductility class DCM upper limit q", "Ductility class DCH upper limit q"],
    [
        ["Single pedestal, skirt, or irregular bracings", "q_pendulum (typically 1.5 - 2.0)", "q_pendulum (typically 2.0)"],
        ["Moment resisting frames or regular bracings", "1.25 * q_pendulum", "1.25 * q_pendulum"],
        ["Cast-in-place concrete walls continuous to foundation", "1.50 * q_pendulum", "1.50 * q_pendulum"]
    ],
    "Upper limit values of behaviour factor q for elevated silos (EN 1998-4 Clause 3.4(4))",
    "Derived from inverted pendulum structures with amplification factors accounting for structural framing type."
)

# Table 4.1
tank_behaviour_factors = Table(
    ["Tank configuration / support condition", "Recommended behaviour factor q", "Response component / note"],
    [
        ["Convective (sloshing) liquid response component", 1.0, "Elastic response spectrum (q = 1.0) shall always be used"],
        ["General tanks designed for elastic response", 1.5, "Accounts for overstrength in elastic response"],
        ["Unanchored vertical steel tanks allowing uplift", 1.5, "Requires bottom plate thickness <= lower shell course thickness"],
        ["Vertical steel tanks with ductile anchors (elongation >= R/200)", 2.0, "Ductile anchors designed to elongate plastically without rupture"]
    ],
    "Design behaviour factors q for ground-supported and anchored tanks (EN 1998-4 Clause 4.3.2)",
    "Accounts for uplift, anchor ductility, and limits convective component to linear elastic response."
)

# Table 5.1
pipeline_behaviour_factors = Table(
    ["Pipeline radius-to-thickness ratio R/t", "Behaviour factor q", "Structural ductility requirement"],
    [
        ["R/t < 50", 3.0, "Significant plastic deformation and energy dissipation capacity in welded steel pipe"],
        ["50 <= R/t < 100", 2.0, "Moderate dissipation capacity before local wall buckling occurs"],
        ["R/t >= 100", 1.0, "Elastic behavior assumed due to sensitivity to shell wrinkling and buckling"]
    ],
    "Behaviour factors q for welded above-ground steel pipelines (EN 1998-4 Clause 5.4.3(3))",
    "Governs the seismic design forces for above-ground piping based on radius-to-thickness ratio."
)
