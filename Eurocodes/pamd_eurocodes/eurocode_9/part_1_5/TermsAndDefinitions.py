try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Terms and definitions used in EN 1999-1-5 (Shell structures)

AluminiumShellStructure = TAD(
    "aluminium shell structure",
    "A three-dimensional curved surface structure fabricated from curved aluminium plates or extruded panels (silos, tanks, ducts, domes) resisting external loads predominantly through membrane stresses."
)

MeridionalBuckling = TAD(
    "meridional buckling",
    "An axisymmetric or non-axisymmetric diamond-pattern buckling mode occurring in cylindrical or conical shells subjected to axial compression or global bending moments."
)

CircumferentialBuckling = TAD(
    "circumferential buckling",
    "An instability mode characterized by inward or outward periodic wave buckles around the circumference of a shell under external lateral pressure or partial vacuum."
)

KnockDownFactor = TAD(
    "knock-down factor (alpha)",
    "An empirical reduction factor multiplying the classical linear elastic critical buckling stress to account for the extreme sensitivity of thin shells to geometric imperfections and residual stresses."
)

ToleranceQualityClass = TAD(
    "tolerance quality class (Class A, Class B, Class C)",
    "Fabrication and erection tolerance standard defining maximum permissible out-of-roundness, dimple depth, and misalignment across welded seams (Class A: Excellent, Class B: High, Class C: Normal)."
)
