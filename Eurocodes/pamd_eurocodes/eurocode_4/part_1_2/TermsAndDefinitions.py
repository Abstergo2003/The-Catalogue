try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Terms and definitions used in EN 1994-1-2 (Structural fire design)

StandardFireExposure = TAD(
    "standard fire exposure",
    "A standardized temperature-time curve representing a fully developed compartment fire, typically defined by ISO 834 / EN 1991-1-2."
)

FireResistance = TAD(
    "fire resistance",
    "The ability of a structure or part thereof to fulfill its required load-bearing capacity (R), integrity (E), or thermal insulation (I) for a specified fire exposure and duration."
)

ThermalInsulation = TAD(
    "thermal insulation (criterion I)",
    "The ability of a separating element of building construction to prevent heat transmission resulting in significant temperature rise on the unexposed face."
)

Integrity = TAD(
    "integrity (criterion E)",
    "The ability of a separating element of building construction to prevent the passage of flames and hot gases and to prevent the occurrence of flames on the unexposed surface."
)

CriticalTemperature = TAD(
    "critical temperature",
    "The temperature of a structural steel member or reinforcement at which failure is expected to occur for a given fire design load level."
)

CompositeFireDesign = TAD(
    "composite fire design",
    "Fire design methodology taking advantage of the combined behavior of structural steel and concrete, including thermal shield effects, concrete moisture evaporation, and load sharing."
)

PartialConcreteEncasement = TAD(
    "partial concrete encasement",
    "Concrete cast between the flanges of an I- or H-steel section, substantially enhancing fire endurance by reducing web heating and stabilizing the compression flange."
)

ConcreteFilledSection = TAD(
    "concrete-filled hollow section",
    "A circular or rectangular hollow structural steel section filled with unreinforced or reinforced concrete to sustain structural load during fire."
)
