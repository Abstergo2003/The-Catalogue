try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Terms and definitions used in EN 1998-3 (Assessment and retrofitting of buildings)

SeismicAssessment = TAD(
    "seismic assessment",
    "Quantitative safety check evaluating whether an existing structure satisfies performance requirements under specified seismic hazard levels."
)

SeismicRetrofitting = TAD(
    "seismic retrofitting (strengthening)",
    "Structural modification of an existing building by adding new shear walls, steel bracings, RC jacketing, or composite FRP wrapping to enhance resistance and ductility."
)

KnowledgeLevel = TAD(
    "knowledge level (KL1, KL2, KL3)",
    "Stratification reflecting the degree of confidence and completeness of archival drawings, in-situ visual inspections, and non-destructive or destructive material testing."
)

ConfidenceFactor = TAD(
    "confidence factor (CF)",
    "A reduction factor dividing mean measured material strengths to account for uncertainties arising from limited site investigation (KL1: CF=1.35; KL2: CF=1.20; KL3: CF=1.00)."
)

PushoverAnalysis = TAD(
    "nonlinear static (pushover) analysis",
    "Analysis of a non-linear structural model subjected to permanent gravity loads and monotonically increasing lateral force profiles to establish the structural capacity curve."
)

NearCollapseLimitState = TAD(
    "Limit State of Near Collapse (NC)",
    "Performance state representing extreme earthquake shaking where the structure sustains heavy damage with minimal residual stiffness, near total collapse."
)

SignificantDamageLimitState = TAD(
    "Limit State of Significant Damage (SD)",
    "Performance state where the structure is significantly damaged with protected life safety and substantial economic repair feasibility (return period 475 years)."
)

DamageLimitationLimitState = TAD(
    "Limit State of Damage Limitation (DL)",
    "Performance state where damage is very light, structural members remain essentially elastic, and non-structural elements do not require substantial repairs."
)
