try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Latin upper case letters
L = Symbol(r"L", "Loaded length, or bridge deck span")
Q_1k = Symbol(r"Q_{1k}", "Characteristic axle load of Tandem System (Lane 1, LM1)")
Q_2k = Symbol(r"Q_{2k}", "Characteristic axle load of Tandem System (Lane 2, LM1)")
Q_3k = Symbol(r"Q_{3k}", "Characteristic axle load of Tandem System (Lane 3, LM1)")
Q_tk = Symbol(r"Q_{tk}", "Characteristic centrifugal force on road bridges")
Q_lk = Symbol(r"Q_{lk}", "Characteristic braking or acceleration force on road bridges")
Q_la = Symbol(r"Q_{la}", "Characteristic traction (acceleration) force on railway bridges")
Q_lb = Symbol(r"Q_{lb}", "Characteristic braking force on railway bridges")
Q_s = Symbol(r"Q_s", "Nosing force on railway bridges")
Q_v = Symbol(r"Q_v", "Vertical axle load for railway traffic")
V = Symbol(r"V", "Speed in km/h")

# Latin lower case letters
q_1k = Symbol(r"q_{1k}", "Characteristic uniformly distributed load (Lane 1, LM1)")
q_2k = Symbol(r"q_{2k}", "Characteristic uniformly distributed load (Lane 2, LM1)")
q_3k = Symbol(r"q_{3k}", "Characteristic uniformly distributed load (Lane 3, LM1)")
q_rk = Symbol(r"q_{rk}", "Characteristic uniformly distributed load on remaining area of carriageway")
q_fk = Symbol(r"q_{fk}", "Characteristic load on footpaths and cycle tracks")
q_vk = Symbol(r"q_{vk}", "Vertical distributed load for rail traffic (LM71, SW/0)")
w = Symbol(r"w", "Carriageway width for a road bridge")
w_l = Symbol(r"w_l", "Width of a notional lane for a road bridge (typically 3.0 m)")
v = Symbol(r"v", "Speed in m/s")

# Greek letters
alpha = Symbol(r"\alpha", "Load classification factor for railway traffic")
Phi = Symbol(r"\Phi", "Dynamic factor for railway Load Models 71, SW/0 and SW/2")
Phi_2 = Symbol(r"\Phi_2", "Dynamic factor for carefully maintained track")
Phi_3 = Symbol(r"\Phi_3", "Dynamic factor for standard track maintenance")
