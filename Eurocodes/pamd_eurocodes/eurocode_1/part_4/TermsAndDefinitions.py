try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

AeratedSiloBottom = TAD(
    "aerated silo bottom",
    "a silo base in which air slides or air injection is used to activate flow in the bottom of the silo"
)
CharacteristicDimensionOfSilo = TAD(
    "characteristic dimension of inside of silo cross-section (d_c)",
    "the characteristic dimension d_c is the diameter of the largest inscribed circle within the silo cross-section"
)
CircularSilo = TAD(
    "circular silo",
    "a silo whose plan cross-section is circular"
)
Discharge = TAD(
    "discharge",
    "the process of removing particulate solids from a silo"
)
EccentricDischarge = TAD(
    "eccentric discharge",
    "discharge where the flow channel is not concentric with the vertical axis of the silo"
)
Filling = TAD(
    "filling",
    "the process of adding particulate solids to a silo"
)
FlowChannel = TAD(
    "flow channel",
    "the zone within the particulate solid where motion occurs during discharge"
)
FluidisedSolid = TAD(
    "fluidised solid",
    "a state of stored fine particulate solid when its bulk contains a high proportion of interstitial air supporting particle weight"
)
FreeFlowingGranularSolid = TAD(
    "free flowing granular solid",
    "a granular solid whose flowing behaviour is not significantly affected by cohesion"
)
FullCondition = TAD(
    "full condition",
    "state of silo when filled to the maximum design level"
)
Hopper = TAD(
    "hopper",
    "the converging bottom section of a silo"
)
InternalFriction = TAD(
    r"angle of internal friction (\phi_i)",
    "the effective angle of internal friction of stored particulate solid"
)
LateralPressureRatio = TAD(
    "lateral pressure ratio K",
    "the ratio of the horizontal pressure on the vertical wall of a silo to the mean vertical stress in the solid at the same level"
)
MassFlow = TAD(
    "mass flow",
    "a flow pattern in which all the stored particles are simultaneously in motion during discharge"
)
FunnelFlow = TAD(
    "funnel flow",
    "a flow pattern in which only a channel within the solid moves, while peripheral material remains stationary"
)
Silo = TAD(
    "silo",
    "containment structure used to store particulate solids (i.e. bunker, bin or silo)"
)
SlenderSilo = TAD(
    "slender silo",
    "a silo where h_c / d_c >= 2.0"
)
SquatSilo = TAD(
    "squat silo",
    "a silo where 0.4 < h_c / d_c <= 1.0"
)
IntermediateSlendernessSilo = TAD(
    "intermediate slenderness silo",
    "a silo where 1.0 < h_c / d_c < 2.0"
)
WallFrictionCoefficient = TAD(
    r"wall friction coefficient (\mu)",
    "ratio of shear stress at the wall to the normal pressure on the wall"
)
