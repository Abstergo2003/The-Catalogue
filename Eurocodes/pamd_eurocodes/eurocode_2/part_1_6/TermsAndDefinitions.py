try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Terms and definitions used in ENV 1992-1-6 (Plain and lightly reinforced concrete structures)

PlainConcreteMember = TAD(
    "plain concrete member",
    "Structural concrete member having no reinforcement (plain concrete) or less reinforcement than the minimum amounts defined for reinforced concrete."
)

StripAndPadFootings = TAD(
    "strip and pad footings",
    "Plain concrete foundation elements where flexural and tensile stresses are resisted entirely or primarily by the tensile capacity of unreinforced concrete."
)

PlainConcreteWalls = TAD(
    "plain concrete walls",
    "Plain concrete walls mainly subjected to compression other than that due to prestressing, resisting vertical loads and out-of-plane lateral actions."
)

EffectiveCrossSection = TAD(
    "effective cross section",
    "The reduced portion of an uncracked plain concrete section assuming a uniform compressive stress distribution in equilibrium with the applied eccentric axial force."
)
