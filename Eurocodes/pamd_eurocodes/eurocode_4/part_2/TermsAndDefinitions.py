try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Terms and definitions used in EN 1994-2 (Composite bridges)

CompositeBridge = TAD(
    "composite bridge",
    "A highway, railway, footbridge, or viaduct superstructure comprising steel main girders (such as plate girders, box girders, or trusses) and an in-situ or precast reinforced or prestressed concrete deck slab acting compositely."
)

DoubleCompositeAction = TAD(
    "double composite action",
    "Structural behavior occurring near intermediate supports of continuous bridges where both the top concrete deck slab and an additional bottom concrete flange slab (or bottom concrete infill) act compositely with the steel girder."
)

InvertedTCompositeGirder = TAD(
    "inverted-T composite girder",
    "A composite bridge deck configuration where precast inverted-T concrete beams or steel tees combine structurally with a cast-in-place concrete topping slab."
)

SlabCastingSequence = TAD(
    "slab casting sequence",
    "The planned chronological order of concrete deck segment pours along the bridge length, designed to control early-age thermal shrinkage, concrete cracking, and redistribution of self-weight bending moments."
)

LongitudinalShearConnection = TAD(
    "longitudinal shear connection in bridges",
    "The system of headed shear studs, block connectors, or continuous perforations transferring longitudinal interface shear between the concrete deck slab and steel main girders under static and cyclic traffic loading."
)

BridgeDeckSlab = TAD(
    "bridge deck slab",
    "A reinforced or prestressed concrete slab serving directly as the traffic roadway or trackbed and functioning as the top compression or tension flange of the primary composite girder system."
)

FatigueShearConnector = TAD(
    "fatigue of shear connectors",
    "Progressive cyclic damage and potential shear fatigue failure of welded headed studs or connectors subjected to high-cycle variable amplitude traffic shear stresses."
)

TensionStiffeningBridge = TAD(
    "tension stiffening in bridge decks",
    "The contribution of uncracked concrete between tensile cracks to the tensile stiffness of the longitudinal deck reinforcement in hogging moment regions of continuous bridge girders."
)
