try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Section 1.3 Terms and definitions used in EN 1993-1-5 (Plated structural elements)

PlatedStructure = TAD(
    "plated structure",
    "A structure built up from nominally flat plates which are joined together; the plates may be stiffened or unstiffened."
)

Stiffener = TAD(
    "stiffener",
    "A plate or section attached to a plate to resist buckling or to strengthen the plate; denoted longitudinal if parallel to member or transverse if perpendicular."
)

StiffenedPlate = TAD(
    "stiffened plate",
    "A plate with transverse or longitudinal stiffeners or both."
)

Subpanel = TAD(
    "subpanel",
    "An unstiffened plate portion surrounded by flanges and/or stiffeners."
)

EffectiveWidth = TAD(
    "effective width",
    "The gross cross-section or width reduced for effects of plate buckling (effectivep), shear lag (effectives), or both (effective)."
)

PlateBuckling = TAD(
    "plate buckling",
    "Buckling of flat plate elements subjected to in-plane direct stresses (compression, bending) or shear stresses."
)

TensionFieldAction = TAD(
    "tension field action",
    "Post-critical shear resistance mechanism where thin web plates develop diagonal tensile membrane stresses anchored by rigid end posts, transverse stiffeners, and flanges."
)
