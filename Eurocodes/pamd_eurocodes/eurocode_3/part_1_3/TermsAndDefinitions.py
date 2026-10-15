try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Terms and definitions used in EN 1993-1-3 (Cold-formed members and sheeting)

ColdFormedMembers = TAD(
    "cold-formed members",
    "Structural members cold-formed from coated or uncoated thin gauge hot-rolled or cold-rolled steel strip or sheet without the application of heat."
)

Sheeting = TAD(
    "sheeting",
    "Cold-formed profiled sheet with trapezoidal, sinusoidal or other corrugations, used as cladding, roofing, or decking."
)

BasicYieldStrength = TAD(
    "basic yield strength",
    "The nominal yield strength of the flat steel sheet material before cold-forming."
)

EffectiveCoreThickness = TAD(
    "effective core thickness",
    "Nominal steel sheet thickness minus the thickness of zinc or metallic and organic protective coatings."
)

DistortionalBuckling = TAD(
    "distortional buckling",
    "Instability mode of thin-walled members involving lateral displacement and cross-sectional distortion of intermediate or edge stiffeners."
)

LocalBuckling = TAD(
    "local buckling",
    "Buckling of individual flat plate elements without overall displacement or cross-sectional distortion."
)

WebCrippling = TAD(
    "web crippling",
    "Local crushing, yielding or crippling of thin webs under high concentrated transverse forces or support reactions."
)

StressedSkinDesign = TAD(
    "stressed skin design",
    "Design method where profiled sheeting acts as a structural diaphragm to resist in-plane shear forces and stabilize the structure."
)
