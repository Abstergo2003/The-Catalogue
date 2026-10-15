try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Section 1.6 Supplementary symbols to EN 1992-1-1 used in EN 1992-1-2

# Latin upper case letters
E_d_fi = Symbol(r"E_{d,fi}", "Design effect of actions in the fire situation")
E_d = Symbol(r"E_d", "Design effect of actions for normal temperature design")
R_d_fi = Symbol(r"R_{d,fi}", "Design resistance in the fire situation; R_{d,fi}(t) at a given time t")
R_class = Symbol(r"R", "Fire resistance class for the load-bearing criterion for 30, 60... minutes in standard fire exposure")
E_class = Symbol(r"E", "Fire resistance class for the integrity criterion for 30, 60... minutes in standard fire exposure")
I_class = Symbol(r"I", "Fire resistance class for the insulation criterion for 30, 60... minutes in standard fire exposure")
T_temp = Symbol(r"T", "Temperature [K]")
X_k = Symbol(r"X_k", "Characteristic value of a material property for normal temperature design")
X_k_theta = Symbol(r"X_k(\theta)", "Characteristic value of a material property in the fire situation, dependent on the material temperature theta")
f_pk_theta = Symbol(r"f_{pk}(\theta)", "Characteristic value of strength of prestressing steel at temperature theta for a specified strain")
f_sk_theta = Symbol(r"f_{sk}(\theta)", "Characteristic strength of reinforcing steel at temperature theta for a specified strain")
k_theta = Symbol(r"k(\theta)", "Reduction factor for a strength or deformation property dependent on the material temperature theta = X_k(theta)/X_k")
n_load = Symbol(r"n", "Load level of a column at normal temperature conditions = N0_{Ed,fi} / (0,7(A_c f_{cd} + A_s f_{yd}))")
t_fire = Symbol(r"t", "Time of fire exposure (min)")

# Greek lower case letters
gamma_M_fi = Symbol(r"\gamma_{M,fi}", "Partial safety factor for a material in fire design")
eta_fi = Symbol(r"\eta_{fi}", "Reduction factor for design load level in the fire situation = E_{d,fi}/E_d")
mu_fi = Symbol(r"\mu_{fi}", "Degree of utilisation in fire situation = N_{Ed,fi} / N_{Rd}")
epsilon_c_theta = Symbol(r"\varepsilon_c(\theta)", "Thermal strain of concrete")
epsilon_p_theta = Symbol(r"\varepsilon_p(\theta)", "Thermal strain of prestressing steel")
epsilon_s_theta = Symbol(r"\varepsilon_s(\theta)", "Thermal strain of reinforcing steel")
epsilon_s_fi = Symbol(r"\varepsilon_{s,fi}", "Strain of the reinforcing or prestressing steel at temperature theta")
lambda_c = Symbol(r"\lambda_c", "Thermal conductivity of concrete [W/mK]")
lambda_0_fi = Symbol(r"\lambda_{0,fi}", "Slenderness of the column under fire conditions")
sigma_c_fi = Symbol(r"\sigma_{c,fi}", "Compressive stress of concrete in fire situation")
sigma_s_fi = Symbol(r"\sigma_{s,fi}", "Steel stress in fire situation")
theta_deg = Symbol(r"\theta", "Temperature [deg C]")
theta_cr = Symbol(r"\theta_{cr}", "Critical temperature [deg C]")
