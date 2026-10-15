try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

BulkWeightDensity = TAD(
    "bulk weight density",
    "the bulk weight density is the overall weight per unit volume of a material, including a normal distribution of micro-voids, voids and pores"
)
AngleOfRepose = TAD(
    "angle of repose",
    "the angle which the natural slope of the sides of a heaped pile of loose material makes to the horizontal"
)
GrossWeightOfVehicle = TAD(
    "gross weight of vehicle",
    "the gross weight of a vehicle includes the self-weight of the vehicle together with the maximum weight of the goods it is permitted to carry"
)
StructuralElements = TAD(
    "structural elements",
    "structural elements comprise the primary structural frame and supporting structures. For bridges, structural elements comprise girders, structural slabs and elements providing support such as cable stays"
)
NonStructuralElements = TAD(
    "non structural elements",
    "non structural elements are those that include completion and finishing elements connected with the structure, including road surfacing and non-structural parapets. They also include services and machinery fixed permanently to, or within, the structure"
)
Partitions = TAD(
    "partitions",
    "non load bearing walls"
)
MovablePartitions = TAD(
    "movable partitions",
    "movable partitions are those which can be moved on the floor, be added or removed or re-built at another place"
)
