try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Latin upper case letters
K_G = Symbol(r"K_G", "Deflagration index of a gas cloud")
K_St = Symbol(r"K_{St}", "Deflagration index of a dust cloud")
P_max = Symbol(r"p_{max}", "Maximum pressure developed in a contained deflagration")
P_red = Symbol(r"p_{red}", "Reduced pressure developed in vented enclosure during deflagration")
P_stat = Symbol(r"p_{stat}", "Static activation pressure that activates a vent closure")
F_dx = Symbol(r"F_{d,x}", "Horizontal equivalent static design force due to impact in travel direction")
F_dy = Symbol(r"F_{d,y}", "Horizontal equivalent static design force due to impact perpendicular to travel direction")
