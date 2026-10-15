try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Section 1.4 Symbols used in EN 1996-2 (Design considerations, selection of materials and execution)

n_tie = Symbol(r"n_{tie}", "Minimum number of wall ties per square metre of cavity wall")
d_tie = Symbol(r"d_{tie}", "Nominal wire diameter or thickness of a wall tie")
s_h = Symbol(r"s_h", "Horizontal spacing between adjacent wall ties")
s_v = Symbol(r"s_v", "Vertical spacing between adjacent courses of wall ties")

c_nom = Symbol(r"c_{nom}", "Nominal mortar or concrete cover to bed joint reinforcement or embedded ties")
w_cavity = Symbol(r"w_{cavity}", "Width of cavity between leaves in a cavity wall")
t_leaf = Symbol(r"t_{leaf}", "Thickness of a single leaf of masonry")
t_joint = Symbol(r"t_{joint}", "Thickness of mortar bed joint (10-15 mm for general purpose, 1-3 mm for thin layer)")

d_joint = Symbol(r"d_{joint}", "Maximum horizontal spacing between vertical movement joints")
h_pier = Symbol(r"h_{pier}", "Height of isolated masonry pier")
t_pier = Symbol(r"t_{pier}", "Thickness or minimum cross-sectional dimension of isolated pier")
