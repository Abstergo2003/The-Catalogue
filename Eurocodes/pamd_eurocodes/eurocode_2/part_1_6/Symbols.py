try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Section 1.7 Special symbols used in ENV 1992-1-6

# Latin lower case letters
a_proj = Symbol(r"a", "Projection of a pad footing from the column face")
e_a = Symbol(r"e_a", "Additional eccentricity covering the effects of geometrical imperfections")
e_0 = Symbol(r"e_0", "First order eccentricity")
e_y = Symbol(r"e_y", "Component of eccentricity e in direction of the y-axis")
e_z = Symbol(r"e_z", "Component of eccentricity e in direction of the z-axis")
e_tot = Symbol(r"e_{tot}", "Total eccentricity")
f_ctd = Symbol(r"f_{ctd}", "Design value of the tensile strength of concrete")
h_F = Symbol(r"h_F", "Depth of a pad footing")
h_w = Symbol(r"h_w", "Overall depth (thickness) of a wall")
i_gyr = Symbol(r"i", "Radius of gyration")
l_h = Symbol(r"l_h", "Clear horizontal length of a wall between vertical restraints")
l_ht = Symbol(r"l_{ht}", "Horizontal length of a transverse wall stabilizing the wall under consideration")
l_w = Symbol(r"l_w", "Clear height of a wall")
l_0_plain = Symbol(r"l_0", "Effective length of a plain concrete compression member")

# Greek symbols
alpha_long = Symbol(r"\alpha", "Reduction coefficient to allow for effect of long term loading on concrete compression strength")
beta_plain = Symbol(r"\beta", "Effective height coefficient: beta = l_0 / l_w")
gamma_n = Symbol(r"\gamma_n", "Additional partial safety factor for plain concrete")
lambda_slend = Symbol(r"\lambda", "Slenderness ratio: lambda = l_0 / i")
sigma_cm = Symbol(r"\sigma_{cm}", "Average concrete compressive stress")
tau_Sd = Symbol(r"\tau_{Sd}", "Design value of the applied shear stress")
