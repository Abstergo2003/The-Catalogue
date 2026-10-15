try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 6.1
categories_of_use = Table(
    ["Category", "Specific Use", "Example"],
    [
        ["A", "Areas for domestic and residential activities", "Rooms in residential buildings and houses; bedrooms and wards in hospitals; bedrooms in hotels and hostels; kitchens and toilets."],
        ["B", "Office areas", "Office areas"],
        ["C", "Areas where people may congregate (with the exception of areas defined under category A, B, and D)", "C1: Areas with tables, etc. (e.g. schools, cafes, restaurants, dining halls, reading rooms, receptions)\nC2: Areas with fixed seats (e.g. churches, theatres, cinemas, conference rooms, lecture halls, assembly halls)\nC3: Areas without obstacles for moving people (e.g. museums, exhibition rooms, access areas in public/admin buildings, hotels, hospitals)\nC4: Areas with possible physical activities (e.g. dance halls, gymnastic rooms, stages)\nC5: Areas susceptible to large crowds (e.g. buildings for public events, concert halls, sports halls including stands, terraces and railway platforms)"],
        ["D", "Shopping areas", "D1: Areas in general retail shops\nD2: Areas in department stores"]
    ],
    "Categories of use",
    "NOTE 1 Depending on their anticipated uses, areas likely to be categorised as C2, C3, C4 may be categorised as C5 by decision of the client and/or National annex.\nNOTE 2 The National annex may provide sub categories to A, B, C1 to C5, D1 and D2.\nNOTE 3 See 6.3.2 for storage or industrial activity."
)

# Table 6.2
imposed_loads_on_floors_balconies_and_stairs_in_buildings = Table(
    ["Categories of loaded areas", "$q_k$ [kN/m2]", "$Q_k$ [kN]"],
    [
        ["Category A - Floors", BRange(1.5, 2.0, 2.0), BRange(2.0, 3.0, 2.0)],
        ["Category A - Stairs", BRange(2.0, 4.0, 3.0), BRange(2.0, 4.0, 2.0)],
        ["Category A - Balconies", BRange(2.5, 4.0, 4.0), BRange(2.0, 3.0, 2.0)],
        ["Category B", BRange(2.0, 3.0, 3.0), BRange(1.5, 4.5, 4.5)],
        ["Category C - C1", BRange(2.0, 3.0, 3.0), BRange(3.0, 4.0, 4.0)],
        ["Category C - C2", BRange(3.0, 4.0, 4.0), BRange(2.5, 7.0, 4.0)],
        ["Category C - C3", BRange(3.0, 5.0, 5.0), BRange(4.0, 7.0, 4.0)],
        ["Category C - C4", BRange(4.5, 5.0, 5.0), BRange(3.5, 7.0, 7.0)],
        ["Category C - C5", BRange(5.0, 7.5, 5.0), BRange(3.5, 4.5, 4.5)],
        ["Category D - D1", BRange(4.0, 5.0, 5.0), BRange(3.5, 7.0, 4.0)],
        ["Category D - D2", BRange(4.0, 5.0, 5.0), BRange(3.5, 7.0, 7.0)]
    ],
    "Imposed loads on floors, balconies and stairs in buildings",
    "NOTE Values for qk and Qk are given where a range is given in this table, the value may be set by the National annex. The recommended values are underlined."
)

# Table 6.3
categories_of_storage_and_industrial_use = Table(
    ["Category", "Specific use", "Example"],
    [
        ["E1", "Areas susceptible to accumulation of goods, including access areas", "Areas for storage use including storage of books and other documents."],
        ["E2", "Industrial use", "Industrial use"]
    ],
    "Categories of storage and industrial use",
    ""
)

# Table 6.4
imposed_loads_on_floors_due_to_storage = Table(
    ["Categories of loaded areas", "$q_k$ [kN/m2]", "$Q_k$ [kN]"],
    [
        ["Category E1", 7.5, 7.0]
    ],
    "Imposed loads on floors due to storage",
    "NOTE Recommended values for qk and Qk are given. The values may be changed if necessary according to the usage for the particular project or by the National annex."
)

# Table 6.5
dimensions_of_forklift_according_to_classes_FL = Table(
    ["Class of Forklift", "Net weight [kN]", "Hoisting load [kN]", "Width of axle a [m]", "Overall width b [m]", "Overall length l [m]"],
    [
        ["FL 1", 21, 10, 0.85, 1.00, 2.60],
        ["FL 2", 31, 15, 0.95, 1.10, 3.00],
        ["FL 3", 44, 25, 1.00, 1.20, 3.30],
        ["FL 4", 60, 40, 1.20, 1.40, 4.00],
        ["FL 5", 90, 60, 1.50, 1.90, 4.60],
        ["FL 6", 110, 80, 1.80, 2.30, 5.10]
    ],
    "Dimensions of forklift according to classes FL",
    ""
)

# Table 6.6
axle_loads_of_forklifts = Table(
    ["Class of forklifts", "Axle load $Q_k$ [kN]"],
    [
        ["FL 1", 26],
        ["FL 2", 40],
        ["FL 3", 63],
        ["FL 4", 90],
        ["FL 5", 140],
        ["FL 6", 170]
    ],
    "Axle loads of forklifts",
    ""
)

# Table 6.7
traffic_and_parking_areas_in_buildings = Table(
    ["Categories of traffic areas", "Specific Use", "Examples"],
    [
        ["F", "Traffic and parking areas for light vehicles (<= 30 kN gross vehicle weight and <= 8 seats not including driver)", "garages; parking areas, parking halls"],
        ["G", "Traffic and parking areas for medium vehicles (> 30 kN, <= 160 kN gross vehicle weight, on 2 axles)", "access routes; delivery zones; zones accessible to fire engines (<= 160 kN gross vehicle weight)"]
    ],
    "Traffic and parking areas in buildings",
    "NOTE 1 Access to areas designed to category F should be limited by physical means built into the structure.\nNOTE 2 Areas designed to categories F and G should be posted with the appropriate warning signs."
)

# Table 6.8
imposed_loads_on_garages_and_vehicle_traffic_areas = Table(
    ["Categories of traffic areas", "$q_k$ [kN/m2]", "$Q_k$ [kN]"],
    [
        ["Category F (Gross vehicle weight <= 30 kN)", BRange(1.5, 2.5, 2.0), BRange(10.0, 20.0, 20.0)],
        ["Category G (30 kN < gross vehicle weight <= 160 kN)", 5.0, BRange(40.0, 90.0, 90.0)]
    ],
    "Imposed loads on garages and vehicle traffic areas",
    "NOTE 1 For category F, qk may be selected within the range 1.5 to 2.5 kN/m2 and Qk within 10 to 20 kN.\nNOTE 2 For category G, Qk may be selected within the range 40 to 90 kN.\nNOTE 3 Recommended values are underlined."
)

# Table 6.9
categorization_of_roofs = Table(
    ["Categories of loaded area", "Specific Use"],
    [
        ["H", "Roofs not accessible except for normal maintenance and repair."],
        ["I", "Roofs accessible with occupancy according to categories A to D."],
        ["K", "Roofs accessible for special services, such as helicopter landing areas."]
    ],
    "Categorization of roofs",
    ""
)

# Table 6.10
imposed_loads_on_roofs_of_category_H = Table(
    ["Roof", "$q_k$ [kN/m2]", "$Q_k$ [kN]"],
    [
        ["Category H", BRange(0.0, 1.0, 0.4), BRange(0.9, 1.5, 1.0)]
    ],
    "Imposed loads on roofs of category H",
    "NOTE 1 For category H qk may be selected within 0.00 to 1.0 kN/m2 and Qk within 0.9 to 1.5 kN. Recommended values: qk = 0.4 kN/m2, Qk = 1.0 kN.\nNOTE 2 qk may be varied by the National Annex dependent upon roof slope."
)

# Table 6.11
imposed_loads_on_roofs_of_category_K_for_helicopters = Table(
    ["Class of Helicopter", "Take-off load Q of helicopter", "Take-off load $Q_k$", "Dimension of the loaded area (m x m)"],
    [
        ["HC1", "Q <= 20 kN", "20 kN", "0.2 x 0.2"],
        ["HC2", "20 kN < Q <= 60 kN", "60 kN", "0.3 x 0.3"]
    ],
    "Imposed loads on roofs of category K for helicopters",
    "Dynamic factor phi = 1.40 applies to take-off load Qk to take account of impact effects."
)

# Table 6.12
horizontal_loads_on_partition_walls_and_parapets = Table(
    ["Loaded areas", "$q_k$ [kN/m]"],
    [
        ["Category A", BRange(0.2, 1.0, 0.5)],
        ["Category B and C1", BRange(0.2, 1.0, 0.5)],
        ["Categories C2 to C4 and D", BRange(0.8, 1.0, 1.0)],
        ["Category C5", BRange(3.0, 5.0, 5.0)],
        ["Category E", BRange(0.8, 2.0, 1.0)],
        ["Category F", "See Annex B"],
        ["Category G", "See Annex B"]
    ],
    "Horizontal loads on partition walls and parapets",
    "NOTE 1 For categories A, B and C1, qk may be selected within 0.2 to 1.0 (0.5 kN/m).\nNOTE 2 For categories C2 to C4 and D, qk may be selected within 0.8 to 1.0 kN/m.\nNOTE 3 For category C5, qk may be selected within 3.0 to 5.0 kN/m.\nNOTE 4 For category E, qk may be selected within 0.8 to 2.0 kN/m."
)

# Table A.1
construction_materials_concrete_and_mortar = Table(
    ["Materials", "Density $\\gamma$ [kN/m3]"],
    [
        ["concrete: lightweight (density class LC 1.0)", "9.0 to 10.0"],
        ["concrete: lightweight (density class LC 1.2)", "10.0 to 12.0"],
        ["concrete: lightweight (density class LC 1.4)", "12.0 to 14.0"],
        ["concrete: lightweight (density class LC 1.6)", "14.0 to 16.0"],
        ["concrete: lightweight (density class LC 1.8)", "16.0 to 18.0"],
        ["concrete: lightweight (density class LC 2.0)", "18.0 to 20.0"],
        ["concrete: normal weight", 24.0],
        ["concrete: normal weight (with unhardened concrete +1 kN/m3)", 24.0],
        ["concrete: reinforced / prestressed", 25.0],
        ["mortar: cement mortar", "19.0 to 23.0"],
        ["mortar: lime-cement mortar", "18.0 to 20.0"],
        ["mortar: lime mortar", "12.0 to 18.0"],
        ["mortar: gypsum mortar", "12.0 to 18.0"]
    ],
    "Construction materials - concrete and mortar",
    "Increase by 1 kN/m3 for normal percentage of reinforcing and prestressing steel."
)

# Table A.2
construction_materials_masonry = Table(
    ["Materials", "Density $\\gamma$ [kN/m3]"],
    [
        ["masonry units: clay units", "10.0 to 24.0"],
        ["masonry units: calcium silicate units", "12.0 to 22.0"],
        ["masonry units: aggregate concrete units", "12.0 to 24.0"],
        ["masonry units: autoclaved aerated concrete units", "4.0 to 10.0"],
        ["masonry units: manufactured stone units", "18.0 to 24.0"],
        ["masonry units: glass blocks, hollow", 10.0],
        ["natural stones: granite, syenite, porphyry", "27.0 to 30.0"],
        ["natural stones: basalt, diorite, gabbro", "27.0 to 31.0"],
        ["natural stones: dense limestone", "20.0 to 29.0"],
        ["natural stones: other limestone", "20.0 to 24.0"],
        ["natural stones: sandstone", "21.0 to 27.0"]
    ],
    "Construction materials - masonry",
    "See prEN 771 for unit definitions."
)

# Table A.3
construction_materials_wood = Table(
    ["Materials", "Density $\\gamma$ [kN/m3]"],
    [
        ["timber (strength classes C14 to C40)", "3.5 to 5.0"],
        ["hardwood (strength classes D30 to D70)", "6.0 to 11.0"],
        ["glued laminated timber (homogenous glulam GL24h to GL36h)", "3.8 to 4.5"],
        ["plywood", "5.0 to 8.0"],
        ["particle boards: chipboard", "7.0 to 8.0"],
        ["fibreboards: hardboard, medium board", "8.0 to 10.0"],
        ["fibreboards: softboard, insulating board", "2.5 to 4.0"]
    ],
    "Construction materials - wood",
    "See EN 338 for timber strength classes."
)

# Table A.4
construction_materials_metals = Table(
    ["Materials", "Density $\\gamma$ [kN/m3]"],
    [
        ["aluminium", 27.0],
        ["brass", "83.0 to 87.0"],
        ["bronze", "83.0 to 89.0"],
        ["copper", "87.0 to 89.0"],
        ["cast iron", "71.0 to 72.5"],
        ["wrought iron", 76.0],
        ["lead", "112.0 to 114.0"],
        ["steel", "77.0 to 78.5"],
        ["zinc", "71.0 to 72.0"]
    ],
    "Construction materials - metals",
    ""
)

# Table A.5
construction_materials_other_materials = Table(
    ["Materials", "Density $\\gamma$ [kN/m3]"],
    [
        ["glass, in sheets", 25.0],
        ["plastics: acrylic sheet", 12.0],
        ["plastics: polystyrene, expanded", 0.3],
        ["plasterboard", 9.0],
        ["asphalt, mastic", "22.0 to 24.0"],
        ["bitumen, pure", 10.5]
    ],
    "Construction materials - other materials",
    ""
)

# Table A.6
bridge_materials = Table(
    ["Bridge materials", "Density $\\gamma$ [kN/m3] or Weight [kN/m]"],
    [
        ["paving: asphalt, mastic", "22.0 to 24.0 kN/m3"],
        ["paving: asphalt concrete", "24.0 kN/m3"],
        ["fill: ballast (gravel, crushed rock)", "15.0 to 20.0 kN/m3"],
        ["track with ballasted bed: 2 rails UIC 60", "1.2 kN/m"],
        ["track with ballasted bed: prestressed concrete sleeper with fastenings", "4.8 kN/m"],
        ["track with ballasted bed: timber sleepers with fastenings", "1.9 kN/m"],
        ["track without ballasted bed: 2 rails UIC 60 with fastenings", "1.7 kN/m"],
        ["track without ballasted bed: 2 rails UIC 60 with bridge beam and guard rails", "4.9 kN/m"]
    ],
    "Bridge materials",
    "Values for railway track and bridge surfacing."
)

# Table A.7
stored_materials_building_and_construction = Table(
    ["Materials", "Density $\\gamma$ [kN/m3]", "Angle of repose $\\phi$ [deg]"],
    [
        ["aggregates: lightweight", "9.0 to 20.0", 30],
        ["aggregates: normal", "20.0 to 30.0", 30],
        ["aggregates: heavyweight", "> 30.0", 30],
        ["gravel and sand, bulked", "15.0 to 20.0", 35],
        ["sand", "14.0 to 19.0", 30],
        ["blast furnace slag: lumps", 17.0, 40],
        ["blast furnace slag: granules", 12.0, 30],
        ["blast furnace slag: crushed foamed", 9.0, 35],
        ["brick sand, crushed brick", 15.0, 35],
        ["cement: in bulk", 16.0, 28],
        ["cement: in bag", 15.0, "-"],
        ["fly ash", "10.0 to 14.0", 25],
        ["gypsum, ground", 15.0, 25],
        ["lime", 13.0, 25],
        ["limestone, powder", 13.0, "25 to 27"],
        ["water, fresh", 10.0, "-"]
    ],
    "Stored materials - building and construction",
    ""
)

# Table A.8
stored_products_agricultural = Table(
    ["Products", "Density $\\gamma$ [kN/m3]", "Angle of repose $\\phi$ [deg]"],
    [
        ["farmyard manure (min 60% solids)", 7.8, "-"],
        ["farmyard manure (with dry straw)", 9.3, 45],
        ["slurry (max 20% solids)", 10.8, "-"],
        ["fertiliser, artificial (NPK granulated)", "8.0 to 12.0", 25],
        ["grain: barley", 7.0, 30],
        ["grain: oats", 5.0, 30],
        ["grain: wheat in bulk", 7.8, 30],
        ["grain: maize in bulk", 7.4, 30],
        ["hay (baled)", "1.0 to 3.0", "-"],
        ["silage", "5.0 to 10.0", "-"],
        ["straw in bulk (dry)", 0.7, "-"]
    ],
    "Stored products - agricultural",
    ""
)

# Table A.9
stored_products_foodstuffs = Table(
    ["Products", "Density $\\gamma$ [kN/m3]", "Angle of repose $\\phi$ [deg]"],
    [
        ["flour: bulk", 6.0, 25],
        ["flour: bagged", 5.0, "-"],
        ["sugar: loose, piled", "7.5 to 10.0", 35],
        ["potatoes: in bulk", 7.6, 35],
        ["sugarbeet: raw", 7.6, 35]
    ],
    "Stored products - foodstuffs",
    ""
)

# Table A.10
stored_products_liquids = Table(
    ["Products", "Density $\\gamma$ [kN/m3]"],
    [
        ["beer", 10.0],
        ["milk", 10.0],
        ["water, fresh", 10.0],
        ["wine", 10.0],
        ["alcohol", 7.8],
        ["diesel", 8.3],
        ["fuel oil", "7.8 to 9.8"],
        ["petrol (gasoline)", 7.4],
        ["liquid gas: butane", 5.7],
        ["liquid gas: propane", 5.0]
    ],
    "Stored products - liquids",
    ""
)

# Table A.11
stored_products_solid_fuels = Table(
    ["Products", "Density $\\gamma$ [kN/m3]", "Angle of repose $\\phi$ [deg]"],
    [
        ["charcoal: air-filled", 4.0, "-"],
        ["coal: raw from pit", 10.0, 35],
        ["coal: dust", 7.0, 25],
        ["coke", "4.0 to 6.5", "35 to 45"],
        ["firewood", 5.4, 45],
        ["lignite/brown coal: briquettes tipped", 7.8, 30],
        ["peat: black, dried loosely tipped", "3.0 to 6.0", 45]
    ],
    "Stored products - solid fuels",
    ""
)

# Table A.12
stored_products_industrial_and_general = Table(
    ["Products", "Density $\\gamma$ [kN/m3]", "Angle of repose $\\phi$ [deg]"],
    [
        ["books and documents", 6.0, "-"],
        ["books and documents, densely stored", 8.5, "-"],
        ["filing racks and cabinets", 6.0, "-"],
        ["paper: in rolls", 15.0, "-"],
        ["paper: piled", 11.0, "-"],
        ["rubber", "10.0 to 17.0", "-"],
        ["rock salt", 22.0, 45],
        ["salt", 12.0, 40],
        ["sawdust: dry, loose", 2.5, 45],
        ["tar, bitumen", 14.0, "-"]
    ],
    "Stored products - industrial and general",
    ""
)
