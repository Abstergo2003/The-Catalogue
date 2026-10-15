try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Section 1.6 Symbols used in EN 1993-3 (Towers, Masts and Chimneys)

A_ref = Symbol(r"A_{ref}", "Reference area for aerodynamic force calculation")
B_2 = Symbol(r"B^2", "Background response factor for wind action")
R_2 = Symbol(r"R^2", "Resonant response factor for wind action")
I_v = Symbol(r"I_v", "Turbulence intensity of the wind at height z")
Sc = Symbol(r"Sc", "Scruton number characterizing mass and damping for vortex excitation")
St = Symbol(r"St", "Strouhal number for vortex shedding frequency")
c_d = Symbol(r"c_d", "Dynamic factor for wind response")
c_f = Symbol(r"c_f", "Aerodynamic force coefficient")
q_p = Symbol(r"q_p", "Peak velocity pressure including mean and turbulent velocity fluctuations")
v_m = Symbol(r"v_m", "Mean wind velocity at height z")
delta = Symbol(r"\delta", "Total logarithmic decrement of damping (delta = delta_s + delta_a)")
delta_s = Symbol(r"\delta_s", "Structural damping logarithmic decrement")
delta_a = Symbol(r"\delta_a", "Aerodynamic damping logarithmic decrement")
gamma_M0 = Symbol(r"\gamma_{M0}", "Partial factor for resistance of cross-sections")
gamma_M1 = Symbol(r"\gamma_{M1}", "Partial factor for resistance of members to instability")
gamma_M2 = Symbol(r"\gamma_{M2}", "Partial factor for resistance of cross-sections in tension to fracture")
gamma_Mg = Symbol(r"\gamma_{Mg}", "Partial factor for guy ropes and stay cables")
gamma_Mi = Symbol(r"\gamma_{Mi}", "Partial factor for insulators")
