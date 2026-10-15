try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Section 1.5 Symbols used in EN 1993-1-9

Delta_sigma = Symbol(r"\Delta\sigma", "Direct stress range")
Delta_tau = Symbol(r"\Delta\tau", "Shear stress range")
Delta_sigma_c = Symbol(r"\Delta\sigma_c", "Reference fatigue strength at 2 * 10^6 cycles (detail category in N/mm2)")
Delta_sigma_D = Symbol(r"\Delta\sigma_D", "Constant amplitude fatigue limit (at 5 * 10^6 cycles)")
Delta_sigma_L = Symbol(r"\Delta\sigma_L", "Cut-off limit for variable amplitude stress ranges (at 10^8 cycles)")
Delta_tau_c = Symbol(r"\Delta\tau_c", "Reference shear fatigue strength at 2 * 10^6 cycles")
m_slope = Symbol(r"m", "Inverse slope of the fatigue S-N curve (m = 3 for N <= 5*10^6, m = 5 for 5*10^6 < N <= 10^8)")
D_fat = Symbol(r"D", "Cumulative fatigue damage index according to Palmgren-Miner rule")
lambda_fat = Symbol(r"\lambda", "Damage equivalent factor for fatigue")
gamma_Mf = Symbol(r"\gamma_{Mf}", "Partial factor for fatigue strength")
