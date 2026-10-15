try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Terms and definitions used in EN 1995-1-1 (General - Common rules and rules for buildings)

SolidTimber = TAD(
    "solid timber",
    "Sawn structural timber members visually or machine graded according to strength classes (EN 338)."
)

GluedLaminatedTimber = TAD(
    "glued laminated timber (glulam)",
    "A structural timber product formed by bonding together horizontal wood laminations with parallel grain directions conforming to EN 1194 / EN 14080."
)

LaminatedVeneerLumber = TAD(
    "laminated veneer lumber (LVL)",
    "A structural wood-based product fabricated from rotary-peeled wood veneers bonded together with parallel grain orientation throughout."
)

ServiceClass = TAD(
    "service class",
    "Classification characterized by the moisture content in the timber corresponding to specified environmental temperature and relative humidity conditions (Service Classes 1, 2, and 3)."
)

LoadDurationClass = TAD(
    "load-duration class",
    "Classification of actions according to the accumulated duration of the characteristic load: permanent (>10 years), long-term (6 months to 10 years), medium-term (1 week to 6 months), short-term (<1 week), or instantaneous."
)

CharacteristicValue = TAD(
    "characteristic value",
    "Material property value corresponding to a prescribed probability (normally 5% fractile) of not being attained in an unlimited test series."
)

EquilibriumMoistureContent = TAD(
    "equilibrium moisture content",
    "The moisture content at which wood neither gains nor loses moisture to the surrounding air."
)

MoistureContent = TAD(
    "moisture content",
    "The mass of water contained in wood expressed as a percentage of its oven-dry mass."
)

DowelFastener = TAD(
    "dowel-type fastener",
    "A cylindrical rod-like fastener (dowel, bolt, nail, or screw) installed into pre-bored or non-prebored holes to transmit lateral shear loads perpendicular to the fastener axis."
)

LoadSharingSystem = TAD(
    "load-sharing system",
    "A structural assembly of equally spaced parallel timber members interconnected by continuous transverse distribution elements, allowing an increase in design strength via k_sys (k_sys = 1.10)."
)

GrainDirection = TAD(
    "grain direction",
    "The principal longitudinal orientation of wood fibers and tracheids, defining the primary anisotropic mechanical axis."
)
