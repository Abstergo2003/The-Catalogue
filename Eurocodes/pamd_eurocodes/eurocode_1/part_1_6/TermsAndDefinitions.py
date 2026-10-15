try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

AuxiliaryConstructionWorks = TAD(
    "auxiliary construction works",
    "any works associated with the construction processes that are not required after use when the related execution activities are completed and they can be removed (e.g. falsework, scaffolding, propping systems, cofferdam, bracing, launching nose)"
)
ConstructionLoad = TAD(
    "construction load",
    "load that can be present due to execution activities, but is not present when the execution activities are completed"
)
