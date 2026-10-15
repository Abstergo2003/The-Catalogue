try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Section 1.5 Terms and definitions used in EN 1993-1-2 (Structural fire design)

PartOfStructure = TAD(
    "part of structure",
    "Isolated part of an entire structure with appropriate support and boundary conditions."
)

CarbonSteel = TAD(
    "carbon steel",
    "Steel grades referred to in Eurocode 3 Part 1-1, except stainless steels."
)

FireProtectionMaterial = TAD(
    "fire protection material",
    "Any material or combination of materials applied to a structural member for the purpose of increasing its fire resistance."
)

StainlessSteel = TAD(
    "stainless steel",
    "All steels referred to in EN 1993-1-4."
)

ConfigurationFactor = TAD(
    "configuration factor",
    "The configuration factor for radiative heat transfer from surface A to surface B is defined as the fraction of diffusely radiated energy leaving surface A that is incident on surface B."
)

ConvectiveHeatTransferCoefficient = TAD(
    "convective heat transfer coefficient",
    "Convective heat flux to the member related to the difference between the bulk temperature of gas bordering the relevant surface of the member and the temperature of that surface."
)

Emissivity = TAD(
    "emissivity",
    "Ratio between the radiative heat absorbed by a given surface, and that of a black body surface."
)

NetHeatFlux = TAD(
    "net heat flux",
    "Energy per unit time and surface area definitely absorbed by members."
)

CriticalTemperature = TAD(
    "critical temperature",
    "The temperature of the load bearing element at which failure of the element in fire situation (Criterion R) is expected to occur for a given load level."
)
