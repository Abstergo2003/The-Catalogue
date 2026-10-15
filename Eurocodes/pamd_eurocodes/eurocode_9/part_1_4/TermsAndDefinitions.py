try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Terms and definitions used in EN 1999-1-4 (Cold-formed structural sheeting)

ProfiledSheeting = TAD(
    "profiled sheeting",
    "Cold-formed thin-gauge aluminium trapezoidal, sinusoidal, or ribbed sheeting designed to carry transverse gravity, snow, and wind loads as well as in-plane shear forces."
)

WebCrippling = TAD(
    "web crippling",
    "A localized limit state failure mode where the thin web of a cold-formed profiled sheet undergoes out-of-plane buckling, crushing, or crippling under a concentrated bearing support reaction or applied load."
)

DistortionalBuckling = TAD(
    "distortional buckling",
    "An instability failure mode involving lateral and rotational displacement of longitudinal flange edge or intermediate stiffeners accompanied by cross-sectional shape distortion."
)

DiaphragmAction = TAD(
    "stressed skin diaphragm action",
    "The structural capacity of interconnected profiled roof or wall sheeting panels to resist in-plane shear forces and provide lateral and torsional restraint to supporting purlins, rafters, and building frames."
)

EffectiveCrossSectionSheeting = TAD(
    "effective cross-section of sheeting",
    "A reduced cross-sectional geometry evaluated by substituting the flat compression widths of flanges and webs with reduced effective widths b_eff to account for post-critical local plate buckling."
)
