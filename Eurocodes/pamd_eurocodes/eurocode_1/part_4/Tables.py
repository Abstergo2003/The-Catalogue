try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 2.1
classification_of_design_situations_silos = Table(
    ["Design situation", "Conditions considered"],
    [
        ["Persistent", "Normal operations of filling, storage, and discharge"],
        ["Transient", "Maintenance, inspection, repair, temporary foundation settlement"],
        ["Accidental", "Explosion of combustible dusts, vehicle impact, seismic events, equipment failure"]
    ],
    "Classification of design situations for silos",
    ""
)

# Table 4.1
wall_surface_categories = Table(
    ["Category", "Description", "Examples"],
    [
        ["D1", "State-of-the-art polished or coated surfaces", "Glass, polished stainless steel, ultra-high molecular weight polyethylene"],
        ["D2", "Smooth wall surfaces", "Mild steel plates, aluminium, smooth formwork concrete"],
        ["D3", "Rough wall surfaces", "Corrugated steel, rough concrete, uncoated masonry"],
        ["D4", "Corrugated or profile walls with horizontal ribs", "Corrugated sheeting with corrugations running horizontally"]
    ],
    "Wall surface categories",
    "Used to determine the wall friction coefficient mu."
)

# Table E.1
particulate_solids_properties = Table(
    ["Material", "Unit weight $\\gamma$ [kN/m3]", "Angle of repose $\\phi_r$ [deg]", "Internal friction $\\phi_i$ [deg]", "Lateral pressure ratio $K$", "Wall friction $\\mu$ (Category D2)"],
    [
        ["Cement", 16.0, 28, 30, 0.45, 0.41],
        ["Fly ash", 12.0, 25, 30, 0.45, 0.41],
        ["Wheat", 7.8, 30, 29, 0.54, 0.38],
        ["Barley", 7.0, 30, 31, 0.50, 0.38],
        ["Maize / Corn", 7.4, 30, 31, 0.50, 0.40],
        ["Soya beans", 7.4, 30, 28, 0.55, 0.36],
        ["Sugar (granulated)", 8.5, 35, 32, 0.48, 0.45],
        ["Sand (dry)", 16.0, 35, 36, 0.40, 0.45],
        ["Gravel", 18.0, 35, 36, 0.40, 0.45],
        ["Coal (raw)", 10.0, 35, 35, 0.45, 0.50]
    ],
    "Properties of particulate solids for silo design",
    "Values based on EN 1991-4 Annex E."
)
