try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Section 1.6 Symbols used in EN 1999-1-2 / ENV 1999-1-2 (Structural fire design for aluminium)

# Temperature and Thermal Parameters
theta_a = Symbol(r"\theta_a", "Temperature of the aluminium member (deg C)")
theta_crit = Symbol(r"\theta_{crit}", "Critical failure temperature of an aluminium member under design fire actions (deg C)")
lambda_a = Symbol(r"\lambda_a", "Thermal conductivity of the aluminium alloy (W/(m*K))")
c_a = Symbol(r"c_a", "Specific heat capacity of the aluminium alloy (J/(kg*K))")
epsilon_m = Symbol(r"\varepsilon_m", "Surface emissivity of the aluminium member")

# High-Temperature Reduction Factors
k_theta_p02 = Symbol(r"k_{\theta,p0.2}", "Reduction factor for 0.2% proof strength of aluminium at temperature theta_a")
k_theta_u = Symbol(r"k_{\theta,u}", "Reduction factor for ultimate tensile strength of aluminium at temperature theta_a")
k_theta_E = Symbol(r"k_{\theta,E}", "Reduction factor for modulus of elasticity of aluminium at temperature theta_a")

# Cross-sectional and Geometric Parameters
A_m_V = Symbol(r"A_m / V", "Section factor for unprotected aluminium members (m^-1)")
A_p_V = Symbol(r"A_p / V", "Section factor for fire-protected aluminium members (m^-1)")
t_fi_d = Symbol(r"t_{fi,d}", "Design fire resistance duration under standard temperature-time curve (min)")

# Partial Safety Factor
gamma_M_fi = Symbol(r"\gamma_{M,fi}", "Partial safety factor for fire design situation (gamma_M,fi = 1.0)")
