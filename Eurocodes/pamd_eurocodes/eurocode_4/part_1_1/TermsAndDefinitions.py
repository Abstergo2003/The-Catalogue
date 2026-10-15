try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Terms and definitions used in EN 1994-1-1 (General rules and rules for buildings)

CompositeMember = TAD(
    "composite member",
    "A structural member with components of concrete and of structural or cold-formed steel, interconnected by shear connection so as to limit the longitudinal slip between concrete and steel and the separation of one component from the other."
)

ShearConnection = TAD(
    "shear connection",
    "An interconnection between the concrete and steel components of a composite member that has sufficient strength and stiffness to enable the two components to be designed as parts of a single structural member."
)

CompositeBehaviour = TAD(
    "composite behaviour",
    "Behaviour which occurs after the shear connection has become effective due to hardening of concrete."
)

CompositeBeam = TAD(
    "composite beam",
    "A composite member subjected mainly to bending."
)

CompositeColumn = TAD(
    "composite column",
    "A composite member subjected mainly to compression or to compression and bending."
)

CompositeSlab = TAD(
    "composite slab",
    "A slab in which profiled steel sheets are used initially as permanent shuttering and subsequently combine structurally with the hardened concrete and act as tensile reinforcement in the finished floor."
)

CompositeFrame = TAD(
    "composite frame",
    "A framed structure in which some or all of the elements are composite members and most of the remainder are structural steel members."
)

CompositeJoint = TAD(
    "composite joint",
    "A joint between a composite member and another composite, steel or reinforced concrete member, in which reinforcement is taken into account in design for the resistance and the stiffness of the joint."
)

ProppedStructure = TAD(
    "propped structure or member",
    "A structure or member where the weight of concrete elements is applied to the steel elements which are supported in the span, or is carried independently until the concrete elements are able to resist stresses."
)

UnproppedStructure = TAD(
    "un-propped structure or member",
    "A structure or member in which the weight of concrete elements is applied to steel elements which are unsupported in the span."
)

UncrackedFlexuralStiffness = TAD(
    "un-cracked flexural stiffness",
    "The stiffness Ea*I1 of a cross-section of a composite member where I1 is the second moment of area of the effective equivalent steel section calculated assuming that concrete in tension is un-cracked."
)

CrackedFlexuralStiffness = TAD(
    "cracked flexural stiffness",
    "The stiffness Ea*I2 of a cross-section of a composite member where I2 is the second moment of area of the effective equivalent steel section calculated neglecting concrete in tension but including reinforcement."
)

Prestress = TAD(
    "prestress",
    "The process of applying compressive stresses to the concrete part of a composite member, achieved by tendons or by controlled imposed deformations."
)

FullShearConnection = TAD(
    "full shear connection",
    "A condition where the number and capacity of shear connectors provided is sufficient to develop the full plastic bending resistance of the composite cross-section."
)

PartialShearConnection = TAD(
    "partial shear connection",
    "A condition where the number of shear connectors provided is less than that for full shear connection, so that the bending resistance of the composite cross-section is limited by the shear resistance of the connectors."
)
