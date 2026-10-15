try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 4.3.1
horizontal_forces_impact_on_substructures_over_roadways = Table(
    ["Type of traffic under the bridge", "Type of vehicle", "Force $F_{d,x}$ [kN]", "Force $F_{d,y}$ [kN]"],
    [
        ["Motorway", "Lorry", BRange(1000, 2500, 1000), BRange(500, 1250, 500)],
        ["Country road (< 80 km/h)", "Lorry", BRange(750, 2500, 750), BRange(375, 1250, 375)],
        ["Urban area (< 60 km/h)", "Lorry", BRange(500, 2500, 500), BRange(250, 1250, 250)],
        ["Courtyards and parking garages (< 20 km/h)", "Cars", BRange(50, 100, 50), BRange(25, 50, 25)],
        ["Courtyards and parking garages (< 20 km/h)", "Lorry", BRange(150, 300, 150), BRange(75, 150, 75)]
    ],
    "Horizontal static equivalent design forces due to impact on members supporting structures over or near roadways",
    "x = direction of normal travel; y = perpendicular to travel direction. Applied between 0.5 and 1.5 m above carriageway."
)

# Table 4.3.2
impact_loads_on_horizontal_structural_members_above_roadways = Table(
    ["Type of traffic", "Type of vehicle", "Force $F_{d,x}$ [kN]", "Force $F_{d,y}$ [kN]"],
    [
        ["Motorway", "Lorry", BRange(1000, 2000, 1000), BRange(500, 1000, 500)],
        ["Country road (< 80 km/h)", "Lorry", BRange(750, 2000, 750), BRange(375, 1000, 375)],
        ["Urban area (< 60 km/h)", "Lorry", BRange(500, 2000, 500), BRange(250, 1000, 250)],
        ["Courtyards and parking garages", "Lorry", BRange(150, 300, 150), BRange(75, 150, 75)]
    ],
    "Impact loads on horizontal structural members above roadways",
    "For bridge superstructures with clearance under required minimum."
)

# Table 4.5.1
classes_of_structures_subject_to_railway_impact = Table(
    ["Class", "Description"],
    [
        ["Class A", "Structures that span across or near operational railway that are permanently occupied or gathering places for people or consist of more than one storey"],
        ["Class B", "Massive structures spanning across operational railway such as bridges carrying vehicular traffic or single storey buildings not permanently occupied"]
    ],
    "Classes of structures subject to impact from derailed traffic",
    ""
)

# Table 4.5.2
horizontal_impact_forces_railways_class_A = Table(
    ["Distance s from element to track centreline", "Force $F_{d,x}$ [kN]", "Force $F_{d,y}$ [kN]"],
    [
        ["s < 3 m", "Project specific (Annex B.8)", "Project specific (Annex B.8)"],
        ["3 m <= s <= 5 m (continuous walls)", 4000, 1500],
        ["s > 5 m", 0, 0]
    ],
    "Horizontal static equivalent design forces due to impact for class A structures over or alongside railways",
    "x = track direction; y = perpendicular to track direction."
)

# Table A.1
categorisation_of_consequences_classes_accidental = Table(
    ["Class", "Building Type and Occupancy Examples"],
    [
        ["Class 1", "Single occupancy houses <= 4 storeys; Agricultural buildings; Buildings into which people rarely go"],
        ["Class 2 (Lower Risk)", "5 storey single occupancy houses; Flats/offices <= 4 storeys; Industrial <= 3 storeys"],
        ["Class 2 (Upper Risk)", "Hotels, flats, offices 4 to 15 storeys; Educational 2 to 15 storeys; Retail premises <= 15 storeys"],
        ["Class 3", "All buildings exceeding above limits; Grandstands, concert halls, stadiums; High occupancy buildings"]
    ],
    "Recommended categorisation of Consequences Classes",
    "See also Annex A for robustness rules."
)
