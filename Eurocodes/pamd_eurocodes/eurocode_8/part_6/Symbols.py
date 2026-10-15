try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Section 1.6 Symbols used in EN 1998-6 (Towers, masts and chimneys)

# Dynamic and Modal Parameters
M_i = Symbol(r"M_i", "Effective modal mass for the i-th mode of vibration")
R_theta = Symbol(r"R_\theta", "Rotational response spectrum ordinate around coordinate axis (rad/s^2)")
xi_j = Symbol(r"\xi_j", "Equivalent modal damping ratio of the j-th mode")
T_1 = Symbol(r"T_1", "Fundamental natural period of vibration of the tower, mast, or chimney")
S_d = Symbol(r"S_d(T)", "Design response spectrum spectral acceleration at period T")

# Behaviour Factors and Regularity
q = Symbol(r"q", "Design behaviour factor for towers, masts, or chimneys (q = q0 * kr)")
q_0 = Symbol(r"q_0", "Basic behaviour factor reflecting the ductility and energy dissipation of the structural framing")
k_r = Symbol(r"k_r", "Modification factor reflecting departure from regular distribution of mass, stiffness, or strength")
mu_curv = Symbol(r"\mu_{1/r}", "Curvature ductility factor at critical sections of reinforced concrete chimneys")

# Cable and Geometric Parameters
E_eq = Symbol(r"E_{eq}", "Equivalent modulus of elasticity of guy cables accounting for sag and tension")
gamma_I = Symbol(r"\gamma_I", "Importance factor for towers, masts, and industrial chimneys")
