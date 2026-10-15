try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 4.1
number_and_width_of_notional_lanes = Table(
    ["Carriageway width $w$", "Number of notional lanes $n_l$", "Width of a notional lane $w_l$ [m]", "Width of remaining area"],
    [
        ["$w < 5.4$ m", 1, 3.0, "$w - 3.0$ m"],
        ["$5.4 \\le w < 6.0$ m", 2, "$w / 2$", 0],
        ["$w \\ge 6.0$ m", "int($w / 3$)", 3.0, "$w - 3 \\times n_l$ m"]
    ],
    "Number and width of notional lanes",
    "Rules for defining notional lanes across the carriageway."
)

# Table 4.2
load_model_1_characteristic_values = Table(
    ["Location", "Tandem System (TS) Axle loads $Q_{ik}$ [kN]", "UDL system $q_{ik}$ [kN/m2]"],
    [
        ["Lane Number 1", 300, 9.0],
        ["Lane Number 2", 200, 2.5],
        ["Lane Number 3", 100, 2.5],
        ["Other lanes", 0, 2.5],
        ["Remaining area ($q_{rk}$)", 0, 2.5]
    ],
    "Load Model 1 (LM1) : characteristic values",
    "Each tandem consists of two axles, each of load alpha_Q * Q_ik with axle spacing 1.2 m."
)

# Table 4.3
characteristic_values_of_centrifugal_forces = Table(
    ["Curve radius $r$ [m]", "Centrifugal force $Q_{tk}$ [kN]"],
    [
        ["$r < 200$ m", "0.2 * Q_v"],
        ["$200 \\le r \\le 1500$ m", "40 * Q_v / r"],
        ["$r > 1500$ m", 0]
    ],
    "Characteristic values of centrifugal forces on road bridges",
    "Qv is total vertical weight of Load Model 1 tandems on the bridge."
)

# Table 6.1
railway_load_model_71_and_sw0 = Table(
    ["Load Model", "Point loads [kN]", "Distributed load $q_{vk}$ [kN/m]"],
    [
        ["Load Model 71", "4 x 250 kN (spaced at 1.6 m)", 80.0],
        ["Load Model SW/0", "-", 133.0],
        ["Load Model SW/2", "-", 150.0]
    ],
    "Characteristic values for vertical loads for Load Models 71, SW/0 and SW/2",
    "Point loads and distributed loads are multiplied by the classification factor alpha."
)
