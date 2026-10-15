try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Terms and definitions used in ENV 1992-1-4 (Lightweight aggregate concrete with closed structure)

LightweightAggregateConcrete = TAD(
    "lightweight aggregate concrete",
    "Concrete having a closed structure and an oven-dry density of not more than 2000 kg/m3 consisting of or containing a proportion of artificial or natural lightweight aggregates having a particle density of less than 2000 kg/m3."
)

ClosedStructure = TAD(
    "closed structure",
    "Structure so made and compacted as to retain no appreciable amount of entrapped air other than entrained air."
)
