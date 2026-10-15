try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Latin upper case letters
R = Symbol(r"R", "Thermal resistance of structural element")
R_in = Symbol(r"R_{in}", "Thermal resistance at inner surface")
R_out = Symbol(r"R_{out}", "Thermal resistance at outer surface")
T_max = Symbol(r"T_{max}", "Maximum shade air temperature (50-year return period)")
T_min = Symbol(r"T_{min}", "Minimum shade air temperature (50-year return period)")
T_max_p = Symbol(r"T_{max,p}", "Maximum shade air temperature with annual exceedence probability p")
T_min_p = Symbol(r"T_{min,p}", "Minimum shade air temperature with annual exceedence probability p")
T_e_max = Symbol(r"T_{e,max}", "Maximum uniform bridge temperature component")
T_e_min = Symbol(r"T_{e,min}", "Minimum uniform bridge temperature component")
T_0 = Symbol(r"T_0", "Initial temperature when structural element is restrained")
T_in = Symbol(r"T_{in}", "Air temperature of the inner environment")
T_out = Symbol(r"T_{out}", "Temperature of the outer environment")
Delta_T_U = Symbol(r"\Delta T_U", "Uniform temperature component")
Delta_T_N_exp = Symbol(r"\Delta T_{N,exp}", "Maximum expansion range of uniform bridge temperature component")
Delta_T_N_con = Symbol(r"\Delta T_{N,con}", "Maximum contraction range of uniform bridge temperature component")
Delta_T_N = Symbol(r"\Delta T_N", "Overall range of uniform bridge temperature component")
Delta_T_M = Symbol(r"\Delta T_M", "Linear temperature difference component")
Delta_T_M_heat = Symbol(r"\Delta T_{M,heat}", "Linear temperature difference component (heating)")
Delta_T_M_cool = Symbol(r"\Delta T_{M,cool}", "Linear temperature difference component (cooling)")
Delta_T_E = Symbol(r"\Delta T_E", "Non-linear part of temperature difference component")
Delta_T = Symbol(r"\Delta T", "Sum of linear and non-linear temperature difference components")
Delta_T_p = Symbol(r"\Delta T_p", "Temperature difference between different parts of a structure")

# Latin lower case letters
h = Symbol(r"h", "Height of the cross-section")
k_sur = Symbol(r"k_{sur}", "Surfacing factor for linear temperature difference component")
p = Symbol(r"p", "Annual probability of maximum (minimum) shade air temperature being exceeded")

# Greek lower case letters
alpha_T = Symbol(r"\alpha_T", "Coefficient of linear expansion [1/deg C]")
lambda_therm = Symbol(r"\lambda", "Thermal conductivity")
omega_N = Symbol(r"\omega_N", "Reduction factor of uniform temperature component for combination")
omega_M = Symbol(r"\omega_M", "Reduction factor of temperature difference component for combination")
