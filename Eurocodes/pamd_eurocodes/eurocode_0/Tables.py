try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

indicative_design_working_life = Table(
    ["Design working life category", "Indicative design working life (years)", "Examples"],
    [
        ["1", "10", "Temporary structures"],
        ["2", "10 to 25", "Replacable structural parts, e.g. gantry girders, bearings"],
        ["3", "15 to 30", "Agricultural and similar structures"],
        ["4", "50", "Building structures and other common structures"],
        ["5", "100", "Monumental building structures, bridges and other civil engineering structures"]
    ],
    "Indicative design working life",
    "(1) Structures or parts of structures that can be dismantled with a view to being re-used should not be considered as temporary"
)
recommended_values_of_phi_factors_for_buildings = Table(
    ["Action", "$ \psi_0 $", "$ \psi_1 $", "$ \psi_3 $"],
    [
        ["Imposed loads in buildings, category (see EN 1991-1-1)", "", "", ""],
        ["Category A : domestic, residential areas", 0.7, 0.5, 0.3],
        ["Category B : office areas", 0.7, 0.5, 0.3],
        ["Category C : congregation areas", 0.7, 0.7, 0.6],
        ["Category D : shopping areas", 0.7, 0.7, 0.6],
        ["Category E : storage areas", 1.0, 0.9, 0.8],
        ["Category F : traffic area, vehicle weight <= 30kN", 0.7, 0.7, 0.6],
        ["Category G : traffic area, 30kN < vehicle weight <= 160kN", 0.7, 0.5, 0.3],
        ["Category H : roofs", 0, 0, 0],
        ["---", "---", "---"],
        ["Snow loads on buildings (see EN 1991-1-3)* Finland, Iceland, Norway, Sweden", 0.7, 0.5, 0.2],
        ["Remainder  of  CEN  Member  States,  for  sites located at altitude H > 1000 m a.s.l.", 0.7, 0.5, 0.2],
        ["Remainder  of  CEN  Member  States,  for  sites located at altitude H <= 1000 m a.s.l.", 0.5, 0.2, 0],
        ["Wind loads on buildings (see EN 1991-1-4)", 0.6, 0.2, 0],
        ["Temperature (non-fire) in buildings (see EN 1991-1-5)", 0.6, 0.5, 0],
    ],
    "Recommended values of $ \\psi $ factors for buildings",
    "NOTE  The $ \\psi $ values may be set by the National annex, \n* For countries not mentioned below, see relevant local conditions."
)
design_values_of_actions_EQU_set_A = Table(
    ["Persistent and transient design situations", "Permanent actions - Unfavourable", "Permanent actions - Favourable", "Leading variable action (*)", "Accompanying variable actions - Main (if any)", "Accompanying variable actions - Others"],
    [
        ["(Eq. 6.10)", "$ \\gamma_{Gj,sup} * G_{kj,sup} $", "$ \\gamma_{Gj,inf}*G_{kj,inf} $", "$ \\gamma_{Q,1}*Q_{k,1} $", "", "$ \\gamma_{Q,i}*\\phi_{0,i}*Q_{k,i} $"]
    ],
    "Design values of actions (EQU) (Set A)",
    """
(*) Variable actions are those considered in Table A1.1
NOTE 1  The $ \\gamma $ values may be set by the National annex. The recommended set of values for $ \gamma $ are :
$ \\gamma_{Gj,sup} $ = 1,10
$ \\gamma_{Gj,inf} $ = 0,90
$ \\gamma_{Q,1} $ = 1,50 where unfavourable (0 where favourable)
$ \\gamma_{Q,i} $ = 1,50 where unfavourable (0 where favourable)
NOTE  2  In  cases  where  the  verification  of  static  equilibrium  also  involves  the  resistance  of  structural
members,  as  an  alternative  to  two  separate  verifications  based  on  Tables  A1.2(A)  and  A1.2(B),  a
combined verification, based on Table A1.2(A), may be adopted, if allowed by the National annex, with
the  following  set  of  recommended  values.  The  recommended  values  may  be  altered  by  the  National
annex.
$ \\gamma_{Gj,sup} $ = 1,35
$ \\gamma_{Gj,inf} $ = 1,15
$ \\gamma_{Q,1} $ = 1,50 where unfavourable (0 where favourable)
$ \\gamma_{Q,i} $ = 1,50 where unfavourable (0 where favourable)
provided that applying $ \\gamma_{Gj,inf} $ = 1,00 both to the favourable part and to the unfavourable part of permanent
actions does not give a more unfavourable effect.
    """
)
design_values_of_actions_STR_Set_B = Table(
    ["Persistent and transient design situations", "Permanent actions - Unfavourable", "Permanent actions - Favourable", "Leading variable action (*)", "Accompanying variable actions - Main (if any)", "Accompanying variable actions - Others"],
    [
        ["(Eq. 6.10)", "$ \\gamma_{Gj,sup} * G_{kj,sup} $", "$ \\gamma_{Gj,inf}*G_{kj,inf} $", "$ \\gamma_{Q,1}*Q_{k,1} $", "", "$ \\gamma_{Q,i}*\\phi_{0,i}*Q_{k,i} $"]
    ],
    "Design values of actions (STR) (Set B)",
    """
(*) Variable actions are those considered in Table A1.1
NOTE  1  The  choice  between  6.10,  or  6.10a  and  6.10b  will  be  in  the  National  annex.  In  case  of  6.10a  and  6.10b,  the  National  annex  may  in  addition  modify  6.10a  to  include permanent actions only.
NOTE 2  The $ \\psi $ and $ \\xi $ values may be set by the National annex. The following values for $ \\psi $ and $ \\gamma $ are recommended when using expressions 6.10, or 6.10a and 6.10b.
$ \\gamma_{Gj,sup} $ = 1,35
$ \\gamma_{Gj,inf} $ = 1,00
$ \\gamma_{Q,1} $ = 1,50 where unfavourable (0 where favourable)
$ \\gamma_{Q,i} $ = 1,50 where unfavourable (0 where favourable)
$ \\xi $ = 0,85 (so that $ \\xi_{\\gammaGj,sup} = 0,85 * 1,35 = 1,15 $).
See also EN 1991 to EN 1999 for $ \\gamma $ values to be used for imposed deformations.
NOTE 3  The characteristic values of all permanent actions from one source are multiplied by $ \\gamma_{G,sup} $ if the total resulting action  effect  is  unfavourable  and $ \\gamma_{G,inf} $ if  the  total  resulting action  effect  is  favourable.  For  example,  all  actions  originating  from  the  self  weight  of  the  structure  may  be  considered  as  coming  from  one  source  ;  this  also  applies  if  different materials are involved.
NOTE 4  For particular verifications, the values for $ \\gamma_G $ and $ \\gamma_Q $ may be subdivided into $ \\gamma_g $ and $ \\gamma_q $ and the model uncertainty factor $ \\gamma_{Sd} $. A value of $ \\gamma_{Sd} $ in the range 1,05 to 1,15 can be used in most common cases and can be modified in the National annex.
    """
)

design_values_of_actions_GEO_Set_B = Table(
    ["Persistent and transient design situations", "Permanent actions - Unfavourable", "Permanent actions - Favourable", "Leading variable action (*)", "Accompanying variable actions(*) - Main (if any)", "Accompanying variable actions(*) - Others"],
    [
        ["(Eq. 6.10a)", "$ \\gamma_{Gj,sup} * G_{kj,sup} $", "$ \\gamma_{Gj,inf}*G_{kj,inf} $", "", "$ \\gamma_{Q,1}*\\psi_{0,1}*Q_{k,1} $", "$ \\gamma_{Q,i}*\\psi_{0,i}*Q_{k,i} $"],
        ["(Eq. 6.10b)", "$ \\xi*\\gamma_{Gj,sup} * G_{kj,sup} $", "$ \\gamma_{Gj,inf}*G_{kj,inf} $", "$ \\gamma_{Q,1}*Q_{k,1} $", "", "$ \\gamma_{Q,i}*\\psi_{0,i}*Q_{k,i} $"]
    ],
    "Design values of actions (GEO) (Set B)",
    """
(*) Variable actions are those considered in Table A1.1
NOTE  1  The  choice  between  6.10,  or  6.10a  and  6.10b  will  be  in  the  National  annex.  In  case  of  6.10a  and  6.10b,  the  National  annex  may  in  addition  modify  6.10a  to  include permanent actions only.
NOTE 2  The $ \\psi $ and $ \\xi $ values may be set by the National annex. The following values for $ \\psi $ and $ \\gamma $ are recommended when using expressions 6.10, or 6.10a and 6.10b.
$ \\gamma_{Gj,sup} $ = 1,35
$ \\gamma_{Gj,inf} $ = 1,00
$ \\gamma_{Q,1} $ = 1,50 where unfavourable (0 where favourable)
$ \\gamma_{Q,i} $ = 1,50 where unfavourable (0 where favourable)
$ \\xi $ = 0,85 (so that $ \\xi_{\\gammaGj,sup} = 0,85 * 1,35 = 1,15 $).
See also EN 1991 to EN 1999 for $ \\gamma $ values to be used for imposed deformations.
NOTE 3  The characteristic values of all permanent actions from one source are multiplied by $ \\gamma_{G,sup} $ if the total resulting action  effect  is  unfavourable  and $ \\gamma_{G,inf} $ if  the  total  resulting action  effect  is  favourable.  For  example,  all  actions  originating  from  the  self  weight  of  the  structure  may  be  considered  as  coming  from  one  source  ;  this  also  applies  if  different materials are involved.
NOTE 4  For particular verifications, the values for $ \\gamma_G $ and $ \\gamma_Q $ may be subdivided into $ \\gamma_g $ and $ \\gamma_q $ and the model uncertainty factor $ \\gamma_{Sd} $. A value of $ \\gamma_{Sd} $ in the range 1,05 to 1,15 can be used in most common cases and can be modified in the National annex.
    """
)

design_values_of_actions_GEO_Set_C = Table(
    ["Persistent and transient design situations", "Permanent actions - Unfavourable", "Permanent actions - Favourable", "Leading variable action (*)", "Accompanying variable actions(*) - Main (if any)", "Accompanying variable actions(*) - Others"],
    [
        ["(Eq. 6.10)", "$ \\gamma_{Gj,sup} * G_{kj,sup} $", "$ \\gamma_{Gj,inf} * G_{kj,inf} $", "$ \\gamma_{Q,1} * Q_{k,1} $", "", "$ \\gamma_{Q,i} * \\psi_{0,i} * Q_{k,i} $"]
    ],
    "Design values of actions (STR/GEO) (Set C)",
    """
(*) Variable actions are those considered in Table A1.1
NOTE  The $ \\gamma $ values may be set by the National annex. The recommended set of values for $ \\gamma $ are :
$ \\gamma_{Gj,sup} $ = 1,00
$ \\gamma_{Gj,inf} $ = 1,00
$ \\gamma_{Q,1} $ = 1,30 where unfavourable (0 where favourable)
$ \\gamma_{Q,i} $ = 1,30 where unfavourable (0 where favourable)
    """
)
design_values_of_actions_for_use_in_accidental_and_seismic_combinations_of_actions = Table(
    ["Design situation", "Permanent actions - unfavourable", "Permanent actions - favourable", "Leading accidental or seismic action", "Accompanying variable actions (**) - main (if any)", "Accompanying variable actions (**) - others"],
    [
        ["Accidental (*) (Eq. 6.11a/b)", "$ G_{kj,sup} $", "$ G_{kj,inf} $", "$ A_d $", "$ \\psi_{11} $ or $ \\psi_{21}*Q_{k1} $", "$ \\psi_{2,i}*Q_{k,i} $"],
        ["Seismic (Eq. 6.12a/b)", "$ G_{kj,sup} $", "$ G_{kj,inf} $", "$ \\gamma*A_{EK} $ or $  A_{Ed}$", "$ \\psi_{2,i}*Q_{k,i} $", "$ \\psi_{2,i}*Q_{k,i} $"]
    ],
    "Design values of actions for use in accidental and seismic combinations of actions",
    """
(*) In the case of accidental design situations, the main variable action may be taken with its frequent or, as in seismic  combinations  of  actions,  its  quasi-permanent  values.  The  choice  will  be  in  the  National  annex, depending on the accidental action under consideration. See also EN 1991-1-2.
(**) Variable actions are those considered in Table A1.1
    """
)

design_values_of_actions_for_use_in_the_combination_of_actions = Table(
    ["Combination", "Permanent actions $ G_d $ - Unfavourable", "Permanent actions $ G_d $ - Favourable", "Variable actions $ Q_d $ - Leading", "Variable actions $ Q_d $ - Others"],
    [
        ["Characteristic", "$ G_{kj,sup} $", "$ G_{kj,inf} $", "$ Q_{k,1} $", "$ \\psi_{0,i}*Q_{k,i} $"],
        ["Frequent", "$ G_{kj,sup} $", "$ G_{kj,inf} $", "$ \\psi_{1,1}*Q_{k,1} $", "$ \\psi_{2,i}*Q_{k,i} $"],
        ["Quasi-permanent", "$ G_{kj,sup} $", "$ G_{kj,inf} $", "$ \\psi_{2,1}*Q_{k,1} $", "$ \\psi_{2,i}*Q_{k,i} $"],
    ],
    "Design values of actions for use in the combination of actions",
    ""
)

definition_of_consequences_classes = Table(
    ["Consequences Class", "Description", "Examples of buildings and civil engineering works"],
    [
        ["CC3", "High consequence for loss of human life, or economic, social or environmental consequences very great", "Grandstands, public buildings where consequences of failure are high (e.g. a concert hall)"],
        ["CC2", "Medium consequence for loss of human life, economic, social or environmental consequences considerable", "Residential and office buildings, public buildings where consequences of failure are medium (e.g. an office building)"],
        ["CC1", "Low consequence for loss of human life, and economic, social or environmental consequences small or negligible", "Agricultural buildings where people do not normally enter (e.g. storage buildings), greenhous"]
    ],
    "Definition of consequences classes",
    "NOTE  At  the  present  time  the  requirements  for  reliability  are  related  to  the  structural  members  of  the construction works."
)

recommended_minimum_values_for_reliability_index = Table(
    ["Reliability Class", "Minimum values for $ \\beta $ - 1 year reference period", "Minimum values for $ \\beta $ - 50 years reference period"],
    [
        ["RC3", 5.2, 4.3],
        ["RC2", 4.7, 3.8],
        ["RC1", 4.2, 3.3]
    ],
    "Recommended minimum values for reliability index $ \\beta $ (ultimate limit states)",
    "NOTE  A  design  using  EN  1990  with  the  partial  factors  given  in  annex  A1  and  EN  1991  to  EN  1999  is considered  generally  to  lead  to  a  structure  with  a  $ \\beta $  value  greater  than  3,8  for  a  50  year  reference  period. Reliability  classes  for  members  of  the  structure  above  RC3  are  not  further  considered  in  this  Annex,  since these structures each require individual consideration."
)

KFI_factor_for_actions = Table(
    ["$ K_{FI} $ factor for actions", "Reliability class RC1", "Reliability class RC2", "Reliability class RC2",],
    [
        ["$ K_{FI} $", 0.9, 1.0, 1.1]
    ],
    "$ K_{FI} $ factor for actions",
    "NOTE  In particular, for class RC3, other  measures  as  described  in  this  Annex  are  normally  preferred  to using KFI factors. KFI should be applied only to unfavourable actions."
)

design_supervision_levels_DSL = Table(
    ["Design Supervision Levels", "Characteristics", "Minimum recommended requirements for checking of calculations, drawings and specifications"],
    [
        ["DSL3 relating to RC3", "Extended supervision", "Third party checking : Checking performed by an organisation different from that which has prepared the design"],
        ["DSL2 relating to RC2", "Normal supervision", "Checking by different persons than those originally responsible and in accordance with the procedure of the organisation."],
        ["DSL1 relating to RC1", "Normal supervision", "Self-checking: Checking performed by the person who has prepared the design"]
    ],
    "Design supervision levels (DSL)",
    ""
)

inspection_levels_IL = Table(
    ["Inspection Levels", "Characteristics", "Requirements"],
    [
        ["IL3 Relating to RC3", "Extended inspection", "Third party inspection"],
        ["IL2 Relating to RC2", "Normal inspection", "Inspection in accordance with the procedures of the organisation"],
        ["IL1 Relating to RC1", "Normal inspection", "Self inspection"],
    ],
    "Inspection levels (IL)",
    "NOTE  Inspection  levels  define  the  subjects  to  be  covered  by  inspection  of  products  and  execution  of works including the scope of inspection. The rules will thus vary from one structural material to another, and are to be given in the relevant execution standards."
)

relation_between_beta_and_Pf = Table(
    ["$ P_f $", "1e-1", "1e-2", "1e-3", "1e-4", "1e-5", "1e-6", "1e-7"],
    [
        ["$ \\beta $", 1.28, 2.32, 3.09, 3.72, 4.27, 4.75, 5.20]
    ],
    "Relation between $ \\beta $ and $ P_f $",
    ""
)

target_reliability_index_beta_for_Class_RC2_structural_members = Table(
    ["Limit state", "Target reliability index - 1 year", "Target reliability index - 50 years"],
    [
        ["Ultimate", 4.7, 3.8],
        ["Fatigue (2)", "", BRange(1.5, 3.8, 1.5)],
        ["Serviceability (irreversible)", 2.9, 1.5]
    ],
    "Target reliability index $ \\beta $ for Class RC2 structural members ",
    """
1) See Annex B
2) For 50 years - Depends on degree of inspectability, reparability and damage tolerance.
    """
)
design_values_for_various_distribution_functions = Table(
    ["Distribution", "Design values"],
    [
        ["Normal", "$ \\mu - \\alpha*\\beta*\\sigma $"],
        ["Lognormal", "$ \\mu \\exp(-\\alpha \\beta V) $"],
        ["Gumbel", "$ u - \\frac{1}{a} \\ln(-\\ln\\Phi(-\\alpha\\beta)) $ \n where $ u = \\mu - \\frac{0.577}{a} $; $ a = \\frac{\\pi}{\\sigma\\sqrt{6}} $"]
    ],
    "Design values for various distribution functions",
    "NOTE  In these expressions $ \\mu $, $ \\sigma $ and  V are,  respectively,  the  mean  value,  the  standard  deviation  and  the coefficient of variation of a given variable. For variable actions, these should be based on the same reference period as for $ \\beta $"
)

expressions_for_psi_for_the_case_of_two_variable_actions = Table(
    ["Distribution", "$ \\psi_0 = F_{accompanying}/F_{leading} $"],
    [
        ["General", "$ \\frac{F_s^{-1}(\\Phi(0,4\\beta')^{N_1})}{F_s^{-1}(\\Phi(0,7\\beta')^{N_1})} $ \n with $ \\beta' = -\\Phi^{-1}(\\Phi(-0.7\\beta)/N_1) $"],
        ["Approximation for very large $N_1$", "$ \\frac{F_s^{-1}(\\exp(-N_1\\Phi(0.4\\beta')))}{F_s^{-1}(\\Phi(0.7\\beta'))} $ with $ \\beta' = -\\Phi^{-1}(\\Phi(-0.7\\beta)/N_1) $"],
        ["Normal (approximation)", "$ \\frac{1+(0.28\\beta-0.7\\ln N_1)V}{1+0.7\\beta} $"],
        ["Gumbel (approximation)", "$ \\frac{1-0.78V(0.58+\\ln(-\\ln\\Phi(0.28\\beta))+\\ln N_1)}{1-0.78V(0.58+\\ln(-\\ln(0.7\\beta)))} $"]
    ],
    "Expressions for $ \\psi_0 $ for the case of two variable actions",
    """
$F_s$(.) is the probability distribution function of the extreme value of the accompanying action in the reference period T ;
$\\Phi$(.) is the standard Normal distribution function ;
T is the reference period ;
$T_1$ is the greater of the basic periods for actions to be combined ;
$N_1$ is the ratio T/T1, approximated to the nearest integer ;
$\\beta$ is the reliability index ;
V is the coefficient of variation of the accompanying action for the reference period.
    """
)

values_of_kn_for_the_5p_characteristic_value = Table(
    ["n", "1", "2", "3", "4", "5", "6", "8", "10", "20", "30", "inf"],
    [
        ["$ V_X $ known", 2.31, 2.01, 1.89, 1.83, 1.80, 1.77, 1.74, 1.72, 1.68, 1.67, 1.64],
        ["$ V_X $ uknown", "-", "-", 3.37, 2.63, 2.33, 2.18, 2.00, 1.92, 1.76, 1.73, 1.64]
    ],
    "Values of $ k_n $ for the 5% characteristic value",
    """
NOTE 1  This table is based on the Normal distribution.
NOTE 2  With a log-normal distribution expression (D.1) becomes :
$ X_d = \\frac{\\eta_d}{\\gamma_m}\\exp(m_y - k_n s_y) $
where:
$ m_y = \\frac{1}{n} \\Sigma\\ln(\\chi_i) $
If $ V_X $ is known from prior knowledge, $ s_y = \\sqrt{\\ln(V_x^2+1)} = V_X $
If $ V_X $ is unknown from prior knowledge, $ s_y = \\sqrt{\\frac{1}{n-1}\\Sigma(\\ln\\chi_i-m_y)^2} $ 
    """
)

values_of_kdn_for_the_ULS_design_value = Table(
    ["n", "1", "2", "3", "4", "5", "6", "8", "10", "20", "30", "inf"],
    [
        ["$ V_X $ known", 4.36, 3.77, 3.56, 3.44, 3.37, 3.33, 3.27, 3.23, 3.16, 3.13, 3.04],
        ["$ V_X $ unknown", "-", "-", "-", 11.40, 7.85, 6.36, 5.07, 4.51, 3.64, 3.44, 3.04]
    ],
    "Values of $ k_{d,n} $ for the ULS design value.",
    """
NOTE  1  This  table  is  based  on  the  assumption  that  the  design  value  corresponds  to  a  product  $ \\alpha_R \\beta = 0.8\\bullet 3.8 = 3.04 $ (see annex C) and  that  X   is  Normally  distributed.  This  gives  a  probability  of  observing  a lower value of about 0,1 %.
NOTE 2  With a log-normal distribution, expression (D.4) becomes :
$ X_d = \\eta_d \\exp(m_y - k_{d,n} s_y) $
    """
)

reduction_factor_nk = Table(
    ["Coefficient of variation $V_r$", "Reduction factor $\\eta_k$ for 1 test", "Reduction factor $\\eta_k$ for 2 or 3 tests"],
    [
        [0.05, 0.80, 0.90],
        [0.11, 0.70, 0.80],
        [0.17, 0.60, 0.70]
    ],
    "Reduction factor $ \\eta_k $",
    ""
)