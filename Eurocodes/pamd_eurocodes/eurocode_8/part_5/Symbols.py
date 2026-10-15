try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Section 1.6 Symbols used in EN 1998-5 (Foundations, retaining structures and geotechnical aspects)

# Seismic action and coefficients
alpha = Symbol(r"\alpha", "Ratio of the design ground acceleration on type A ground ag to the acceleration of gravity g")
k_h = Symbol(r"k_h", "Horizontal seismic coefficient used in pseudo-static geotechnical analysis (k_h = alpha * S / r)")
k_v = Symbol(r"k_v", "Vertical seismic coefficient used in pseudo-static geotechnical analysis (typically +/- 0.5 * k_h)")
r = Symbol(r"r", "Retaining structure displacement/flexibility factor used for the calculation of k_h")
S = Symbol(r"S", "Soil factor accounting for ground type stratigraphic profile")
S_T = Symbol(r"S_T", "Topographic amplification factor for structures located on or near slopes and ridge crests")

# Geotechnical and Dynamic Soil Properties
v_s = Symbol(r"v_s", "Velocity of shear wave propagation in soil layer")
v_s_max = Symbol(r"v_{s,max}", "Average shear wave velocity at small shear strain (< 10^-5)")
G_max = Symbol(r"G_{max}", "Average shear modulus of soil at small strain")
N_1_60 = Symbol(r"N_{1(60)}", "SPT blow count normalized for effective overburden pressure and 60% energy ratio")
N_SPT = Symbol(r"N_{SPT}", "Measured Standard Penetration Test blow count")
c_u = Symbol(r"c_u", "Undrained shear strength of cohesive soil")
phi_prime = Symbol(r"\phi'", "Angle of shearing resistance of soil in terms of effective stress")
delta = Symbol(r"\delta", "Angle of shearing friction resistance between ground and footing or retaining wall")

# Earth Pressures and Foundation Actions
E_d = Symbol(r"E_d", "Design seismic action effect on the foundation or retaining wall")
E_pd = Symbol(r"E_{pd}", "Lateral design resistance due to passive earth pressure on footing or wall")
K = Symbol(r"K", "Total (static + dynamic) earth pressure coefficient evaluated by Mononobe-Okabe method")
gamma_M = Symbol(r"\gamma_M", "Partial factor for soil material properties in seismic design situations (gamma_M = 1.0)")
gamma_Rd = Symbol(r"\gamma_{Rd}", "Model partial factor for seismic bearing capacity of foundations")
