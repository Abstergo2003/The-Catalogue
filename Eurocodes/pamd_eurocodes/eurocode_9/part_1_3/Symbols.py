try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Section 1.6 Symbols used in EN 1999-1-3 / ENV 1999-2 (Structures susceptible to fatigue)

# Stress Ranges & Detail Categories
Delta_sigma = Symbol(r"\Delta\sigma", "Normal stress range (Delta_sigma = |sigma_max - sigma_min|)")
Delta_tau = Symbol(r"\Delta\tau", "Shear stress range in welds, bolts, or webs")
Delta_sigma_c = Symbol(r"\Delta\sigma_c", "Reference fatigue strength at 2 * 10^6 cycles (Detail Category in MPa)")
Delta_tau_c = Symbol(r"\Delta\tau_c", "Reference fatigue shear strength at 2 * 10^6 cycles (Shear Detail Category in MPa)")
Delta_sigma_D = Symbol(r"\Delta\sigma_D", "Constant amplitude fatigue limit (CAFL) at N_D = 5 * 10^6 cycles")
Delta_sigma_L = Symbol(r"\Delta\sigma_L", "Cut-off limit below which cyclic stresses do not contribute to fatigue damage (at N_L = 10^8 cycles)")

# S-N Curve Slope Parameters & Cycles
m_1 = Symbol(r"m_1", "Inverse slope of the S-N curve for N <= 5 * 10^6 cycles (typically m1 = 3 to 4)")
m_2 = Symbol(r"m_2", "Inverse slope of the S-N curve for 5 * 10^6 < N <= 10^8 cycles (typically m2 = m1 + 2)")
N = Symbol(r"N", "Endurance (number of stress cycles to failure) at a given constant stress range")
n_i = Symbol(r"n_i", "Number of applied cycles in stress range block Delta_sigma_i")
N_i = Symbol(r"N_i", "Number of cycles to failure corresponding to stress range Delta_sigma_i")
D = Symbol(r"D", "Cumulative fatigue damage index according to Palmgren-Miner summation (D = sum(n_i / N_i))")

# Partial Safety Factors
gamma_Mf = Symbol(r"\gamma_{Mf}", "Partial safety factor for fatigue strength")
gamma_Ff = Symbol(r"\gamma_{Ff}", "Partial factor for fatigue actions")
