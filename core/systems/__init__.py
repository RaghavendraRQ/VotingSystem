from core.systems.Approval import Approval
from core.systems.BordaCount import BordaCount
from core.systems.InstantRunOff import InstantRunOff
from core.systems.Majority import Majority
from core.systems.Plurality import Plurality
from core.systems.Range import Range
from core.systems.Ranked import Ranked
from core.systems.Condorcet import Condorcet


candidates = ["Alice", "Bob", "Charlie"]
__all__ = ["Approval", "BordaCount", "InstantRunOff", "Majority", "Plurality", "candidates", "Range", "Ranked", "Condorcet"]