try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Latin upper case letters
F_k = Symbol(r"F_k", "Characteristic value of a crane action")
F_w = Symbol(r"F_w", "Forces caused by in-service wind")
H_B = Symbol(r"H_B", "Buffer force")
H_L = Symbol(r"H_L", "Longitudinal loads caused by acceleration and deceleration")
H_S = Symbol(r"H_S", "Horizontal loads caused by skewing")
H_T = Symbol(r"H_T", "Transverse loads caused by acceleration and deceleration")
H_TA = Symbol(r"H_{TA}", "Tilting force")
K = Symbol(r"K", "Drive force")
Q_c = Symbol(r"Q_c", "Selfweight of the crane")
Q_h = Symbol(r"Q_h", "Hoistload")
Q_T = Symbol(r"Q_T", "Test load")

# Latin lower case letters
h = Symbol(r"h", "Distance between instantaneous slide pole and guidance means")
k_Q = Symbol(r"k_Q", "Load spectrum factor")
l = Symbol(r"l", "Span of the crane bridge")
m_c = Symbol(r"m_c", "Mass of the crane")
m_w = Symbol(r"m_w", "Number of single wheel drives")
n = Symbol(r"n", "Number of wheel pairs")
v_h = Symbol(r"v_h", "Steady hoisting speed in [m/s]")

# Greek lower case letters
alpha = Symbol(r"\alpha", "Skewing angle")
lambda_dam = Symbol(r"\lambda", "Damage equivalent factor")
mu_fric = Symbol(r"\mu", "Friction factor")
phi_i = Symbol(r"\varphi_i", "Dynamic factor")
phi_1 = Symbol(r"\varphi_1", "Dynamic factor for crane self-weight excitation")
phi_2 = Symbol(r"\varphi_2", "Dynamic factor for hoisting ungrounded load")
phi_3 = Symbol(r"\varphi_3", "Dynamic factor for sudden release of payload")
phi_4 = Symbol(r"\varphi_4", "Dynamic factor for travelling on rails")
phi_5 = Symbol(r"\varphi_5", "Dynamic factor for acceleration / deceleration")
psi_0 = Symbol(r"\psi_0", "Combination factor for crane loads")
psi_1 = Symbol(r"\psi_1", "Frequent value factor for crane loads")
psi_2 = Symbol(r"\psi_2", "Quasi-permanent value factor for crane loads")
