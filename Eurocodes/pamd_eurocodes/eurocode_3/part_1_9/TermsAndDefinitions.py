try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Terms and definitions used in EN 1993-1-9 (Fatigue)

Fatigue = TAD(
    "fatigue",
    "The process of progressive and localized structural damage occurring when a material is subjected to cyclic loading at stress levels below the ultimate tensile strength."
)

StressRange = TAD(
    "stress range",
    "The algebraic difference between the maximum and minimum stress in a cycle."
)

DetailCategory = TAD(
    "detail category",
    "Numerical designation given to a particular structural detail indicating its reference fatigue strength Delta_sigma_c (in N/mm2) at 2 * 10^6 cycles."
)

ConstantAmplitudeFatigueLimit = TAD(
    "constant amplitude fatigue limit",
    "The stress range limit Delta_sigma_D below which fatigue damage will not occur under constant amplitude stress cycles (at 5 * 10^6 cycles for normal stress)."
)

CutOffLimit = TAD(
    "cut-off limit",
    "The stress range limit Delta_sigma_L below which stress ranges do not contribute to fatigue damage under variable amplitude loading (at 10^8 cycles)."
)

DamageEquivalentFactor = TAD(
    "damage equivalent factor",
    "Factor lambda which relates the actual fatigue spectrum of cyclic actions to a damage equivalent reference stress range."
)

CumulativeDamage = TAD(
    "cumulative damage",
    "The accumulated ratio of applied cycles to endurance cycles summed across all stress ranges, evaluated using Palmgren-Miner's rule (D <= 1.0)."
)

RainflowMethod = TAD(
    "rainflow method",
    "A cycle counting algorithm widely used to extract closed stress-strain hysteresis loops from complex variable-amplitude stress histories."
)
