try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

ThermalActions = TAD(
    "thermal actions",
    "thermal actions on a structure or a structural element are those actions that arise from the changes of temperature fields within a specified time interval"
)
ShadeAirTemperature = TAD(
    "shade air temperature",
    "the shade air temperature is the temperature measured by thermometers placed in a white painted louvred wooden box known as a 'Stevenson screen'"
)
MaximumShadeAirTemperature = TAD(
    "maximum shade air temperature T_max",
    "value of maximum shade air temperature with an annual probability of being exceeded of 0.02 (equivalent to a mean return period of 50 years), based on the maximum hourly values recorded"
)
MinimumShadeAirTemperature = TAD(
    "minimum shade air temperature T_min",
    "value of minimum shade air temperature with an annual probability of being exceeded of 0.02 (equivalent to a mean return period of 50 years), based on the minimum hourly values recorded"
)
InitialTemperature = TAD(
    "initial temperature T_0",
    "the temperature of a structural element at the relevant stage of its restraint (completion)"
)
Cladding = TAD(
    "cladding",
    "the part of the building which provides a weatherproof membrane. Generally cladding will only carry self weight and/or wind actions"
)
UniformTemperatureComponent = TAD(
    "uniform temperature component",
    "the temperature, constant over the cross section, which governs the expansion or contraction of an element or structure"
)
TemperatureDifferenceComponent = TAD(
    "temperature difference component",
    "the part of a temperature profile in a structural element representing the temperature difference between the outer face of the element and any in-depth point"
)
