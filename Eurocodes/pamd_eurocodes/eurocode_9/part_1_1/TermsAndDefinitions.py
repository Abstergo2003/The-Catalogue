try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Terms and definitions used in EN 1999-1-1 / ENV 1999-1-1 (General structural rules for aluminium)

HeatAffectedZone = TAD(
    "heat-affected zone (HAZ)",
    "The region of parent metal adjacent to a fusion weld which is thermally affected by the heat of welding, leading to local metallurgical degradation and reduction of mechanical strength properties."
)

HAZSoftening = TAD(
    "HAZ softening",
    "The reduction in proof strength and ultimate tensile strength occurring within the heat-affected zone of heat-treatable or strain-hardened aluminium alloys as a consequence of welding heat."
)

CrossSectionClass = TAD(
    "cross-section class (Class 1, 2, 3, 4)",
    "Classification defining the extent to which local plate buckling limits the cross-sectional resistance and plastic rotational capacity of aluminium members."
)

EffectiveThickness = TAD(
    "effective thickness (t_eff)",
    "A reduced fictitious plate thickness applied to slender compression elements in Class 4 sections to account for post-critical local buckling, calculated as t_eff = rho_c * t."
)

BucklingClass = TAD(
    "buckling class (Class A, Class B)",
    "Categorization of aluminium structural cross-sections and alloys governing the selection of the column buckling curve and imperfection factor alpha."
)

ExtrudedProfile = TAD(
    "extruded profile",
    "A structural cross-sectional shape produced by forcing a heated aluminium cylindrical billet through a hardened steel die under high hydraulic pressure."
)

WroughtAlloy = TAD(
    "wrought aluminium alloy",
    "An aluminium alloy primarily intended for fabrication into semi-finished forms (sheets, plates, extrusions, drawn tubes, forgings) by mechanical plastic deformation."
)

HeatTreatableAlloy = TAD(
    "heat-treatable alloy",
    "An aluminium alloy (e.g. 6000 and 7000 series) whose mechanical strength can be significantly increased by solution heat treatment, quenching, and subsequent artificial or natural precipitation ageing."
)
