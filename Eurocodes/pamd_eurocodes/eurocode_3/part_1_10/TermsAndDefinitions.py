try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Terms and definitions used in EN 1993-1-10 (Material toughness and through-thickness properties)

BrittleFracture = TAD(
    "brittle fracture",
    "Sudden, catastrophic failure of a steel component characterized by rapid crack propagation at stress levels below general yield."
)

CharpyVNotchImpactEnergy = TAD(
    "Charpy V-notch impact energy",
    "Energy absorbed by a standardized Charpy V-notch specimen when fractured under impact at a specified test temperature."
)

DesignTemperature = TAD(
    "design temperature",
    "The lowest service temperature T_Ed expected to occur in the steel element during its design working life."
)

ReferenceTemperature = TAD(
    "reference temperature",
    "The temperature T_Ed adjusted for strain rate, cold-forming and member geometry used to assess brittle fracture susceptibility."
)

LamellarTearing = TAD(
    "lamellar tearing",
    "Sub-surface cracking of rolled steel products along planes of non-metallic inclusions caused by through-thickness tensile welding strains."
)

ThroughThicknessProperties = TAD(
    "through-thickness properties",
    "Ductility and reduction of area in the direction perpendicular to the rolling surface of a steel plate or wide flat."
)

QualityClass = TAD(
    "quality class",
    "Designation (Z15, Z25, Z35 according to EN 10164) indicating minimum required through-thickness reduction of area to resist lamellar tearing."
)
