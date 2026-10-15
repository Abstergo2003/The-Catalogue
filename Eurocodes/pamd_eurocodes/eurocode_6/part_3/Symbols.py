try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Section 1.4 Symbols used in EN 1996-3 (Simplified calculation methods for unreinforced masonry)

N_Rd = Symbol(r"N_{Rd}", "Design value of vertical load resistance calculated by simplified method (N_Rd = c_A * f_d * A)")
c_A = Symbol(r"c_A", "Capacity reduction factor allowing for effects of slenderness, eccentricity, and floor spans")
f_d = Symbol(r"f_d", "Design compressive strength of masonry (f_d = f_k / gamma_M)")
A = Symbol(r"A", "Gross cross-sectional area of the wall (A = l * t)")

h = Symbol(r"h", "Clear storey height of the wall")
h_ef = Symbol(r"h_{ef}", "Effective height of the wall in simplified design")
t = Symbol(r"t", "Actual thickness of the wall leaf")
t_ef = Symbol(r"t_{ef}", "Effective thickness of the wall")
l = Symbol(r"l", "Length of the wall in plan")
L_f = Symbol(r"L_f", "Span of the floor slab supported on the wall")

h_b = Symbol(r"h_b", "Depth of earth backfill acting against a basement masonry wall")
p_Ed = Symbol(r"p_{Ed}", "Design lateral earth or wind pressure per unit area")
A_sw = Symbol(r"A_{sw}", "Total cross-sectional area of shear walls in a given orthogonal direction")
A_floor = Symbol(r"A_{floor}", "Gross area of floor supported by the lateral load resisting system")
