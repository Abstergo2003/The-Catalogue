try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Terms and definitions used in EN 1997-2 (Ground investigation and laboratory testing)

LaboratoryTest = TAD(
    "geotechnical laboratory test",
    "Standardized physical, mechanical, or chemical procedure performed in a testing laboratory on undisturbed or disturbed soil and rock specimens retrieved from boreholes."
)

AtterbergLimits = TAD(
    "Atterberg limits",
    "Empirical water content thresholds (liquid limit w_L, plastic limit w_P, and shrinkage limit w_S) defining transitions between rheological states in cohesive soils."
)

TriaxialCompressionTest = TAD(
    "triaxial compression test",
    "A shear strength test on a cylindrical soil specimen subjected to isotropic confining cell pressure and subsequent axial deviatoric loading to failure under unconsolidated-undrained (UU), consolidated-undrained (CU), or consolidated-drained (CD) conditions."
)

DirectShearTest = TAD(
    "direct shear test (shear box test)",
    "A laboratory test in which a soil specimen placed in a split metal box is sheared along a pre-determined horizontal plane under a constant normal vertical stress."
)

OedometerConsolidationTest = TAD(
    "oedometer consolidation test",
    "A one-dimensional compression test in a rigid ring preventing lateral strain, used to measure soil compressibility parameters (C_c, C_s, E_oed) and rate of primary consolidation (c_v)."
)

CompactionTest = TAD(
    "Proctor compaction test",
    "A standardized dynamic impact compaction test establishing the maximum dry density rho_d,max and optimum moisture content w_opt for engineered earthworks fill."
)

PermeabilityTest = TAD(
    "hydraulic conductivity (permeability) test",
    "A constant-head or falling-head laboratory test measuring the discharge rate of water through a soil specimen to calculate Darcy's coefficient of permeability k."
)

SampleQualityClass = TAD(
    "sample quality category / class",
    "Standardized ranking (Quality Classes 1 to 5 conforming to EN ISO 22475-1) indicating the degree of ground disturbance and the suitability of soil samples for laboratory testing."
)
