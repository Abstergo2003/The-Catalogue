try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Terms and definitions used in EN 1996-1-2 (Structural fire design)

StandardFireExposure = TAD(
    "standard fire exposure",
    "A standardized time-temperature curve representing a fully developed fire within a building compartment (ISO 834 / EN 1991-1-2)."
)

FireResistance = TAD(
    "fire resistance",
    "The ability of a masonry wall or column to satisfy specified load-bearing (R), integrity (E), or thermal insulation (I) criteria during standard fire exposure."
)

SeparatingWall = TAD(
    "separating wall in fire",
    "A wall designed to prevent the propagation of fire, hot gases, and heat transfer from one compartment to an adjacent space (criteria EI or REI)."
)

NonLoadbearingWallInFire = TAD(
    "non-loadbearing wall in fire",
    "A separating partition wall that carries only its self-weight under fire exposure without sustaining external gravity actions (criteria EI)."
)

LoadbearingWallInFire = TAD(
    "loadbearing wall in fire",
    "A masonry wall required to maintain both stability/load-bearing capacity and compartmental separating functions under fire exposure (criteria REI)."
)

ThermalInsulationI = TAD(
    "thermal insulation (criterion I)",
    "The ability of a wall to limit temperature rise on the unexposed face to a mean of 140 K and a maximum of 180 K above initial ambient temperature."
)

IntegrityE = TAD(
    "integrity (criterion E)",
    "The ability of a separating wall to prevent the passage of flames and hot gases and prevent ignition of a cotton pad on the unexposed side."
)

MechanicalResistanceR = TAD(
    "mechanical resistance (criterion R)",
    "The ability of a load-bearing wall to maintain its structural equilibrium and load-carrying capacity without structural collapse during fire exposure."
)
