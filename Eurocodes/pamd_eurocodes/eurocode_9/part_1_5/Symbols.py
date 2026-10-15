try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Section 1.6 Symbols used in EN 1999-1-5 (Shell structures)

# Shell Geometry & Imperfections
r = Symbol(r"r", "Radius of cylindrical or conical shell middle surface")
t = Symbol(r"t", "Nominal thickness of shell wall")
L = Symbol(r"L", "Cylinder length between ring stiffeners or boundary supports")
Delta_w_k = Symbol(r"\Delta w_k", "Characteristic amplitude of initial radial shell wall imperfection (dimple)")
omega_shell = Symbol(r"\omega", "Dimensionless shell length parameter (omega = L / sqrt(r * t))")

# Critical Elastic Buckling Stresses
sigma_x_Rcr = Symbol(r"\sigma_{x,Rcr}", "Critical elastic meridional (axial) buckling stress of shell")
sigma_theta_Rcr = Symbol(r"\sigma_{\theta,Rcr}", "Critical elastic circumferential (hoop) buckling stress under external pressure")
tau_xtheta_Rcr = Symbol(r"\tau_{x\theta,Rcr}", "Critical elastic in-plane shear buckling stress of shell")

# Imperfection Knock-Down & Reduction Factors
alpha_x = Symbol(r"\alpha_x", "Elastic knock-down imperfection factor for axial meridional compression")
alpha_theta = Symbol(r"\alpha_\theta", "Elastic knock-down imperfection factor for circumferential compression")
alpha_tau = Symbol(r"\alpha_\tau", "Elastic knock-down imperfection factor for membrane shear")
lambda_bar_x = Symbol(r"\bar{\lambda}_x", "Relative shell slenderness parameter for meridional buckling")
chi_x = Symbol(r"\chi_x", "Buckling reduction factor for axial compression")

# Partial Safety Factor
gamma_M1 = Symbol(r"\gamma_{M1}", "Partial safety factor for shell stability and buckling resistance (gamma_M1 = 1.10)")
