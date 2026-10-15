try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Terms and definitions used in EN 1996-1-1 (General rules for reinforced and unreinforced masonry)

Masonry = TAD(
    "masonry",
    "An assemblage of masonry units laid in a specified arrangement and bonded together with mortar."
)

UnreinforcedMasonry = TAD(
    "unreinforced masonry",
    "Masonry that contains no reinforcement, or less reinforcement than the minimum required for reinforced masonry."
)

ReinforcedMasonry = TAD(
    "reinforced masonry",
    "Masonry in which steel reinforcing bars, bed-joint reinforcement, or mesh are embedded in mortar or concrete infill so that all materials act together in resisting forces."
)

ConfinedMasonry = TAD(
    "confined masonry",
    "Masonry in which vertical and horizontal reinforced concrete or reinforced masonry confining elements (tie-columns and tie-beams) are cast in place after the masonry walls have been erected."
)

MasonryUnit = TAD(
    "masonry unit",
    "A preformed building component intended for use in masonry construction, manufactured from clay, calcium silicate, aggregate concrete, autoclaved aerated concrete, manufactured stone, or dimensioned natural stone."
)

Mortar = TAD(
    "mortar",
    "A mix of one or more inorganic binders, aggregates, water, and optional admixtures used to bed and joint masonry units (classified as general purpose, thin layer, or lightweight mortar)."
)

BedJoint = TAD(
    "bed joint",
    "A horizontal mortar joint upon which masonry units are placed."
)

HeadJoint = TAD(
    "head joint (perpend)",
    "A vertical mortar joint perpendicular to the bed joint and to the face of the wall."
)

CavityWall = TAD(
    "cavity wall",
    "A wall consisting of two parallel single-leaf walls effectively tied together across a continuous cavity with corrosion-resistant wall ties or bed-joint reinforcement."
)

ShearWall = TAD(
    "shear wall",
    "A structural masonry wall primarily designed and detailed to resist lateral in-plane horizontal shear forces, such as wind or seismic loads."
)

LoadbearingWall = TAD(
    "loadbearing wall",
    "A wall primarily designed to support vertical gravity loads from roofs, floors, or upper storeys in addition to its own self-weight."
)
