try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Section 1.5 Terms and definitions used in EN 1992-1-2

CriticalTemperatureOfReinforcement = TAD(
    "critical temperature of reinforcement",
    "The temperature of reinforcement at which failure of the member in fire situation (Criterion R) is expected to occur at a given steel stress level."
)

FireWall = TAD(
    "fire wall",
    "A wall separating two spaces (generally two buildings) that is designed for fire resistance and structural stability, and may include resistance to horizontal loading such that, in case of fire and failure of the structure on one side of the wall, fire spread beyond the wall is avoided."
)

MaximumStressLevel = TAD(
    "maximum stress level",
    "For a given temperature, the stress level at which the stress-strain relationship of steel is truncated to provide a yield plateau."
)

PartOfStructure = TAD(
    "part of structure",
    "Isolated part of an entire structure with appropriate support and boundary conditions."
)

ProtectiveLayers = TAD(
    "protective layers",
    "Any material or combination of materials applied to a structural member for the purpose of increasing its fire resistance."
)

ReducedCrossSection = TAD(
    "reduced cross section",
    "Cross section of the member in structure fire design used in the reduced cross section method. It is obtained from the residual cross section by removing parts of the cross section with assumed zero strength and stiffness."
)
