try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Terms and definitions used in EN 1996-2 (Design considerations, selection of materials and execution)

ExposureClass = TAD(
    "exposure class (micro-environment MX)",
    "Classification of environmental actions to which masonry is exposed during its design life, encompassing dryness (MX1), moisture (MX2), freeze-thaw cycles (MX3), de-icing or marine salts (MX4), and chemical attack (MX5)."
)

WallTie = TAD(
    "wall tie",
    "A corrosion-resistant metallic or synthetic anchoring device linking two leaves of a cavity wall to ensure composite lateral out-of-plane action and resist wind suction."
)

DampProofCourse = TAD(
    "damp proof course (DPC)",
    "A continuous impervious sheet, membrane, or slate layer built into masonry walls to impede capillary rise or downward percolation of moisture."
)

MovementJoint = TAD(
    "movement joint",
    "A planned joint traversing the masonry leaf that accommodates moisture expansion, thermal movements, and differential foundation settlements without distressing the wall."
)

Efflorescence = TAD(
    "efflorescence",
    "A whitish powdery deposit of water-soluble mineral salts migrating to and crystalizing on the masonry surface as moisture evaporates."
)

BedJointReinforcement = TAD(
    "bed joint reinforcement",
    "Prefabricated stainless steel or galvanized steel ladder/truss wire reinforcement embedded in mortar bed joints to control shrinkage cracking and distribute lateral loads."
)

PointingAndJointing = TAD(
    "pointing and jointing",
    "The tooling and compaction of the outer mortar face in joints (weather-struck, flush, bucket-handle) to optimize rainwater shedding and prevent frost spalling."
)

WorkmanshipQuality = TAD(
    "workmanship and execution quality",
    "The required standard of site construction, ensuring full mortar bedding, proper bond overlapping, plumb verticality, and protective measures during frosty or rainy weather."
)
