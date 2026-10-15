try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Terms and definitions used in DD ENV 1997-3 (Ground investigation and field testing)

ConePenetrationTest = TAD(
    "cone penetration test (CPT / CPTU)",
    "An in-situ sounding method in which an instrumented cylindrical steel cone is pushed vertically into ground at a constant rate (20 mm/s) to record cone tip resistance q_c, sleeve friction f_s, and pore water pressure u_2."
)

StandardPenetrationTest = TAD(
    "standard penetration test (SPT)",
    "A dynamic borehole penetration test measuring the number of blows N required to drive a thick-walled split-barrel sampler 300 mm into the ground under a 63.5 kg hammer falling freely through 760 mm."
)

PressuremeterTest = TAD(
    "Ménard pressuremeter test (PMT)",
    "An in-situ borehole expansion test in which a cylindrical probe with flexible rubber membrane expands radially against borehole walls to determine the pressuremeter modulus E_M and limit pressure p_LM."
)

FlatDilatometerTest = TAD(
    "flat dilatometer test (Marchetti DMT)",
    "An in-situ test pushing a blade with an expandable circular steel membrane into the ground to measure contact lift-off pressure p_0 and 1.1 mm expansion pressure p_1."
)

FieldVaneTest = TAD(
    "field vane shear test (FVT)",
    "An in-situ test in which a four-bladed rectangular steel vane pushed into soft saturated clay is rotated at a constant angular rate to measure peak and remoulded undrained shear strength c_fv."
)

DynamicProbing = TAD(
    "dynamic probing test (DP)",
    "Continuous dynamic penetration sounding measuring the resistance of ground strata to the driving of a pointed steel cone under standardized hammer blows."
)

PlateLoadingTest = TAD(
    "plate loading test (PLT)",
    "An in-situ load test applying incremental vertical forces to a rigid steel plate placed on a prepared ground surface to measure settlement, deformation modulus, and subgrade reaction modulus k_s."
)

Piezocone = TAD(
    "piezocone (CPTU)",
    "A specialized cone penetrometer fitted with a porous ceramic/polyethylene filter and pressure transducer enabling simultaneous recording of penetration pore pressure and dissipation rates."
)
