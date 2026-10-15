try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 2.1N
partial_factors_for_materials_for_ultimate_limit_states = Table(
    ["Design situations", r"$\gamma_C$ for concrete", r"$\gamma_S$ for reinforcing steel", r"$\gamma_S$ for prestressing steel"],
    [
        ["Persistent & Transient", 1.5, 1.15, 1.15],
        ["Accidental", 1.2, 1.0, 1.0]
    ],
    "Partial factors for materials for ultimate limit states",
    "The values for partial factors for materials for serviceability limit state verification should be taken as those given in the particular clauses of this Eurocode. The recommended value is 1,0."
)

# Table 3.1
strength_and_deformation_characteristics_for_concrete = Table(
    [
        "Strength class",
        r"$f_{ck}$ [MPa]",
        r"$f_{ck,cube}$ [MPa]",
        r"$f_{cm}$ [MPa]",
        r"$f_{ctm}$ [MPa]",
        r"$f_{ctk,0.05}$ [MPa]",
        r"$f_{ctk,0.95}$ [MPa]",
        r"$E_{cm}$ [GPa]",
        r"$\varepsilon_{c1}$ [‰]",
        r"$\varepsilon_{cu1}$ [‰]",
        r"$\varepsilon_{c2}$ [‰]",
        r"$\varepsilon_{cu2}$ [‰]",
        "n",
        r"$\varepsilon_{c3}$ [‰]",
        r"$\varepsilon_{cu3}$ [‰]"
    ],
    [
        ["C12/15", 12, 15, 20, 1.6, 1.1, 2.0, 27, 1.8, 3.5, 2.0, 3.5, 2.0, 1.75, 3.5],
        ["C16/20", 16, 20, 24, 1.9, 1.3, 2.5, 29, 1.9, 3.5, 2.0, 3.5, 2.0, 1.75, 3.5],
        ["C20/25", 20, 25, 28, 2.2, 1.5, 2.9, 30, 2.0, 3.5, 2.0, 3.5, 2.0, 1.75, 3.5],
        ["C25/30", 25, 30, 33, 2.6, 1.8, 3.3, 31, 2.1, 3.5, 2.0, 3.5, 2.0, 1.75, 3.5],
        ["C30/37", 30, 37, 38, 2.9, 2.0, 3.8, 33, 2.2, 3.5, 2.0, 3.5, 2.0, 1.75, 3.5],
        ["C35/45", 35, 45, 43, 3.2, 2.2, 4.2, 34, 2.25, 3.5, 2.0, 3.5, 2.0, 1.75, 3.5],
        ["C40/50", 40, 50, 48, 3.5, 2.5, 4.6, 35, 2.3, 3.5, 2.0, 3.5, 2.0, 1.75, 3.5],
        ["C45/55", 45, 55, 53, 3.8, 2.7, 4.9, 36, 2.4, 3.5, 2.0, 3.5, 2.0, 1.75, 3.5],
        ["C50/60", 50, 60, 58, 4.1, 2.9, 5.3, 37, 2.45, 3.5, 2.0, 3.5, 2.0, 1.75, 3.5],
        ["C55/67", 55, 67, 63, 4.2, 3.0, 5.5, 38, 2.5, 3.2, 2.2, 3.1, 1.75, 1.8, 3.1],
        ["C60/75", 60, 75, 68, 4.4, 3.1, 5.7, 39, 2.6, 3.0, 2.3, 2.9, 1.6, 1.9, 2.9],
        ["C70/85", 70, 85, 78, 4.6, 3.2, 6.0, 41, 2.7, 2.8, 2.4, 2.7, 1.45, 2.0, 2.7],
        ["C80/95", 80, 95, 88, 4.8, 3.4, 6.3, 42, 2.8, 2.8, 2.5, 2.6, 1.4, 2.2, 2.6],
        ["C90/105", 90, 105, 98, 5.0, 3.5, 6.6, 44, 2.8, 2.8, 2.6, 2.6, 1.4, 2.3, 2.6]
    ],
    "Strength and deformation characteristics for concrete",
    "Values of fck are characteristic cylinder strengths; fck,cube are characteristic cube strengths. Ecm values are secant moduli."
)

# Table 3.2
nominal_unrestrained_drying_shrinkage_values = Table(
    [r"$f_{ck}/f_{ck,cube}$ [MPa]", "RH 20%", "RH 40%", "RH 60%", "RH 80%", "RH 90%", "RH 100%"],
    [
        ["20/25", 0.62, 0.58, 0.49, 0.30, 0.17, 0.00],
        ["40/50", 0.48, 0.46, 0.38, 0.24, 0.13, 0.00],
        ["60/75", 0.38, 0.36, 0.30, 0.19, 0.10, 0.00],
        ["80/95", 0.30, 0.28, 0.24, 0.15, 0.08, 0.00],
        ["90/105", 0.27, 0.25, 0.21, 0.13, 0.07, 0.00]
    ],
    "Nominal unrestrained drying shrinkage values epsilon_cd,0 (in o/oo) for concrete with cement CEM Class N",
    "Expected mean values, with a coefficient of variation of about 30%."
)

# Table 3.3
values_for_kh = Table(
    [r"$h_0$ [mm]", r"$k_h$"],
    [
        [100, 1.0],
        [200, 0.85],
        [300, 0.75],
        [r"$\ge 500$", 0.70]
    ],
    "Values for kh in Expression (3.9)",
    "h0 is the notional size of the cross-section = 2Ac/u."
)

# Table 4.1
exposure_classes = Table(
    ["Class designation", "Description of the environment", "Informative examples where exposure classes may occur"],
    [
        ["X0", "For concrete without reinforcement or embedded metal: all exposures except where there is freeze/thaw, abrasion or chemical attack. For concrete with reinforcement or embedded metal: very dry", "Concrete inside buildings with very low air humidity"],
        ["XC1", "Dry or permanently wet", "Concrete inside buildings with low air humidity; Concrete permanently submerged in water"],
        ["XC2", "Wet, rarely dry", "Concrete surfaces subject to long-term water contact; Many foundations"],
        ["XC3", "Moderate humidity", "Concrete inside buildings with moderate or high air humidity; External concrete sheltered from rain"],
        ["XC4", "Cyclic wet and dry", "Concrete surfaces subject to water contact, not within exposure class XC2"],
        ["XD1", "Moderate humidity", "Concrete surfaces exposed to airborne chlorides"],
        ["XD2", "Wet, rarely dry", "Swimming pools; Concrete components exposed to industrial waters containing chlorides"],
        ["XD3", "Cyclic wet and dry", "Parts of bridges exposed to spray containing chlorides; Pavements; Car park slabs"],
        ["XS1", "Exposed to airborne salt but not in direct contact with sea water", "Structures near to or on the coast"],
        ["XS2", "Permanently submerged", "Parts of marine structures"],
        ["XS3", "Tidal, splash and spray zones", "Parts of marine structures"],
        ["XF1", "Moderate water saturation, without de-icing agent", "Vertical concrete surfaces exposed to rain and freezing"],
        ["XF2", "Moderate water saturation, with de-icing agent", "Vertical concrete surfaces of road structures exposed to freezing and airborne de-icing agents"],
        ["XF3", "High water saturation, without de-icing agents", "Horizontal concrete surfaces exposed to rain and freezing"],
        ["XF4", "High water saturation with de-icing agents or sea water", "Road and bridge decks exposed to de-icing agents; Concrete surfaces exposed to direct spray containing de-icing agents and freezing; Splash zone of marine structures exposed to freezing"],
        ["XA1", "Slightly aggressive chemical environment according to EN 206-1, Table 2", "Natural soils and ground water"],
        ["XA2", "Moderately aggressive chemical environment according to EN 206-1, Table 2", "Natural soils and ground water"],
        ["XA3", "Highly aggressive chemical environment according to EN 206-1, Table 2", "Natural soils and ground water"]
    ],
    "Exposure classes related to environmental conditions in accordance with EN 206-1",
    ""
)

# Table 4.2
minimum_cover_requirements_with_regard_to_bond = Table(
    ["Arrangement of bars", r"Minimum cover $c_{min,b}$"],
    [
        ["Separated", "Diameter of bar"],
        ["Bundled", "Equivalent diameter (phi_n) (see 8.9.1)"]
    ],
    "Minimum cover, cmin,b, requirements with regard to bond",
    "If the nominal maximum aggregate size is greater than 32 mm, cmin,b should be increased by 5 mm."
)

# Table 4.3N
recommended_structural_classification = Table(
    ["Criterion", "X0", "XC1", "XC2 / XC3", "XC4", "XD1", "XD2 / XS1", "XD3 / XS2 / XS3"],
    [
        ["Design Working Life of 100 years", "+2", "+2", "+2", "+2", "+2", "+2", "+2"],
        ["Strength Class", r"$\ge$ C30/37: -1", r"$\ge$ C30/37: -1", r"$\ge$ C35/45: -1", r"$\ge$ C40/50: -1", r"$\ge$ C40/50: -1", r"$\ge$ C40/50: -1", r"$\ge$ C45/55: -1"],
        ["Member with slab geometry", "-1", "-1", "-1", "-1", "-1", "-1", "-1"],
        ["Special Quality Control of concrete production", "-1", "-1", "-1", "-1", "-1", "-1", "-1"]
    ],
    "Recommended structural classification",
    "The recommended Structural Class (design working life of 50 years) is S4. The recommended minimum Structural Class is S1."
)

# Table 4.4N
minimum_cover_requirements_for_reinforcement_steel = Table(
    ["Structural Class", "X0", "XC1", "XC2 / XC3", "XC4", "XD1 / XS1", "XD2 / XS2", "XD3 / XS3"],
    [
        ["S1", 10, 10, 10, 15, 20, 25, 30],
        ["S2", 10, 10, 15, 20, 25, 30, 35],
        ["S3", 10, 10, 20, 25, 30, 35, 40],
        ["S4", 10, 15, 25, 30, 35, 40, 45],
        ["S5", 15, 20, 30, 35, 40, 45, 50],
        ["S6", 20, 25, 35, 40, 45, 50, 55]
    ],
    "Values of minimum cover, cmin,dur, requirements with regard to durability for reinforcement steel (mm)",
    ""
)

# Table 4.5N
minimum_cover_requirements_for_prestressing_steel = Table(
    ["Structural Class", "X0", "XC1", "XC2 / XC3", "XC4", "XD1 / XS1", "XD2 / XS2", "XD3 / XS3"],
    [
        ["S1", 10, 15, 20, 25, 30, 35, 40],
        ["S2", 10, 15, 25, 30, 35, 40, 45],
        ["S3", 10, 20, 30, 35, 40, 45, 50],
        ["S4", 10, 25, 35, 40, 45, 50, 55],
        ["S5", 15, 30, 40, 45, 50, 55, 60],
        ["S6", 20, 35, 45, 50, 55, 60, 65]
    ],
    "Values of minimum cover, cmin,dur, requirements with regard to durability for prestressing steel (mm)",
    ""
)

# Table 7.1N
recommended_values_of_wmax = Table(
    ["Exposure Class", "Reinforced / unbonded prestressed members (Quasi-permanent)", "Prestressed members with bonded tendons (Frequent)"],
    [
        ["X0, XC1", 0.4, 0.2],
        ["XC2, XC3, XC4", 0.3, 0.2],
        ["XD1, XD2, XS1, XS2, XS3", 0.3, "Decompression"]
    ],
    "Recommended values of wmax (mm)",
    "For X0, XC1 exposure classes, crack width has no influence on durability and this limit is set to guarantee acceptable appearance. For XD/XS classes, decompression requires bonded tendons to lie at least 25 mm within concrete in compression."
)

# Table 7.4N
basic_ratios_of_span_effective_depth = Table(
    ["Structural System", "K", r"Concrete highly stressed ($\rho = 1.5\%$)", r"Concrete lightly stressed ($\rho = 0.5\%$)"],
    [
        ["Simply supported beam, one- or two-way spanning simply supported slab", 1.0, 14, 20],
        ["End span of continuous beam or one-way continuous slab or two-way spanning slab continuous over one long side", 1.3, 18, 26],
        ["Interior span of beam or one-way or two-way spanning slab", 1.5, 20, 30],
        ["Slab supported on columns without beams (flat slab) (based on longer span)", 1.2, 17, 24],
        ["Cantilever", 0.4, 6, 8]
    ],
    "Basic ratios of span/effective depth for reinforced concrete members without axial compression",
    "Values obtained using Expression (7.16) for common cases (C30, sigma_s = 310 MPa)."
)

# Table 8.1N
minimum_mandrel_diameter = Table(
    ["Type / Configuration", "Bar diameter", "Minimum mandrel diameter"],
    [
        ["Bars and wire for bends, hooks and loops", r"$\phi \le 16$ mm", r"$4\phi$"],
        ["Bars and wire for bends, hooks and loops", r"$\phi > 16$ mm", r"$7\phi$"],
        ["Welded bent reinforcement and mesh bent after welding", r"$d \ge 3\phi$", r"$5\phi$"],
        ["Welded bent reinforcement and mesh bent after welding", r"$d < 3\phi$ or welding within curved zone", r"$20\phi$"]
    ],
    "Minimum mandrel diameter to avoid damage to reinforcement",
    "The mandrel size for welding within the curved zone may be reduced to 5phi where welding is carried out in accordance with prEN ISO 17660 Annex B."
)

# Table 8.2
anchorage_coefficients = Table(
    ["Influencing factor", "Type of anchorage", "In tension", "In compression"],
    [
        ["Shape of bars", "Straight", r"$\alpha_1 = 1.0$", r"$\alpha_1 = 1.0$"],
        ["Shape of bars", "Other than straight", r"$\alpha_1 = 0.7$ if $c_d > 3\phi$, else $1.0$", r"$\alpha_1 = 1.0$"],
        ["Concrete cover", "Straight", r"$\alpha_2 = 1 - 0.15(c_d - \phi)/\phi \in [0.7, 1.0]$", r"$\alpha_2 = 1.0$"],
        ["Concrete cover", "Other than straight", r"$\alpha_2 = 1 - 0.15(c_d - 3\phi)/\phi \in [0.7, 1.0]$", r"$\alpha_2 = 1.0$"],
        ["Confinement by transverse reinforcement", "All types", r"$\alpha_3 = 1 - K\lambda \in [0.7, 1.0]$", r"$\alpha_3 = 1.0$"],
        ["Confinement by welded transverse reinforcement", "All types", r"$\alpha_4 = 0.7$", r"$\alpha_4 = 0.7$"],
        ["Confinement by transverse pressure", "All types", r"$\alpha_5 = 1 - 0.04p \in [0.7, 1.0]$", "-"]
    ],
    "Values of alpha_1, alpha_2, alpha_3, alpha_4 and alpha_5 coefficients",
    "See EN 1992-1-1 Section 8.4.4 for definitions of lambda, K and p."
)

# Table 8.3
lap_coefficient_alpha_6 = Table(
    ["Percentage of lapped bars relative to total cross-section area", r"$\alpha_6$"],
    [
        ["< 25%", 1.0],
        ["33%", 1.15],
        ["50%", 1.4],
        ["> 50%", 1.5]
    ],
    "Values of the coefficient alpha_6",
    "Intermediate values may be determined by interpolation."
)

# Table C.1
properties_of_reinforcement = Table(
    ["Product form", "Characteristic yield strength fyk or f0.2k [MPa]", "Minimum value of k = (ft/fy)k", "Characteristic strain at maximum force e_uk [%]", "Bendability"],
    [
        ["Class A (Bars and de-coiled rods)", "400 to 600", r"$\ge 1.05$", r"$\ge 2.5$", "Bend/Rebend test"],
        ["Class B (Bars and de-coiled rods)", "400 to 600", r"$\ge 1.08$", r"$\ge 5.0$", "Bend/Rebend test"],
        ["Class C (Bars and de-coiled rods)", "400 to 600", r"$\ge 1.15, < 1.35$", r"$\ge 7.5$", "Bend/Rebend test"],
        ["Class A (Wire Fabrics)", "400 to 600", r"$\ge 1.05$", r"$\ge 2.5$", "Bend/Rebend test"],
        ["Class B (Wire Fabrics)", "400 to 600", r"$\ge 1.08$", r"$\ge 5.0$", "Bend/Rebend test"],
        ["Class C (Wire Fabrics)", "400 to 600", r"$\ge 1.15, < 1.35$", r"$\ge 7.5$", "Bend/Rebend test"]
    ],
    "Properties of reinforcement",
    "Valid for temperatures between -40 deg C and 100 deg C for reinforcement in the finished structure."
)
