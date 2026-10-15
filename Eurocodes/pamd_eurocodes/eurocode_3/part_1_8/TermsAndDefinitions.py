try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

# Section 1.4 Terms and definitions used in EN 1993-1-8 (Design of joints)

Connection = TAD(
    "connection",
    "Location at which two or more elements meet. In a connection, fasteners or welds transmit forces between elements."
)

Joint = TAD(
    "joint",
    "Zone where two or more members are interconnected, consisting of the connection and the corresponding web panels or stiffeners."
)

JointConfiguration = TAD(
    "joint configuration",
    "Type of joint defined by member geometry, arrangement of fasteners, and stiffening elements."
)

RotationalStiffness = TAD(
    "rotational stiffness",
    "The moment required to produce unit rotation in a joint."
)

MomentResistance = TAD(
    "moment resistance",
    "The maximum design bending moment that a joint can resist."
)

ColumnWebPanel = TAD(
    "column web panel",
    "The portion of a column web bounded by the tension and compression zones of a connected beam."
)

TStub = TAD(
    "T-stub",
    "An idealized T-shaped element consisting of a flange and a stem used in the component method to model the tension resistance of bolted joints."
)

GapJoint = TAD(
    "gap joint",
    "A lattice girder joint in which there is a positive physical gap between adjacent brace members at the face of the chord."
)

OverlapJoint = TAD(
    "overlap joint",
    "A lattice girder joint in which one brace member overlaps another at the face of the chord."
)
