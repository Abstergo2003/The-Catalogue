try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Section 1.4 Terms and definitions used in EN 1993-1-1

Frame = TAD(
    "frame",
    "Portion of a structure, comprising an assembly of directly connected structural elements, designed to act together to resist load. This term refers to both rigid-jointed frames and triangulated frames, covering both plane frames and three-dimensional frames."
)

SubFrame = TAD(
    "sub-frame",
    "A frame which forms part of a larger frame, but is treated as an isolated frame in a structural analysis."
)

TypeOfFraming = TAD(
    "type of framing",
    "Terms used to distinguish between frames which are simple (joints not required to resist moments), semi-continuous (structural properties of connections considered in global analysis), or continuous (only structural properties of members considered in global analysis)."
)

GlobalAnalysis = TAD(
    "global analysis",
    "The determination of a consistent set of internal forces and moments in a structure, which are in equilibrium with a particular set of actions on the structure."
)

SystemLength = TAD(
    "system length",
    "Distance between two adjacent points at which a member is braced against lateral displacement in a given plane, or between one such point and the end of the member."
)

BucklingLength = TAD(
    "buckling length",
    "System length of an otherwise similar member with pinned ends, which has the same buckling resistance as a given member."
)

ShearLag = TAD(
    "shear lag",
    "Non-uniform distribution of longitudinal stress across wide flanges of a beam or girder caused by in-plane shear deformations of the flange."
)

CapacityDesign = TAD(
    "capacity design",
    "Design method in which non-dissipative components are proportioned to resist the maximum forces that can be transmitted by ductile dissipative components."
)
