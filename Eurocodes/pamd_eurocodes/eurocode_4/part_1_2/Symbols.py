try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Section 1.6 Symbols used in EN 1994-1-2 (Structural fire design)

theta = Symbol(r"\theta", "Temperature (in degrees Celsius)")
theta_a = Symbol(r"\theta_a", "Temperature of structural steel components")
theta_c = Symbol(r"\theta_c", "Temperature of concrete")
theta_s = Symbol(r"\theta_s", "Temperature of reinforcing steel")
theta_cr = Symbol(r"\theta_{cr}", "Critical temperature of a composite steel element")

k_c_theta = Symbol(r"k_{c,\theta}", "Reduction factor for cylinder compressive strength of concrete at elevated temperature theta")
k_y_theta = Symbol(r"k_{y,\theta}", "Reduction factor for yield strength of structural steel at elevated temperature theta")
k_s_theta = Symbol(r"k_{s,\theta}", "Reduction factor for yield strength of reinforcing steel at elevated temperature theta")
k_E_theta = Symbol(r"k_{E,\theta}", "Reduction factor for modulus of elasticity of structural steel at elevated temperature theta")

eta_fi = Symbol(r"\eta_{fi}", "Reduction factor for design load level in the fire situation")
gamma_M_fi = Symbol(r"\gamma_{M,fi}", "Partial factor for a material property in the fire situation (gamma_M,fi = 1.0)")

R_fi_d = Symbol(r"R_{fi,d}", "Design value of resistance of the composite member in the fire situation")
E_fi_d = Symbol(r"E_{fi,d}", "Design value of effect of actions in the fire situation")

h_eff = Symbol(r"h_{eff}", "Effective slab thickness of composite slab with profiled steel sheeting")
u = Symbol(r"u", "Axis distance of reinforcing bars or steel components to the nearest exposed surface")
u_s = Symbol(r"u_s", "Axis distance of longitudinal reinforcing bars to the nearest exposed surface")
b_c = Symbol(r"b_c", "Width of concrete encasement or concrete-filled section")
