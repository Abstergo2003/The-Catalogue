try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Section 1.6 Symbols used in EN 1998-4 (Silos, tanks and pipelines)

# Hydrodynamic & Silo Pressure Symbols
p_i = Symbol(r"p_i", "Impulsive hydrodynamic pressure component acting on the tank or silo wall in unison with ground acceleration")
p_c = Symbol(r"p_c", "Convective hydrodynamic pressure component associated with liquid sloshing vibrations")
m_i = Symbol(r"m_i", "Equivalent impulsive liquid mass participating in the rigid/flexible body mode of the tank")
m_c = Symbol(r"m_c", "Equivalent convective (sloshing) liquid mass participating in the fundamental free surface wave mode")
T_i = Symbol(r"T_i", "Fundamental period of vibration of the impulsive mode of the tank-liquid system")
T_c = Symbol(r"T_c", "Fundamental period of vibration of the convective (sloshing) mode of the liquid")
d_max = Symbol(r"d_{max}", "Maximum peak vertical free surface sloshing wave height in a tank under earthquake action")

# Shell & Structural Parameters
R = Symbol(r"R", "Radius of a circular cylindrical tank, silo, or pipeline")
H = Symbol(r"H", "Total height or depth of the stored particulate solid or liquid at maximum filling level")
t = Symbol(r"t", "Wall thickness of the silo, tank shell course, or pipeline cross-section")
sigma_e = Symbol(r"\sigma_e", "Elastic critical buckling stress of a cylindrical shell under axial or circumferential compression")

# Seismic Action and Safety Factors
gamma_I = Symbol(r"\gamma_I", "Importance factor applied to the reference seismic action depending on content hazard and failure consequences")
q = Symbol(r"q", "Behaviour factor accounting for energy dissipation and ductility in the structure or supporting framing")
