try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 2.1
seismic_assessment_limit_states_and_return_periods = Table(
    ["Limit State for Assessment", "Probability of exceedance in 50 years", "Reference return period TN [years]", "Structural performance level"],
    [
        ["Damage Limitation (DL)", "20%", 225, "Negligible structural damage; minor non-structural repairs"],
        ["Significant Damage (SD)", "10%", 475, "Significant structural damage; residual lateral capacity; life safe"],
        ["Near Collapse (NC)", "2%", 2475, "Heavy structural damage; low residual strength; collapse prevented"]
    ],
    "Limit states and recommended return periods for seismic assessment of existing buildings (EN 1998-3 Clause 2.1 Table 2.1)",
    "Verification checks capacity against demand at each considered limit state."
)

# Table 3.1
knowledge_levels_and_confidence_factors = Table(
    ["Knowledge Level", "Geometry / Inspection", "Material testing / Documentation", r"Confidence Factor $CF$", "Permitted analysis methods"],
    [
        ["KL1 (Limited)", "Visual survey of critical elements and simulated design", "Limited in-situ tests (at least 1 per floor)", 1.35, "Linear static or multimode analysis only"],
        ["KL2 (Normal)", "Full structural survey and original design drawings", "Normal testing (at least 2 per floor/component)", 1.20, "Linear and non-linear analysis"],
        ["KL3 (Full)", "Comprehensive drawings, details, and site verification", "Comprehensive testing (at least 3 per floor/component)", 1.00, "All linear and non-linear methods"]
    ],
    "Knowledge Levels (KL) and corresponding Confidence Factors CF (EN 1998-3 Clause 3.3 Table 3.1)",
    "Design property f_d = f_mean / (CF * gamma_M)."
)

# Table 5.1
drift_limits_for_unreinforced_masonry_walls_in_assessment = Table(
    ["Failure mechanism in masonry pier", "Limit State DL (Damage Limitation)", "Limit State SD (Significant Damage)", "Limit State NC (Near Collapse)"],
    [
        ["In-plane shear failure (diagonal cracking)", "0.15% drift", "0.30% drift", "0.40% drift"],
        ["In-plane flexural rocking failure", "0.20% drift", "0.60% drift", "0.80% drift"],
        ["Out-of-plane flexural failure", "0.10% drift", "0.30% drift", "0.50% drift"]
    ],
    "Interstorey drift capacity limits for unreinforced masonry walls in seismic assessment (EN 1998-3 Annex C Table C.1)",
    "Drift ratio is relative horizontal displacement divided by pier height."
)
