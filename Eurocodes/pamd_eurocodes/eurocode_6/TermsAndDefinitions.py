"""
Eurocode 6: Design of masonry structures - Terms and Definitions.
Re-exports terms and definitions from all parts of Eurocode 6.
"""
from .part_1_1 import TermsAndDefinitions as part_1_1
from .part_1_2 import TermsAndDefinitions as part_1_2
from .part_1_3 import TermsAndDefinitions as part_1_3
from .part_2 import TermsAndDefinitions as part_2
from .part_3 import TermsAndDefinitions as part_3

from .part_1_1.TermsAndDefinitions import *
from .part_1_2.TermsAndDefinitions import *
from .part_1_3.TermsAndDefinitions import *
from .part_2.TermsAndDefinitions import *
from .part_3.TermsAndDefinitions import *
