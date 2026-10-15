try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Section 1.6 Symbols used in EN 1998-3 (Assessment and retrofitting of buildings)

CF = Symbol(r"CF", "Confidence Factor applied to existing material strengths based on Knowledge Level")
KL = Symbol(r"KL", "Knowledge Level regarding geometry, detailing, and materials of the existing building")

theta_y = Symbol(r"\theta_y", "Chord rotation at yield of structural component")
theta_u = Symbol(r"\theta_u", "Ultimate chord rotation capacity of structural component")
theta_um = Symbol(r"\theta_{um}", "Mean value of ultimate chord rotation from experimental testing")

d_t = Symbol(r"d_t", "Target displacement of the structural system under nonlinear static pushover analysis")
gamma_el = Symbol(r"\gamma_{el}", "Partial factor for existing material properties")
L_V = Symbol(r"L_V", "Shear span of member (ratio of bending moment to shear force M / V)")
rho_s = Symbol(r"\rho_s", "Volumetric ratio of transverse confining reinforcement")
omega_conf = Symbol(r"\omega", "Mechanical reinforcement ratio of confining steel")
