try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

CharacteristicValueOfSnowLoadOnTheGround = TAD(
    "characteristic value of snow load on the ground",
    "snow load on the ground based on an annual probability of exceedence of 0.02, excluding exceptional snow loads"
)
AltitudeOfTheSite = TAD(
    "altitude of the site",
    "height above mean sea level of the site where the structure is to be located, or is already located for an existing structure"
)
ExceptionalSnowLoadOnTheGround = TAD(
    "exceptional snow load on the ground",
    "load of the snow layer on the ground resulting from a snow fall which has an exceptionally infrequent likelihood of occurring"
)
CharacteristicValueOfSnowLoadOnTheRoof = TAD(
    "characteristic value of snow load on the roof",
    "product of the characteristic snow load on the ground and appropriate coefficients"
)
UndriftedSnowLoadOnTheRoof = TAD(
    "undrifted snow load on the roof",
    "load arrangement which describes the uniformly distributed snow load on the roof, affected only by the shape of the roof, before any redistribution of snow due to other climatic actions"
)
DriftedSnowLoadOnTheRoof = TAD(
    "drifted snow load on the roof",
    "load arrangement which describes the snow load distribution resulting from snow having been moved from one location to another location on a roof, e.g. by the action of the wind"
)
RoofSnowLoadShapeCoefficient = TAD(
    "roof snow load shape coefficient",
    "ratio of the snow load on the roof to the undrifted snow load on the ground, without the influence of exposure and thermal effects"
)
ThermalCoefficient = TAD(
    "thermal coefficient",
    "coefficient defining the reduction of snow load on roofs as a function of the heat flux through the roof, causing snow melting"
)
ExposureCoefficient = TAD(
    "exposure coefficient",
    "coefficient defining the reduction or increase of load on a roof of an unheated building, as a fraction of the characteristic snow load on the ground"
)
LoadDueToExceptionalSnowDrift = TAD(
    "load due to exceptional snow drift",
    "load arrangement which describes the load of the snow layer on the roof resulting from a snow deposition pattern which has an exceptionally infrequent likelihood of occurring"
)
