try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Section 1.5.2 Additional terms and definitions used in EN 1992-1-1

PrecastStructures = TAD(
    "precast structures",
    "Precast structures are characterised by structural elements manufactured elsewhere than in the final position in the structure. In the structure, elements are connected to ensure the required structural integrity."
)

PlainOrLightlyReinforcedConcreteMembers = TAD(
    "plain or lightly reinforced concrete members",
    "Structural concrete members having no reinforcement (plain concrete) or less reinforcement than the minimum amounts defined in Section 9."
)

UnbondedAndExternalTendons = TAD(
    "unbonded and external tendons",
    "Unbonded tendons for post-tensioned members having ducts which are permanently ungrouted, and tendons external to the concrete cross-section (which may be encased in concrete after stressing, or have a protective membrane)."
)

Prestress = TAD(
    "prestress",
    "The process of prestressing consists in applying forces to the concrete structure by stressing tendons relative to the concrete member. Prestress is used globally to name all the permanent effects of the prestressing process, which comprise internal forces in the sections and deformations of the structure. Other means of prestressing are not considered in this standard."
)
