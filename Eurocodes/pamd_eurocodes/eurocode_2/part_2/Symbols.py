try:
    from symbol import Symbol
except ImportError:
    from pamd_eurocodes.symbol import Symbol

# Bridge-specific symbols used in EN 1992-2

l_0_col = Symbol(r"l_0", "Effective buckling height of a bridge column or pier")
l_col = Symbol(r"l_{col}", "Clear height of a column or pier between structural restraints")
V_Rd1 = Symbol(r"V_{Rd1}", "Design shear resistance of a section without shear reinforcement under bridge loading")
V_Rd2 = Symbol(r"V_{Rd2}", "Maximum design shear resistance limited by crushing of compression struts in webs")
V_Rd3 = Symbol(r"V_{Rd3}", "Design shear resistance of a section with shear reinforcement")
Delta_sigma_Rsk = Symbol(r"\Delta\sigma_{Rsk}", "Characteristic fatigue strength of reinforcing steel at 10^6 cycles under bridge traffic")
S_cd_min_equ = Symbol(r"S_{cd,min,equ}", "Equivalent minimum compressive stress level in concrete under fatigue loading")
S_cd_max_equ = Symbol(r"S_{cd,max,equ}", "Equivalent maximum compressive stress level in concrete under fatigue loading")
phi_p = Symbol(r"\phi_p", "Equivalent diameter of a prestressing tendon")
cot_theta = Symbol(r"\cot\theta", "Cotangent of the angle between concrete compression struts and the main longitudinal tension chord")
w_max_bridge = Symbol(r"w_{max}", "Limiting design crack width for reinforced or prestressed concrete bridges")
Delta_h_cover = Symbol(r"\Delta h", "Allowance for tolerance in concrete cover for in-situ or precast bridge elements")
