try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Section 1.6 Symbols used in EN 1997-2 (Ground investigation and laboratory testing)

# Soil index and physical properties
w = Symbol(r"w", "Water content (moisture content) of soil expressed as ratio or percentage")
w_L = Symbol(r"w_L", "Liquid limit of fine-grained soil")
w_P = Symbol(r"w_P", "Plastic limit of fine-grained soil")
I_P = Symbol(r"I_P", "Plasticity index (I_P = w_L - w_P)")
I_C = Symbol(r"I_C", "Consistency index (I_C = (w_L - w) / I_P)")
I_L = Symbol(r"I_L", "Liquidity index (I_L = (w - w_P) / I_P)")

e = Symbol(r"e", "Void ratio (ratio of volume of voids to volume of solids)")
n_porosity = Symbol(r"n", "Porosity (ratio of volume of voids to total volume)")
S_r = Symbol(r"S_r", "Degree of saturation (ratio of volume of water to volume of voids)")

rho_bulk = Symbol(r"\rho", "Bulk density (total mass per unit volume)")
rho_d = Symbol(r"\rho_d", "Dry density (mass of solids per unit volume)")
rho_s = Symbol(r"\rho_s", "Particle density (density of solid mineral grains)")

# Mechanical and compressibility parameters from lab testing
c_prime = Symbol(r"c'", "Effective cohesion intercept from drained triaxial or shear box test")
phi_prime = Symbol(r"\phi'", "Angle of shearing resistance in terms of effective stress from lab tests")
c_u = Symbol(r"c_u", "Undrained shear strength from undrained triaxial compression or vane test")

E_oed = Symbol(r"E_{oed}", "Oedometer modulus of deformation in one-dimensional consolidation")
C_c = Symbol(r"C_c", "Compression index from oedometer e - log sigma' curve")
C_s = Symbol(r"C_s", "Swelling or recompression index from oedometer test")
c_v = Symbol(r"c_v", "Coefficient of consolidation (m2/s)")
k_perm = Symbol(r"k", "Coefficient of permeability / hydraulic conductivity (m/s)")
q_u = Symbol(r"q_u", "Unconfined compressive strength from unconfined compression test")
