try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

SafetyBarrier = TAD(
    "safety barrier",
    "road vehicle restraint system installed alongside, or on the central reserve, of a road"
)
VehicleParapet = TAD(
    "vehicle parapet",
    "safety barrier installed on the edge, or near the edge, of a bridge or on a retaining wall where there is a vertical drop"
)
PedestrianRestraintSystem = TAD(
    "pedestrian restraint system",
    "system installed to provide guidance and restraint for pedestrians"
)
Carriageway = TAD(
    "carriageway",
    "part of the road surface, supported by a single structure, which includes all physical traffic lanes, hard shoulders, hard strips and marker strips"
)
HardShoulder = TAD(
    "hard shoulder",
    "surfaced strip, usually of one traffic lane width, adjacent to the outermost physical traffic lane, intended for vehicles in difficulty"
)
NotionalLane = TAD(
    "notional lane",
    "strip of carriageway defined for the application of traffic load models"
)
Tracks = TAD(
    "tracks",
    "tracks include rails and sleepers, laid on a ballast bed or directly fastened to bridge decks"
)
Footpath = TAD(
    "footpath",
    "strip located alongside tracks or carriageway, between traffic lanes/tracks and parapets"
)
ResonantSpeed = TAD(
    "resonant speed",
    "traffic speed at which a frequency of loading coincides with a natural frequency of the structure (or part of it)"
)
