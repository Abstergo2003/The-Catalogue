try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Terms and definitions used in EN 1998-2 (Bridges)

SeismicIsolationBridge = TAD(
    "seismic isolation in bridges",
    "A design strategy providing a flexible horizontal interface (elastomeric or sliding bearings) between bridge superstructure and substructure to lengthen the fundamental period and shift the bridge into a lower spectral acceleration regime."
)

DuctileBridge = TAD(
    "ductile bridge behavior",
    "A seismic design concept where earthquake energy dissipation is concentrated in specific flexural plastic hinges located in accessible portions of the piers, while the superstructure and foundations remain essentially elastic."
)

LimitedDuctileBridge = TAD(
    "limited ductile bridge behavior",
    "A design concept for low seismicity or brittle substructures where a low behavior factor (q <= 1.5) is adopted and plastic mechanism formation is not relied upon."
)

BridgePierHinge = TAD(
    "plastic hinge in bridge pier",
    "A confined ductile region detailed with close-spaced transverse stirrups or spirals capable of sustaining extensive cyclic inelastic flexural rotations without shear failure or bar buckling."
)

UnseatingFailure = TAD(
    "unseating failure",
    "A catastrophic failure mechanism wherein the bridge deck slides off its pier or abutment support seat due to large longitudinal relative seismic displacements."
)

LeadRubberBearing = TAD(
    "lead-rubber bearing (LRB)",
    "A laminated elastomeric bearing incorporating a solid central lead cylinder that yields under lateral shear, providing substantial hysteretic energy damping."
)

ViscousDamper = TAD(
    "fluid viscous damper",
    "A hydraulic pistoned energy dissipation device generating resisting forces proportional to velocity to reduce peak earthquake displacements without increasing dead-load stiffness."
)
