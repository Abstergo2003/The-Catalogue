try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

FireCompartment = TAD(
    "fire compartment",
    "space within a building that extends over one or several floors and which is enclosed by separating elements such that fire spread beyond the compartment is prevented during the relevant fire exposure"
)
FireResistance = TAD(
    "fire resistance",
    "ability of a structure or part of it to fulfil its required functions (load-bearing function and/or separating function) for a specified load level, for a specified measure of fire exposure and for a specified period of time"
)
SeparatingFunction = TAD(
    "separating function",
    "ability of a separating element to prevent fire spread (e.g. by passage of flames or hot gases, or by ignition beyond the separating element) during the relevant fire exposure"
)
LoadBearingFunction = TAD(
    "load-bearing function",
    "ability of a structure or a member to sustain specified actions during the relevant fire exposure, according to defined criteria"
)
NormalTemperatureDesign = TAD(
    "normal temperature design",
    "the ultimate limit state design for ambient temperatures according to Part 1-1 of EN 1992 to EN 1996 and EN 1999"
)
CombustionFactor = TAD(
    "combustion factor",
    "an assumed factor representing the efficiency of combustion of the fire load"
)
DesignFire = TAD(
    "design fire",
    "a specified fire development assumed for design purposes"
)
DesignFireLoadDensity = TAD(
    "design fire load density",
    "the fire load density considered for determining thermal actions in fire design"
)
FireActivationRisk = TAD(
    "fire activation risk",
    "parameter taking into account the probability of fire initiation"
)
FireLoad = TAD(
    "fire load",
    "sum of thermal energies which are released by combustion of all combustible materials in a space (building contents and construction elements)"
)
FireLoadDensity = TAD(
    "fire load density",
    "fire load per unit area related to the floor area (q_f) or related to the surface area of the total enclosure (q_t)"
)
FireWall = TAD(
    "fire wall",
    "separating element that is a wall separating two spaces (e.g. two buildings) that is designed for fire resistance and structural stability, and may include resistance to additional horizontal lateral loading"
)
Flashover = TAD(
    "flashover",
    "simultaneous ignition of all combustible materials in an enclosure"
)
FullyDevelopedFire = TAD(
    "fully developed fire",
    "state of full involvement of all combustible materials in a fire within a specified space"
)
HydrocarbonFireCurve = TAD(
    "hydrocarbon fire curve",
    "a nominal temperature-time curve for representing effects of an hydrocarbon type fire"
)
LocalisedFire = TAD(
    "localised fire",
    "a fire involving only a limited area of the fire load in the compartment"
)
OpeningFactor = TAD(
    "opening factor",
    "factor representing the amount of ventilation depending on the area of openings in the compartment walls, on the height of these openings and on the total area of the enclosure surfaces"
)
RateOfHeatRelease = TAD(
    "rate of heat release",
    "heat (energy) released by a combustible product as a function of time"
)
StandardTemperatureTimeCurve = TAD(
    "standard temperature-time curve",
    "a nominal curve defined in prEN13501-2 for representing a model of a fully developed fire in a compartment"
)
TemperatureTimeCurves = TAD(
    "temperature-time curves",
    "gas temperature in the environment of member surfaces as a function of time (nominal or parametric)"
)
ConfigurationFactor = TAD(
    "configuration factor",
    "the configuration factor for radiative heat transfer from surface A to surface B is defined as the fraction of diffusely radiated energy leaving surface A that is incident on surface B"
)
ConvectiveHeatTransferCoefficient = TAD(
    "convective heat transfer coefficient",
    "convective heat flux to the member related to the difference between the bulk temperature of gas bordering the relevant surface of the member and the temperature of that surface"
)
Emissivity = TAD(
    "emissivity",
    "equal to absorptivity of a surface, i.e. the ratio between the radiative heat absorbed by a given surface and that of a black body surface"
)
NetHeatFlux = TAD(
    "net heat flux",
    "energy, per unit time and surface area, definitely absorbed by members"
)
