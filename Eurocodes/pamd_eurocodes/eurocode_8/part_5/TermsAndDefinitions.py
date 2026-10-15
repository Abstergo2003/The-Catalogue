try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Terms and definitions used in EN 1998-5 (Foundations, retaining structures and geotechnical aspects)

SoilLiquefaction = TAD(
    "soil liquefaction",
    "A phenomenon in which saturated, loose cohesionless soils temporarily lose shear strength and stiffness due to buildup of excess pore water pressure under cyclic earthquake shaking."
)

CyclicStressRatio = TAD(
    "cyclic stress ratio (CSR)",
    "The average earthquake-induced cyclic shear stress divided by the initial effective vertical overburden pressure acting at a given soil depth."
)

CyclicResistanceRatio = TAD(
    "cyclic resistance ratio (CRR)",
    "The cyclic shear stress ratio that causes liquefaction in a specified number of cycles, evaluated from in-situ SPT, CPT, or shear wave velocity tests."
)

MononobeOkabeMethod = TAD(
    "Mononobe-Okabe method",
    "A pseudo-static limit equilibrium analytical method extending Coulomb's wedge theory to calculate seismic active and passive lateral earth pressures on retaining walls."
)

TopographicAmplification = TAD(
    "topographic amplification",
    "The amplification of seismic ground motion occurring at the crest of ridges, isolated cliffs, and steep slopes caused by focalization and diffraction of seismic waves."
)

KinematicInteraction = TAD(
    "kinematic interaction",
    "The component of soil-structure interaction whereby the presence of stiff foundation elements modifies the free-field incident seismic wavefield, independent of superstructure inertia."
)

InertialInteraction = TAD(
    "inertial interaction",
    "The dynamic interaction between foundation and surrounding soil caused by base shear forces and overturning moments transmitted by the vibrating superstructure."
)

PseudoStaticAnalysis = TAD(
    "pseudo-static analysis",
    "A simplified engineering analysis method where dynamic seismic accelerations are converted into equivalent static lateral and vertical inertia body forces."
)
