try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Terms and definitions used in EN 1998-6 (Towers, masts and chimneys)

SupportingShaft = TAD(
    "supporting shaft or shell",
    "The structural shell or lattice column component which supports waste gas flues, service platforms, and internal equipment."
)

InternalFlue = TAD(
    "internal flue",
    "A waste gas conducting flue installed inside a supporting shaft protecting components against high temperature and chemical aggression."
)

TransmissionTower = TAD(
    "transmission tower",
    "A tall cantilever lattice or tubular steel tower used to support electric power transmission cables or telecommunication antennas."
)

TangentTower = TAD(
    "tangent tower",
    "An electric transmission tower used where the line is straight or deviates by less than 3 degrees in plan."
)

AngleTower = TAD(
    "angle tower",
    "A transmission tower located where the line changes direction by more than 3 degrees in plan, resisting resultant transverse wire tension."
)

AnchorTower = TAD(
    "anchor tower (dead-end tower)",
    "A tower capable of resisting dead-end longitudinal tension forces from all cables on one side, in addition to vertical and transverse loads."
)

RotationalExcitation = TAD(
    "rotational excitation",
    "Seismic ground motion rotational components (torsional and rocking) considered in dynamic analyses of tall slender structures."
)

GuyedMast = TAD(
    "guyed mast",
    "A slender column or truss mast supported laterally by sets of inclined prestressed stay cables (guys) anchored to the ground at various elevations."
)
