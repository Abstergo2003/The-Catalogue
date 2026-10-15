try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Terms and definitions used in EN 1995-2 (Bridges)

TimberBridge = TAD(
    "timber bridge",
    "A road bridge, footbridge, cycle bridge, or railway bridge whose primary structural deck or superstructure load-bearing components are made of structural timber or glued laminated timber."
)

StressLaminatedDeck = TAD(
    "stress-laminated timber deck (SLT)",
    "A bridge deck slab built from vertical timber laminations placed side-by-side on edge and compressed transversely by high-strength post-tensioned steel bars to transmit vertical shear and transverse bending by friction."
)

GluedLaminatedBridgeGirder = TAD(
    "glued laminated bridge girder",
    "Deep longitudinal glulam beams, arches, or trusses supporting the bridge roadway and transferring vehicular actions to bridge abutments and piers."
)

CrossLaminatedTimberDeck = TAD(
    "cross-laminated timber deck (CLT)",
    "A solid engineered timber panel composed of cross-laminated timber boards serving as a two-way load-distributing bridge deck plate."
)

TransversePrestressing = TAD(
    "transverse prestressing",
    "Post-tensioning applied perpendicularly across the timber laminations to maintain adequate interlaminar friction and prevent joint opening under dynamic wheel loads."
)

ServiceClass3Bridge = TAD(
    "service class 3 bridge environment",
    "Outdoor environmental exposure class characteristic of bridges where structural timber is subject to weather, driving rain, and higher equilibrium moisture contents (often exceeding 20%)."
)

FatigueInTimberBridges = TAD(
    "fatigue in timber bridges",
    "Progressive structural degradation of timber elements and metal fasteners under high-cycle repeated vehicular axle loads."
)

DeckWaterproofing = TAD(
    "deck waterproofing system",
    "A protective impermeable membrane or asphalt paving course applied directly over the timber deck surface to prevent rainwater infiltration into laminations and joints."
)
