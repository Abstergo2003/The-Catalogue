try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Terms and definitions used in EN 1995-1-2 (Structural fire design)

CharringRate = TAD(
    "charring rate",
    "The linear velocity at which the pyrolysis front and charring line advances into the solid timber or glulam member under standard fire exposure (in mm/min)."
)

EffectiveCrossSectionMethod = TAD(
    "effective cross-section method",
    "A simplified design method in which an effective cross-section is obtained by removing the notional charring depth d_char,n plus a zero-strength layer d_0 = 7 mm, with initial ambient mechanical properties retained."
)

ReducedPropertiesMethod = TAD(
    "reduced properties method",
    "A design method where the cross-section is reduced only by the charring depth d_char, while mechanical strength and stiffness properties of the residual core are multiplied by reduction factors."
)

CharLayer = TAD(
    "char layer",
    "The layer of carbonized, burnt wood formed on fire-exposed faces that acts as an insulating thermal barrier due to its low thermal conductivity."
)

ZeroStrengthLayer = TAD(
    "zero-strength layer",
    "A heated wood layer immediately below the charcoal front with assumed zero load-bearing strength and stiffness (thickness d_0 = 7 mm)."
)

ResidualCrossSection = TAD(
    "residual cross-section",
    "The cross-section of the original timber member remaining after subtracting the depth of charring d_char."
)

DelayTimeOfCharring = TAD(
    "delay time of charring (t_ch)",
    "The elapsed time of fire exposure before charring of a timber member protected by fire claddings or linings initiates."
)

FailureTimeOfProtection = TAD(
    "failure time of protection (t_f)",
    "The fire duration at which fire-protective panels, linings, or insulations fall off or cease to protect the substrate timber member."
)
