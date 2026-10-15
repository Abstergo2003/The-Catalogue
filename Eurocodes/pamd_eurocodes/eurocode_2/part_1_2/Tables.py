try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 5.2a
minimum_column_dimensions_and_axis_distances_method_a = Table(
    [
        "Standard fire resistance",
        r"Column exposed on >1 side ($\mu_{fi} = 0.2$)",
        r"Column exposed on >1 side ($\mu_{fi} = 0.5$)",
        r"Column exposed on >1 side ($\mu_{fi} = 0.7$)",
        r"Exposed on 1 side ($\mu_{fi} = 0.7$)"
    ],
    [
        ["R 30", "200/25", "200/25", "200/32 or 300/27", "155/25"],
        ["R 60", "200/25", "200/36 or 300/31", "250/46 or 350/40", "155/25"],
        ["R 90", "200/31 or 300/25", "300/45 or 400/38", "350/53 or 450/40**", "155/25"],
        ["R 120", "250/40 or 350/35", "350/45** or 450/40**", "350/57** or 450/51**", "175/35"],
        ["R 180", "350/45**", "350/63**", "450/70**", "230/55"],
        ["R 240", "350/61**", "450/75**", "-", "295/70"]
    ],
    "Minimum column dimensions and axis distances for columns with rectangular or circular section (Method A)",
    "Format: b_min / a (mm). ** denotes minimum 8 bars. Table based on recommended value alpha_cc = 1.0."
)

# Table 5.3
minimum_wall_thickness_of_non_load_bearing_walls = Table(
    ["Standard fire resistance", "Minimum wall thickness (mm)"],
    [
        ["EI 30", 60],
        ["EI 60", 80],
        ["EI 90", 100],
        ["EI 120", 120],
        ["EI 180", 150],
        ["EI 240", 175]
    ],
    "Minimum wall thickness of non load-bearing walls (partitions)",
    "If calcareous aggregates are used the minimum wall thickness may be reduced by 10%."
)

# Table 5.4
minimum_dimensions_and_axis_distances_for_load_bearing_reinforced_concrete_walls = Table(
    [
        "Standard fire resistance",
        r"Wall exposed on 1 side ($\mu_{fi} = 0.35$)",
        r"Wall exposed on 2 sides ($\mu_{fi} = 0.35$)",
        r"Wall exposed on 1 side ($\mu_{fi} = 0.7$)",
        r"Wall exposed on 2 sides ($\mu_{fi} = 0.7$)"
    ],
    [
        ["REI 30", "100/10*", "120/10*", "120/10*", "120/10*"],
        ["REI 60", "110/10*", "120/10*", "130/10*", "140/10*"],
        ["REI 90", "120/20*", "140/10*", "140/25", "170/25"],
        ["REI 120", "150/25", "160/25", "160/35", "220/35"],
        ["REI 180", "180/40", "200/45", "210/50", "270/55"],
        ["REI 240", "230/55", "250/55", "270/60", "350/60"]
    ],
    "Minimum dimensions and axis distances for load-bearing reinforced concrete walls",
    "* Normally the cover required by EN 1992-1-1 will control. Values given as wall thickness / axis distance (mm)."
)

# Table 5.5
minimum_dimensions_and_axis_distances_for_simply_supported_beams = Table(
    [
        "Standard fire resistance",
        "Combination 1 (bmin/a)",
        "Combination 2 (bmin/a)",
        "Combination 3 (bmin/a)",
        "Combination 4 (bmin/a)",
        "Class WA (bw)",
        "Class WB (bw)",
        "Class WC (bw)"
    ],
    [
        ["R 30", "80/25", "120/20", "160/15*", "200/15*", 80, 80, 80],
        ["R 60", "120/40", "160/35", "200/30", "300/25", 100, 80, 100],
        ["R 90", "150/55", "200/45", "300/40", "400/35", 110, 100, 100],
        ["R 120", "200/65", "240/60", "300/55", "500/50", 130, 120, 120],
        ["R 180", "240/80", "300/70", "400/65", "600/60", 150, 150, 140],
        ["R 240", "280/90", "350/80", "500/75", "700/70", 170, 170, 160]
    ],
    "Minimum dimensions and axis distances for simply supported beams made with reinforced and prestressed concrete",
    "* Normally the cover required by EN 1992-1-1 will control. asd = a + 10 mm."
)

# Table 5.6
minimum_dimensions_and_axis_distances_for_continuous_beams = Table(
    [
        "Standard fire resistance",
        "Combination 1 (bmin/a)",
        "Combination 2 (bmin/a)",
        "Combination 3 (bmin/a)",
        "Combination 4 (bmin/a)",
        "Class WA (bw)",
        "Class WB (bw)",
        "Class WC (bw)"
    ],
    [
        ["R 30", "80/15*", "160/12*", "-", "-", 80, 80, 80],
        ["R 60", "120/25", "200/12*", "-", "-", 100, 80, 100],
        ["R 90", "150/35", "250/25", "-", "-", 110, 100, 100],
        ["R 120", "200/45", "300/35", "450/35", "500/30", 130, 120, 120],
        ["R 180", "240/60", "400/50", "550/50", "600/40", 150, 150, 140],
        ["R 240", "280/75", "500/60", "650/60", "700/50", 170, 170, 160]
    ],
    "Minimum dimensions and axis distances for continuous beams made with reinforced and prestressed concrete",
    "* Normally the cover required by EN 1992-1-1 will control. asd = a + 10 mm."
)

# Table 5.8
minimum_dimensions_and_axis_distances_for_solid_slabs = Table(
    [
        "Standard fire resistance",
        "Slab thickness hs (mm)",
        "One-way slab axis-distance a (mm)",
        r"Two-way slab ($l_y/l_x \le 1.5$) axis-distance a (mm)",
        r"Two-way slab ($1.5 < l_y/l_x \le 2$) axis-distance a (mm)"
    ],
    [
        ["REI 30", 60, "10*", "10*", "10*"],
        ["REI 60", 80, 20, "10*", "15*"],
        ["REI 90", 100, 30, "15*", 20],
        ["REI 120", 120, 40, 20, 25],
        ["REI 180", 150, 55, 30, 40],
        ["REI 240", 175, 65, 40, 50]
    ],
    "Minimum dimensions and axis distances for reinforced and prestressed concrete simply supported one-way and two-way solid slabs",
    "* Normally the cover required by EN 1992-1-1 will control. lx and ly are the spans of a two-way slab (ly is longer span)."
)

# Table 5.9
minimum_dimensions_and_axis_distances_for_solid_flat_slabs = Table(
    ["Standard fire resistance", "Slab thickness hs (mm)", "Axis distance a (mm)"],
    [
        ["REI 30", 150, "10*"],
        ["REI 60", 180, "15*"],
        ["REI 90", 200, 25],
        ["REI 120", 200, 35],
        ["REI 180", 200, 45],
        ["REI 240", 200, 50]
    ],
    "Minimum dimensions and axis distances for reinforced and prestressed concrete solid flat slabs",
    "* Normally the cover required by EN 1992-1-1 will control. The axis distance a denotes the axis distance of the reinforcement in the lower layer."
)
