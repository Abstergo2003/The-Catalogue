try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Latin upper case letters
A_deb = Symbol(r"A_{deb}", "Area of obstruction (accumulation of debris)")
F_deb = Symbol(r"F_{deb}", "Horizontal forces exerted by accumulation of debris")
F_cb_k = Symbol(r"F_{cb,k}", "Characteristic values of concentrated construction loads Q_cb")
F_hn = Symbol(r"F_{hn}", "Nominal horizontal forces")
F_wa = Symbol(r"F_{wa}", "Horizontal forces due to currents on immersed obstacles")
Q_c = Symbol(r"Q_c", "Construction loads (general symbol)")
Q_ca = Symbol(r"Q_{ca}", "Construction loads due to working personnel, staff and visitors with handtools")
Q_cb = Symbol(r"Q_{cb}", "Construction loads due to storage of moveable items")
Q_cc = Symbol(r"Q_{cc}", "Construction loads due to non-permanent equipment in position for use")
Q_cd = Symbol(r"Q_{cd}", "Construction loads due to moveable heavy machinery and equipment")
Q_ce = Symbol(r"Q_{ce}", "Construction loads from accumulation of waste materials")
Q_cf = Symbol(r"Q_{cf}", "Construction loads from parts of structure in temporary states")
Q_W = Symbol(r"Q_W", "Wind actions during execution")
Q_wa = Symbol(r"Q_{wa}", "Actions caused by water during execution")

# Latin lower case letters
b = Symbol(r"b", "Width of an immersed object")
c_pe = Symbol(r"c_{pe}", "External wind pressure coefficients for free-standing walls")
h = Symbol(r"h", "Water depth")
k = Symbol(r"k", "Shape factor for an immersed object")
p = Symbol(r"p", "Flowing water pressure, which may be current water")
q_ca_k = Symbol(r"q_{ca,k}", "Characteristic value of uniformly distributed load of Q_ca")
q_cb_k = Symbol(r"q_{cb,k}", "Characteristic value of uniformly distributed load of Q_cb")
q_cc_k = Symbol(r"q_{cc,k}", "Characteristic value of uniformly distributed load representing Q_cc")
v_w = Symbol(r"v_w", "Mean speed of water")

# Greek lower case letters
rho_wa = Symbol(r"\rho_{wa}", "Density of water")
