try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Section 1.6 Symbols used in DD ENV 1997-3 (Ground investigation and field testing)

# Cone Penetration Test (CPT / CPTU)
q_c = Symbol(r"q_c", "Measured cone tip resistance in CPT")
q_t = Symbol(r"q_t", "Corrected total cone resistance in CPTU (q_t = q_c + u_2 * (1 - a))")
f_s = Symbol(r"f_s", "Sleeve friction measured on the friction sleeve in CPT")
R_f = Symbol(r"R_f", "Friction ratio in CPT (R_f = (f_s / q_c) * 100%)")
u_2 = Symbol(r"u_2", "Pore water pressure measured at the cone shoulder in CPTU")
B_q = Symbol(r"B_q", "Normalized pore pressure parameter in CPTU")

# Standard Penetration Test (SPT)
N_spt = Symbol(r"N", "Measured SPT blow count for 300 mm penetration (excluding initial seating)")
N_60 = Symbol(r"N_{60}", "Energy-corrected SPT blow count to 60% theoretical free-fall energy")
N_1_60 = Symbol(r"(N_1)_{60}", "Overburden-normalized and energy-corrected SPT blow count in sands")

# Pressuremeter Test (PMT)
E_M = Symbol(r"E_M", "Ménard pressuremeter modulus of ground deformation")
p_LM = Symbol(r"p_{LM}", "Ménard limit pressure at which ground fails in cylindrical expansion")
p_0_pmt = Symbol(r"p_0", "In-situ horizontal total at-rest earth pressure from PMT curve")
p_f = Symbol(r"p_f", "Creep pressure threshold on Ménard pressuremeter curve")

# Flat Dilatometer Test (DMT)
I_D = Symbol(r"I_D", "Material index from flat dilatometer test")
E_D = Symbol(r"E_D", "Dilatometer modulus from membrane deflection")
K_D = Symbol(r"K_D", "Horizontal stress index from lift-off pressure")

# Field Vane Test (FVT) and Plate Load Test (PLT)
c_fv = Symbol(r"c_{fv}", "Field vane shear strength of cohesive ground")
mu_v = Symbol(r"\mu_v", "Vane test correction factor based on plasticity index")
k_s = Symbol(r"k_s", "Modulus of subgrade reaction from plate loading test")
