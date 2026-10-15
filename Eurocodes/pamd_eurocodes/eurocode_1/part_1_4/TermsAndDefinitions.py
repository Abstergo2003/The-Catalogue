try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

FundamentalBasicWindVelocity = TAD(
    "fundamental basic wind velocity",
    "the 10 minute mean wind velocity with an annual risk of being exceeded of 0.02, irrespective of wind direction, at a height of 10 m above flat open country terrain and accounting for altitude effects (if required)"
)
BasicWindVelocity = TAD(
    "basic wind velocity",
    "the fundamental basic wind velocity modified to account for the direction of the wind being considered and the season (if required)"
)
MeanWindVelocity = TAD(
    "mean wind velocity",
    "the basic wind velocity modified to account for the effect of terrain roughness and orography"
)
PressureCoefficient = TAD(
    "pressure coefficient",
    "external pressure coefficients give the effect of the wind on external surfaces; internal pressure coefficients give the effect on internal surfaces; net pressure coefficients give the resulting effect per unit area"
)
ForceCoefficient = TAD(
    "force coefficient",
    "force coefficients give the overall effect of the wind on a structure, structural element or component as a whole, including friction, if not specifically excluded"
)
BackgroundResponseFactor = TAD(
    "background response factor",
    "the background factor allowing for the lack of full correlation of the pressure on the structure surface"
)
ResonanceResponseFactor = TAD(
    "resonance response factor",
    "the resonance response factor allowing for turbulence in resonance with the vibration mode"
)
