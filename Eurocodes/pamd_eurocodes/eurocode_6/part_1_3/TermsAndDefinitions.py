try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Terms and definitions used in DD ENV 1996-1-3 (Detailed rules on lateral loading)

LateralLoad = TAD(
    "lateral load on masonry",
    "Actions acting perpendicular to the face of a wall, notably out-of-plane wind pressures, earth pressures, barrier pedestrian loadings, or blast overpressures."
)

ArchingAction = TAD(
    "arching action",
    "A structural mechanism where a laterally loaded masonry wall bounded by rigid non-yielding supports develops internal in-plane compressive thrust arches that substantially enhance its lateral load capacity."
)

YieldLineMethod = TAD(
    "yield-line / fracture line method",
    "An ultimate limit state analysis method based on rigid-plastic plate kinematics where lateral wall collapse is idealized along discrete flexural fracture lines."
)

OrthogonalRatio = TAD(
    "orthogonal ratio (mu)",
    "The ratio between the characteristic flexural strength of masonry with failure parallel to bed joints and perpendicular to bed joints (mu = f_xk1 / f_xk2)."
)

BoundarySupportCondition = TAD(
    "boundary support condition",
    "The restraint provided to a masonry panel along its top, bottom, and side edges (simply supported, continuous, or free unsupported edge)."
)

VerticalArching = TAD(
    "vertical arching",
    "Arching action developed vertically between floor slabs or beam supports when top and bottom wall boundaries are positively restrained against translation."
)

HorizontalArching = TAD(
    "horizontal arching",
    "Arching action developed horizontally between piers, columns, or intersecting cross-walls."
)
