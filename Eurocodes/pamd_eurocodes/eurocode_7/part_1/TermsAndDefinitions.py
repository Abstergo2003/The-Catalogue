try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Terms and definitions used in EN 1997-1 (General rules)

GeotechnicalCategory = TAD(
    "geotechnical category",
    "Classification establishing the necessary geotechnical investigations, design calculations, and construction checks based on structural complexity and ground risk (Category 1: simple, negligible risk; Category 2: conventional structures; Category 3: complex, unusual ground or high risk)."
)

CharacteristicValueOfGeotechnicalParameter = TAD(
    "characteristic value of a geotechnical parameter",
    "A cautious estimate of the value affecting the occurrence of the limit state, taking into account field and laboratory measurements, geological history, and structural stiffness."
)

DerivedValue = TAD(
    "derived value",
    "A value of a geotechnical parameter deduced from field or laboratory test results using theoretical relations, empirical correlations, or established experience."
)

DesignApproach1 = TAD(
    "Design Approach 1 (DA1)",
    "A design procedure requiring two separate calculations: Combination 1 (A1 + M1 + R1) checks structural sizing under high action factors; Combination 2 (A2 + M2 + R1) checks geotechnical sizing under unfavorable material factors."
)

DesignApproach2 = TAD(
    "Design Approach 2 (DA2)",
    "An action (effect) and resistance factor approach where a single calculation is performed applying partial factors to actions/effects (A1) and to ground resistances (R2), with material properties unfactored (M1)."
)

DesignApproach3 = TAD(
    "Design Approach 3 (DA3)",
    "An action and material factor approach where partial factors are applied to actions from the superstructure (A1 or A2) and simultaneously to ground strength parameters (M2), using resistance factors R3 = 1.0."
)

SpreadFoundation = TAD(
    "spread foundation (shallow foundation)",
    "A foundation element (pad, strip footing, or raft) that transmits building loads directly to the ground at or near ground surface level."
)

PileFoundation = TAD(
    "pile foundation (deep foundation)",
    "A slender structural element installed or cast into the ground to transfer loads to deeper, more competent strata by shaft friction and/or base resistance."
)

RetainingStructure = TAD(
    "retaining structure",
    "A structural wall (gravity wall, cantilever reinforced concrete wall, anchored sheet-pile wall, or diaphragm wall) constructed to retain ground at a higher level than that in front."
)

UpliftUPL = TAD(
    "uplift failure (UPL)",
    "Loss of equilibrium of a structure or ground due to buoyancy or excessive upward pore water pressures exceeding downward gravity forces."
)

HydraulicHeaveHYD = TAD(
    "hydraulic heave (HYD)",
    "Upward seepage failure of ground caused by severe hydraulic pore pressure gradients below excavations, resulting in boiling, quick conditions, or internal erosion (piping)."
)
