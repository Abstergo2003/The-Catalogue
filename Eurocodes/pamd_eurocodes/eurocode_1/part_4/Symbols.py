try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Latin upper case letters
A = Symbol(r"A", "Plan cross-sectional area of vertical walled segment")
A_c = Symbol(r"A_c", "Plan cross-sectional area of flow channel during eccentric discharge")
C = Symbol(r"C", "Load magnifying factor")
C_o = Symbol(r"C_o", "Discharge factor (load magnifying factor) for the solid")
C_op = Symbol(r"C_{op}", "Patch load solid reference factor")
K = Symbol(r"K", "Lateral pressure ratio (ratio of horizontal to vertical stress)")
K_o = Symbol(r"K_o", "Value of K measured for zero horizontal strain")
S = Symbol(r"S", "Hopper geometry factor (= 2 for conical, = 1 for wedge)")
U = Symbol(r"U", "Internal perimeter of the plan cross-section")
Y_J = Symbol(r"Y_J", "Janssen pressure depth variation function")
Y_R = Symbol(r"Y_R", "Squat silo pressure depth variation function")

# Latin lower case letters
d_c = Symbol(r"d_c", "Characteristic dimension of inside of silo cross-section")
e_f = Symbol(r"e_f", "Eccentricity of filling")
e_d = Symbol(r"e_d", "Eccentricity of discharge")
h_b = Symbol(r"h_b", "Overall height of silo from hopper apex to equivalent surface")
h_c = Symbol(r"h_c", "Height of vertical-walled segment of silo")
h_h = Symbol(r"h_h", "Height of hopper from apex to transition")
p_h = Symbol(r"p_h", "Horizontal pressure on vertical silo wall")
p_hf = Symbol(r"p_{hf}", "Horizontal pressure after filling")
p_he = Symbol(r"p_{he}", "Horizontal pressure during discharge")
p_v = Symbol(r"p_v", "Mean vertical stress in stored solid")
p_vf = Symbol(r"p_{vf}", "Mean vertical stress after filling")
p_w = Symbol(r"p_w", "Wall frictional traction")
p_wf = Symbol(r"p_{wf}", "Wall frictional traction after filling")
p_we = Symbol(r"p_{we}", "Wall frictional traction during discharge")
p_p = Symbol(r"p_p", "Patch load pressure")
p_n = Symbol(r"p_n", "Normal pressure on hopper wall")
z = Symbol(r"z", "Depth below equivalent surface of the solid")
z_o = Symbol(r"z_o", "Janssen characteristic depth (z_o = A / (mu * K * U))")

# Greek lower case letters
beta = Symbol(r"\beta", "Hopper inclination angle to the horizontal")
gamma = Symbol(r"\gamma", "Unit weight of stored particulate solid")
mu = Symbol(r"\mu", "Wall friction coefficient (mu = tan(phi_w))")
phi_i = Symbol(r"\phi_i", "Angle of internal friction of particulate solid")
phi_r = Symbol(r"\phi_r", "Angle of repose of particulate solid")
phi_w = Symbol(r"\phi_w", "Wall friction angle")
