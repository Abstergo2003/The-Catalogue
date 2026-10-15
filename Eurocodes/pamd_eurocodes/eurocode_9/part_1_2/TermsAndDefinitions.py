try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Terms and definitions used in EN 1999-1-2 / ENV 1999-1-2 (Structural fire design for aluminium)

CriticalAluminiumTemperature = TAD(
    "critical aluminium temperature",
    "The uniform member temperature at which an aluminium element can no longer sustain the mechanical design action effects in the fire situation, typically between 170 deg C and 300 deg C."
)

SectionFactorAluminium = TAD(
    "section factor (Am / V)",
    "The ratio between the exposed surface area of an aluminium member per unit length and its volume per unit length, dictating the heating rate under fire exposure."
)

FireProtectionMaterial = TAD(
    "fire protection material",
    "Thermal insulation material applied to aluminium structural members (boards, mineral wool wraps, or intumescent coatings) to delay heating of the cross-section."
)

StandardFireExposure = TAD(
    "standard fire exposure (ISO 834)",
    "A standard temperature-time curve representing fully developed flashover compartment fire conditions used to classify fire resistance ratings (R15, R30, R60)."
)

ThermalConductivityAluminium = TAD(
    "thermal conductivity of aluminium",
    "The very high rate of thermal conduction characteristic of aluminium alloys (160 to 210 W/(m*K)), resulting in rapid, almost uniform temperature distributions throughout cross-sections."
)
