try:
    from tad import TAD
except ImportError:
    from pamd_eurocodes.tad import TAD

SelfweightOfCrane = TAD(
    "selfweight of the crane (Q_c)",
    "selfweight of all fixed and movable elements including mechanical and electrical equipment, without lifting attachment and portion of suspended hoist ropes"
)
Hoistload = TAD(
    "hoistload (Q_H)",
    "includes masses of payload, lifting attachment and portion of suspended hoist ropes or chains moved by crane structure"
)
Crab = TAD(
    "crab",
    "part of an overhead travelling crane that incorporates a hoist and is able to travel on rails on top of the crane bridge"
)
CraneBridge = TAD(
    "crane bridge",
    "part of an overhead travelling crane that spans between crane runway beams and supports the crab"
)
GuidanceMeans = TAD(
    "guidance means",
    "system used to keep a crane aligned on a runway, through horizontal reactions between crane and runway beams (wheel flanges or guide rollers)"
)
Hoist = TAD(
    "hoist",
    "machine for lifting loads"
)
HoistBlock = TAD(
    "hoist block",
    "underslung trolley that incorporates a hoist and travels on the bottom flange of a beam"
)
OverheadTravellingCrane = TAD(
    "overhead travelling crane",
    "machine for lifting and moving loads, moving on wheels along overhead crane runway beams"
)
NaturalFrequency = TAD(
    "natural frequency",
    "the frequency of free vibration on a system"
)
FreeVibration = TAD(
    "free vibration",
    "vibration of a system that occurs in the absence of forced vibration"
)
ForcedVibration = TAD(
    "forced vibration",
    "vibration of a system if the response is imposed by external time-varying excitation"
)
Damping = TAD(
    "damping",
    "dissipation of energy with time or distance in a vibrating system"
)
Resonance = TAD(
    "resonance",
    "condition in forced vibration when any change, however small, in frequency of excitation causes a decrease in response"
)
ModeOfVibration = TAD(
    "mode of vibration",
    "characteristic pattern assumed by a vibrating system in which motion of every particle is simple harmonic with the same frequency"
)
