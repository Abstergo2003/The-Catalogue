try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Section 1.6 Symbols used in EN 1998-2 (Bridges)

q_bridge = Symbol(r"q", "Behavior factor for seismic design of bridge piers")
gamma_I_bridge = Symbol(r"\gamma_I", "Importance factor for bridges (Class I: 0.8, Class II: 1.0, Class III: 1.3)")
d_Ed = Symbol(r"d_{Ed}", "Design seismic displacement of the bridge superstructure")
d_eg = Symbol(r"d_{eg}", "Effective displacement difference between adjacent bridge segments or supports")
L_ov = Symbol(r"L_{ov}", "Minimum overlap length of bridge deck on support seat to prevent unseating")

mu_d = Symbol(r"\mu_d", "Target displacement ductility factor for bridge piers")
T_eff = Symbol(r"T_{eff}", "Effective vibration period of base-isolated bridge superstructure")
K_eff = Symbol(r"K_{eff}", "Effective horizontal stiffness of seismic isolation bearings")
xi_eff = Symbol(r"\xi_{eff}", "Effective equivalent viscous damping ratio of the isolation system")
F_res = Symbol(r"F_{res}", "Residual restoring force of seismic isolation bearings")
