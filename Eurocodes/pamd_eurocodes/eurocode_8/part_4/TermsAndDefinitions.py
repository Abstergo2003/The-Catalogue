try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Terms and definitions used in EN 1998-4 (Silos, tanks and pipelines)

FullIntegrityRequirement = TAD(
    "full integrity requirement",
    "A damage limitation requirement stating that the considered system and its accessory elements remain fully serviceable and leak-proof under seismic action."
)

MinimumOperatingLevel = TAD(
    "minimum operating level",
    "A damage limitation requirement ensuring that after damage control operations have been carried out, the capacity of the system can be restored up to a predefined level of operation."
)

ImpulsivePressure = TAD(
    "impulsive pressure",
    "The hydrodynamic pressure component produced by the inertia forces of the liquid moving synchronously with the tank walls and base."
)

ConvectivePressure = TAD(
    "convective pressure",
    "The hydrodynamic sloshing pressure component associated with the long-period oscillatory surface waves of the liquid."
)

SloshingWaveHeight = TAD(
    "sloshing wave height",
    "The vertical displacement of the free liquid surface during earthquake excitation, governing required freeboard to prevent roof damage or spillage."
)

ElephantFootBuckling = TAD(
    "elephant's foot buckling",
    "An outward bulge buckling mode at the base of a thin cylindrical metal tank shell resulting from high axial compressive stresses combined with internal hoop tensile stresses."
)

BreathingMode = TAD(
    "breathing mode",
    "Cross-sectional or shell ovalling mode of vibration in thin-walled tanks or pipes involving non-axisymmetric circumferential deformation."
)

PipelineFaultCrossing = TAD(
    "pipeline fault crossing",
    "The intersection of a buried or above-ground pipeline with an active tectonic fault trace subject to permanent ground displacement."
)
