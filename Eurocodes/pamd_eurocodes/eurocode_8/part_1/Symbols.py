try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Section 1.6 Symbols used in EN 1998-1 (General rules, seismic actions and rules for buildings)

# Ground motion and seismic action parameters
a_g = Symbol(r"a_g", "Design ground acceleration on type A ground (a_g = gamma_I * a_gR)")
a_gR = Symbol(r"a_{gR}", "Reference peak ground acceleration on type A ground")
a_vg = Symbol(r"a_{vg}", "Design ground acceleration in the vertical direction")
S = Symbol(r"S", "Soil factor accounting for ground type stratigraphic profile")
T_B = Symbol(r"T_B", "Lower limit period of the constant spectral acceleration branch")
T_C = Symbol(r"T_C", "Upper limit period of the constant spectral acceleration branch")
T_D = Symbol(r"T_D", "Beginning period of the constant spectral displacement range")
T_1 = Symbol(r"T_1", "Fundamental period of vibration of the building in the considered direction")
T = Symbol(r"T", "Vibration period of a linear single-degree-of-freedom system")

# Response spectra
S_e = Symbol(r"S_e(T)", "Elastic horizontal response spectrum acceleration")
S_ve = Symbol(r"S_{ve}(T)", "Elastic vertical response spectrum acceleration")
S_d = Symbol(r"S_d(T)", "Design response spectrum acceleration for linear elastic analysis")
eta_damping = Symbol(r"\eta", "Damping correction factor for viscous damping ratio xi (eta = sqrt(10 / (5 + xi)))")
xi_damping = Symbol(r"\xi", "Viscous damping ratio of the structure (typically 5%)")

# Structural behavior and forces
q = Symbol(r"q", "Behavior factor accounting for energy dissipation capacity (q = q_0 * k_w >= 1.5)")
q_0 = Symbol(r"q_0", "Basic value of the behavior factor depending on structural system and ductility class")
k_w = Symbol(r"k_w", "Factor reflecting the prevailing failure mode in structural wall systems")
F_b = Symbol(r"F_b", "Seismic base shear force (F_b = S_d(T_1) * m * lambda)")
gamma_I = Symbol(r"\gamma_I", "Importance factor of the building depending on importance class")
d_g = Symbol(r"d_g", "Design ground displacement (d_g = 0.025 * a_g * S * T_C * T_D)")
d_e = Symbol(r"d_e", "Displacement of a point determined by linear elastic analysis")
d_s = Symbol(r"d_s", "Design displacement of a point induced by design seismic action (d_s = q * d_e)")
d_r = Symbol(r"d_r", "Design interstorey drift (relative lateral displacement between storeys)")
theta_p_delta = Symbol(r"\theta", "Interstorey drift sensitivity coefficient for second-order P-Delta effects")
