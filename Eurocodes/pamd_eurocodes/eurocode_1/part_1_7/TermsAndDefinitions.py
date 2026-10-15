try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

BurningVelocity = TAD(
    "burning velocity",
    "rate of flame propagation relative to the velocity of the unburned dust, gas or vapour that is ahead of it"
)
Deflagration = TAD(
    "deflagration",
    "propagation of a combustion zone at a velocity that is less than the speed of sound in the unreacted medium"
)
Detonation = TAD(
    "detonation",
    "propagation of a combustion zone at a velocity that is greater than the speed of sound in the unreacted medium"
)
FlameSpeed = TAD(
    "flame speed",
    "speed of a flame front relative to a fixed reference point"
)
FlammableLimits = TAD(
    "flammable limits",
    "minimum and maximum concentrations of a combustible material, in a homogeneous mixture with a gaseous oxidizer that will propagate a flame"
)
VentingPanel = TAD(
    "venting panel",
    "non-structural part of the enclosure (wall, floor, ceiling) with limited resistance that is intended to relieve the developing pressure from deflagration in order to reduce pressure on structural parts of the building"
)
Robustness = TAD(
    "robustness",
    "the ability of a structure to withstand events like fire, explosions, impact or the consequences of human error, without being damaged to an extent disproportionate to the original cause"
)
