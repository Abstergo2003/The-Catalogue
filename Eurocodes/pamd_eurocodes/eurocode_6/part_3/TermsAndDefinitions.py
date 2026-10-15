try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Terms and definitions used in EN 1996-3 (Simplified calculation methods for unreinforced masonry)

SimplifiedCalculationMethod = TAD(
    "simplified calculation method",
    "A standardized design procedure for unreinforced masonry buildings of limited height and regular layout (up to 3 or 4 storeys) that eliminates complex frame analysis by enforcing geometry and slenderness bounds."
)

InternalWall = TAD(
    "internal loadbearing wall",
    "A loadbearing wall located entirely within the perimeter envelope of the building supporting floor or roof loads from both sides."
)

ExternalWall = TAD(
    "external wall",
    "A wall forming part of the external envelope of a building subjected to simultaneous vertical gravity loads and lateral wind suction or pressure."
)

BasementWall = TAD(
    "basement wall",
    "A subterranean loadbearing or non-loadbearing masonry wall resisting lateral earth pressure and surface surcharges in addition to axial gravity loads."
)

ShearWallInSimplifiedMethod = TAD(
    "shear wall in simplified method",
    "A straight planar masonry wall having an effective length l >= 0.2 * h acting to provide overall transverse or longitudinal lateral stability against horizontal wind loads."
)

GableWall = TAD(
    "gable wall",
    "The triangular portion of an exterior end wall between the level of the eaves and the ridge of a pitched roof."
)

BackfillMaterial = TAD(
    "backfill material",
    "Clean, free-draining granular soil or crushed rock placed against the exterior face of basement masonry walls with adequate drainage."
)
