try:
    from table import Table
    from range import BRange
except ImportError:
    from pamd_eurocodes.table import Table
    from pamd_eurocodes.range import BRange

# Table 3.1
effective_width_factor_beta_for_shear_lag = Table(
    [r"Parameter $\kappa$", "Location / Verification", r"Effective width factor $\beta$"],
    [
        [r"$\kappa \le 0.02$", "Any location", 1.0],
        [r"$0.02 < \kappa \le 0.70$", "Sagging bending", r"$\beta_1 = 1 / (1 + 6.4 \kappa^2)$"],
        [r"$0.02 < \kappa \le 0.70$", "Hogging bending", r"$\beta_2 = 1 / (1 + 6.1 \kappa^2)$"],
        [r"$\kappa > 0.70$", "Sagging bending", r"$\beta_1 = 1 / (5.9 \kappa)$"],
        [r"$\kappa > 0.70$", "Hogging bending", r"$\beta_2 = 1 / (8.6 \kappa)$"],
        ["All kappa", "End support", r"$\beta_0 = (0.55 + 0.025 / \kappa) \beta_1 \le \beta_1$"],
        ["All kappa", "Cantilever", r"$\beta = \beta_2$ at support and at end"]
    ],
    "Effective width factor beta for shear lag",
    "kappa = alpha_0 * b_0 / Le, where alpha_0 = sqrt(1 + Asl / (b0 * t))."
)

# Table 4.1
buckling_factor_k_sigma_internal_compression_elements = Table(
    ["Stress ratio psi", r"Buckling factor $k_\sigma$"],
    [
        ["1.0 (uniform compression)", 4.0],
        ["0.0 (pure bending)", 7.81],
        ["-1.0 (pure bending across depth)", 23.9],
        ["1 > psi > 0", r"$8.2 / (1.05 + \psi)$"],
        ["0 > psi > -1", r"$7.81 - 6.29 \psi + 9.78 \psi^2$"],
        [r"$\psi < -1$", r"$5.98 (1 - \psi)^2$"]
    ],
    "Buckling factor k_sigma for internal compression elements",
    "psi = sigma2 / sigma1 is the ratio of edge stresses."
)

# Table 4.2
buckling_factor_k_sigma_outstand_compression_elements = Table(
    ["Stress ratio psi", r"Buckling factor $k_\sigma$"],
    [
        ["1.0 (uniform compression)", 0.43],
        ["0.0", 0.57],
        ["-1.0", 0.85],
        ["1 > psi > 0", r"$0.57 - 0.21 \psi + 0.07 \psi^2$"],
        ["0 > psi > -1", r"$0.57 - 0.21 \psi + 0.07 \psi^2$"]
    ],
    "Buckling factor k_sigma for outstand compression elements",
    "Applies to outstand flanges and stiffener outstands."
)

# Table 5.1
shear_buckling_coefficient_k_tau = Table(
    ["Stiffener arrangement", "Aspect ratio a/hw", r"Shear buckling coefficient $k_\tau$"],
    [
        ["Plates with rigid transverse stiffeners only", r"$a/h_w \ge 1$", r"$5.34 + 4.00 / (a/h_w)^2$"],
        ["Plates with rigid transverse stiffeners only", r"$a/h_w < 1$", r"$4.00 + 5.34 / (a/h_w)^2$"],
        ["Plates with longitudinal stiffeners", r"$a/h_w \ge 3$", r"$5.34 + 4.00 / (a/h_w)^2 + k_{\tau st}$"],
        ["Plates with longitudinal stiffeners", r"$a/h_w < 3$", r"$4.00 + 5.34 / (a/h_w)^2 + k_{\tau st}$"]
    ],
    "Shear buckling coefficient k_tau for plated web panels",
    "a is the distance between transverse stiffeners, hw is the clear web depth."
)
