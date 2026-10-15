try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Latin upper case letters
C_e = Symbol(r"C_e", "Exposure coefficient")
C_t = Symbol(r"C_t", "Thermal coefficient")
C_esl = Symbol(r"C_{esl}", "Coefficient for exceptional snow loads")
A = Symbol(r"A", "Site altitude above sea level [m]")
S_e = Symbol(r"S_e", "Snow load per metre length due to overhang [kN/m]")
F_s = Symbol(r"F_s", "Force per metre length exerted by a sliding mass of snow [kN/m]")

# Latin lower case letters
b = Symbol(r"b", "Width of construction work [m]")
d = Symbol(r"d", "Depth of the snow layer [m]")
h = Symbol(r"h", "Height of construction work [m]")
k = Symbol(r"k", "Coefficient to take account of irregular shape of snow")
l_s = Symbol(r"l_s", "Length of snow drift or snow loaded area [m]")
s = Symbol(r"s", "Snow load on the roof [kN/m2]")
s_k = Symbol(r"s_k", "Characteristic value of snow on the ground at the relevant site [kN/m2]")
s_Ad = Symbol(r"s_{Ad}", "Design value of exceptional snow load on the ground [kN/m2]")

# Greek lower case letters
alpha = Symbol(r"\alpha", "Pitch of roof, measured from horizontal [deg]")
beta = Symbol(r"\beta", "Angle between horizontal and tangent to curve for cylindrical roof [deg]")
gamma = Symbol(r"\gamma", "Weight density of snow [kN/m3]")
mu = Symbol(r"\mu", "Snow load shape coefficient")
mu_1 = Symbol(r"\mu_1", "Snow load shape coefficient (monopitch or pitched roofs)")
mu_2 = Symbol(r"\mu_2", "Snow load shape coefficient (pitched or multi-span roofs)")
mu_3 = Symbol(r"\mu_3", "Snow load shape coefficient (multi-span roofs)")
psi_0 = Symbol(r"\psi_0", "Factor for combination value of a variable action")
psi_1 = Symbol(r"\psi_1", "Factor for frequent value of a variable action")
psi_2 = Symbol(r"\psi_2", "Factor for quasi-permanent value of a variable action")
