try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Section 1.4 Symbols used in DD ENV 1996-1-3 (Detailed rules on lateral loading)

q_lat = Symbol(r"q_{lat}", "Design lateral load (wind or horizontal earth pressure) per unit area")
W_Ed = Symbol(r"W_{Ed}", "Design wind pressure action per unit area")
M_Ed1 = Symbol(r"M_{Ed1}", "Design bending moment per unit length about axis parallel to bed joints")
M_Ed2 = Symbol(r"M_{Ed2}", "Design bending moment per unit length about axis perpendicular to bed joints")
M_Rd1 = Symbol(r"M_{Rd1}", "Design moment of resistance about axis parallel to bed joints")
M_Rd2 = Symbol(r"M_{Rd2}", "Design moment of resistance about axis perpendicular to bed joints")

f_xk1 = Symbol(r"f_{xk1}", "Characteristic flexural strength of masonry with failure plane parallel to bed joints")
f_xk2 = Symbol(r"f_{xk2}", "Characteristic flexural strength of masonry with failure plane perpendicular to bed joints")
f_xd1 = Symbol(r"f_{xd1}", "Design flexural strength parallel to bed joints (f_xd1 = f_xk1 / gamma_M)")
f_xd2 = Symbol(r"f_{xd2}", "Design flexural strength perpendicular to bed joints (f_xd2 = f_xk2 / gamma_M)")

mu = Symbol(r"\mu", "Orthogonal ratio of flexural strengths (mu = f_xk1 / f_xk2)")
alpha_bend = Symbol(r"\alpha", "Bending moment coefficient depending on boundary conditions and aspect ratio h/L")
gamma_M = Symbol(r"\gamma_M", "Partial safety factor for masonry material in flexure")

h = Symbol(r"h", "Height of the wall between horizontal supports")
L = Symbol(r"L", "Length of the wall between vertical lateral supports")
t = Symbol(r"t", "Thickness of the wall")
Z = Symbol(r"Z", "Elastic section modulus of the wall per unit length (Z = t^2 / 6)")
