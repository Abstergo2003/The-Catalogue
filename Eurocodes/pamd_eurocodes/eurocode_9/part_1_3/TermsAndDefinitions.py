try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Terms and definitions used in EN 1999-1-3 / ENV 1999-2 (Structures susceptible to fatigue)

DetailCategory = TAD(
    "detail category (fatigue strength Delta_sigma_c)",
    "The numerical designation of a given structural detail, defined as the characteristic fatigue strength in MPa at 2 * 10^6 cycles."
)

FatigueDamage = TAD(
    "fatigue damage",
    "Structural degradation caused by repetitive cyclic loading leading to initiation and progressive stable growth of microscopic cracks into macroscopic fractures."
)

SNCurve = TAD(
    "S-N curve (Wöhler curve)",
    "A graphical or mathematical relationship relating the cyclic stress range Delta_sigma to the number of cycles to failure N on a double-logarithmic scale."
)

PalmgrenMinerRule = TAD(
    "Palmgren-Miner summation rule",
    "A cumulative linear fatigue damage hypothesis stating that failure occurs when the cumulative damage index D = sum(n_i / N_i) reaches 1.0."
)

DamageTolerantDesign = TAD(
    "damage tolerant method",
    "A design concept that permits fatigue cracks to develop during service life provided they can be detected and repaired through systematic scheduled in-service inspections before structural safety is compromised."
)

SafeLifeDesign = TAD(
    "safe life method",
    "A design concept requiring that the structure possesses a sufficiently low probability of fatigue failure during its specified design working life without relying on in-service crack detection."
)

CutOffLimit = TAD(
    "cut-off limit (Delta_sigma_L)",
    "The stress range threshold below which stress cycles are assumed to produce no contribution to cumulative fatigue damage under variable amplitude loading spectra."
)
