try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Terms and definitions used in EN 1992-3 (Liquid retaining and containment structures)

ContainmentStructures = TAD(
    "containment structures",
    "Structures constructed from plain, reinforced, or prestressed concrete used for the storage or containment of liquids or granular solids (e.g. tanks, reservoirs, silos)."
)

LiquidRetainingStructures = TAD(
    "liquid retaining structures",
    "Structures or elements intended to hold liquids without unacceptable loss or percolation, classified by tightness classes according to leak tolerance."
)

TightnessClass0 = TAD(
    "tightness class 0",
    "Some degree of leakage acceptable, or leakage of liquids irrelevant."
)

TightnessClass1 = TAD(
    "tightness class 1",
    "Leakage to be limited to a small amount. Some surface staining or damp patches acceptable."
)

TightnessClass2 = TAD(
    "tightness class 2",
    "Leakage to be minimal. Appearance not to be impaired by staining. Cracks passing through full thickness of the section should generally be avoided."
)

TightnessClass3 = TAD(
    "tightness class 3",
    "No leakage permitted. Special measures (e.g. liners or prestress) will generally be required to ensure watertightness."
)

CompleteJoints = TAD(
    "complete joints",
    "Movement joints where complete discontinuity is provided in both reinforcement and concrete to allow free relative movements without restraint."
)

TransitionalThermalStrain = TAD(
    "transitional thermal strain",
    "An irrecoverable, time-independent strain which occurs in concrete heated while in a stressed condition."
)
