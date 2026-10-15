try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Terms and definitions used in EN 1992-2 (Concrete Bridges)

BridgeDeck = TAD(
    "bridge deck",
    "The structural component of a bridge that directly supports vehicular or pedestrian traffic and distributes traffic loads to the supporting superstructure or substructure."
)

ParapetBeam = TAD(
    "parapet beam",
    "An edge beam or upstand supporting the parapet, safety barrier, or pedestrian railing along the sides of the bridge deck."
)

Crosshead = TAD(
    "crosshead",
    "A transverse beam or pier cap directly supporting longitudinal bridge girders or deck slabs and transferring loads down to the bridge piers or columns."
)

ElastomericBearing = TAD(
    "elastomeric bearing",
    "A flexible bridge bearing fabricated from natural or synthetic rubber, designed to accommodate bridge deck translations and rotations while transferring vertical and horizontal loads to the substructure."
)

VoidedSlab = TAD(
    "voided slab",
    "A reinforced or prestressed concrete bridge deck slab containing longitudinal voids or hollow tubes introduced to reduce the self-weight of the structure."
)

SegmentallyCastBridges = TAD(
    "segmentally cast bridges",
    "Concrete bridges erected incrementally by connecting discrete precast or cast-in-place segments with post-tensioning cables."
)

MonolithicConnection = TAD(
    "monolithic connection",
    "A moment-resisting joint between the superstructure (bridge deck or girders) and substructure (piers or abutments) constructed without mechanical bearings."
)

PileCap = TAD(
    "pile cap",
    "A reinforced concrete block that distributes the column, pier, or abutment loads among a group of foundation piles."
)
