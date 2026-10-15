try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Section 1.7 Special symbols used in ENV 1992-1-4

LC = Symbol(r"LC", "Prefix for strength classes of lightweight aggregate concrete")
eta_E = Symbol(r"\eta_E", "Conversion factor for calculation of modulus of elasticity = (rho/2200)^2")
eta_1 = Symbol(r"\eta_1", "Coefficient for determination of tensile strength = 0.40 + 0.60 * (rho/2200)")
eta_2 = Symbol(r"\eta_2", "Ratio of moduli of elasticity of lightweight aggregate concrete and normal weight concrete")
eta_3 = Symbol(r"\eta_3", "Factor for the evaluation of creep coefficients of lightweight aggregate concrete")
eta_4 = Symbol(r"\eta_4", "Factor for the evaluation of basic shrinkage strains of lightweight aggregate concrete")
rho_density = Symbol(r"\rho", "Oven-dry density of lightweight aggregate concrete in kg/m3")
f_lck = Symbol(r"f_{lck}", "Characteristic compressive cylinder strength of lightweight concrete (N/mm2)")
E_lcm = Symbol(r"E_{lcm}", "Secant modulus of elasticity of lightweight aggregate concrete")
f_lct_eff = Symbol(r"f_{lct,eff}", "Effective tensile strength of lightweight concrete at the time when cracking occurs")
