try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 1
masonry_exposure_classes_MX = Table(
    ["Exposure Class", "Environmental description", "Examples of occurrence"],
    [
        ["MX1", "In a dry environment", "Internal walls and inner leaves of cavity walls in residential/office buildings"],
        ["MX2.1", "Exposed to moisture but not freeze/thaw and without salts", "External walls protected by eaves or cladding without frost risk"],
        ["MX2.2", "Subject to wetting without frost and without salts", "Internal walls in damp industrial rooms, laundries, or showers"],
        ["MX3.1", "Exposed to moisture and freeze/thaw without salts", "External unrendered walls in regions with winter frosts"],
        ["MX3.2", "Severe exposure to moisture and freeze/thaw", "Parapets, freestanding boundary walls, chimneys, earth retaining walls"],
        ["MX4", "Exposed to airborne salt or de-icing salt splashes", "External walls near seawater or coastal areas, bridge abutments"],
        ["MX5", "In aggressive chemical environment", "Industrial masonry exposed to chemical fumes or aggressive ground waters"]
    ],
    "Classification of micro-environmental exposure conditions for masonry (EN 1996-2 Table 1)",
    "Governs durability specification for masonry units, mortars, wall ties, and bed joint reinforcement."
)

# Table 2
selection_of_masonry_units_and_mortars_for_durability = Table(
    ["Exposure Class", "Clay units (freeze-thaw class)", "Calcium silicate units", "Aggregate concrete blocks", "Minimum mortar class"],
    [
        ["MX1", "F0 (passive) or F1 (moderate)", "Minimum compressive strength >= 10 N/mm2", "Category I or II, all densities", "M2.5 (general purpose)"],
        ["MX2.1 / MX2.2", "F1 (moderate frost resistance)", "Minimum compressive strength >= 15 N/mm2", "Dense aggregate concrete or high density AAC", "M5"],
        ["MX3.1 / MX3.2", "F2 (severe frost resistance)", "Frost resistant units with declared performance", "Dense concrete blocks with low water absorption", "M5 to M10"],
        ["MX4", "F2 (frost resistant) with low soluble salt content S2", "Sulphate resistant with declared marine suitability", "High-density concrete blocks with sulphate-resisting cement", "M10 (sulphate-resisting)"],
        ["MX5", "Chemical-resistant engineering brick (Class A/B)", "Special evaluation for chemical resistance", "Special chemical-resistant formulations", "M15 (acid/chemical resistant)"]
    ],
    "Acceptable combinations of masonry units and mortars for durability (EN 1996-2 Table 2)",
    "Ensures frost resistance and chemical durability over the 50-year design life."
)

# Table 3
minimum_specifications_and_spacing_for_cavity_wall_ties = Table(
    ["Cavity width [mm]", "Minimum tie density [ties/m2]", "Max horizontal spacing sh [mm]", "Max vertical spacing sv [mm]", "Extra ties at reveals/openings"],
    [
        ["50 <= w <= 75", 2.5, 900, 450, "3 ties per metre height within 225 mm of edge"],
        ["75 < w <= 100", 3.0, 750, 450, "3 ties per metre height within 225 mm of edge"],
        ["100 < w <= 150", 4.0, 600, 450, "3 ties per metre height within 225 mm of edge"],
        ["150 < w <= 300", 5.0, 450, 450, "3 ties per metre height within 225 mm of edge"]
    ],
    "Minimum tie density and spacing for cavity walls (EN 1996-2 Clause 2.3 Table 3)",
    "Stainless steel (EN 10088) or austenitic wire ties required in corrosive or external environments."
)

# Table 4
maximum_horizontal_spacing_of_movement_joints = Table(
    ["Masonry unit material", "Maximum joint spacing [m]", "Notes on movement characteristics"],
    [
        ["Clay brick masonry", 12.0, "Moisture expansion occurs irreversibly over early years"],
        ["Calcium silicate brick masonry", 8.0, "Drying shrinkage predominates"],
        ["Dense aggregate concrete blockwork", 6.0, "Drying shrinkage and thermal movement"],
        ["Autoclaved aerated concrete (AAC) blockwork", 6.0, "Substantial early drying shrinkage"],
        ["Manufactured stone masonry", 8.0, "Moderate drying shrinkage"]
    ],
    "Maximum horizontal spacing between vertical movement joints in external unreinforced walls (EN 1996-2 Table 4)",
    "Spacing may be increased when bed-joint reinforcement is provided."
)

# Table 5
execution_tolerances_for_masonry_walls = Table(
    ["Geometric parameter", "Permissible deviation (Class 1)", "Permissible deviation (Class 2)"],
    [
        ["Verticality per single storey (height <= 3m)", "+/- 10 mm", "+/- 7 mm"],
        ["Verticality over total building height (height > 10m)", "+/- 20 mm", "+/- 15 mm"],
        ["Straightness / alignment in horizontal plan (per 10m)", "+/- 10 mm", "+/- 7 mm"],
        ["Wall leaf thickness t", "+/- 5 mm", "+/- 3 mm"],
        ["Vertical mortar head joint alignment", "+/- 15 mm", "+/- 10 mm"]
    ],
    "Permissible geometric execution tolerances for masonry walls (EN 1996-2 Clause 3.4 Table 5)",
    "Ensures construction alignment satisfies initial eccentricity assumptions in design."
)
