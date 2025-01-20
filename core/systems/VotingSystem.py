from typing import List


VOTING_SYSTEMS = {
    "plurality": "Plurality",   # Implemented
    "majority": "Majority",     # Implemented
    "borda": "Borda",           # Implemented
    "approval": "Approval",     # Implemented
    "range": "Range",           # Implemented

    "ranked": "Ranked",         # Implementing
    "condorcet": "Condorcet",   # Implementing
    "instant-runoff": "Instant Runoff",     # Implemented
    "single-transferable-vote": "Single Transferable Vote",     # Find out how to implement
    "mixed-member-proportional": "Mixed Member Proportional"    # Find out how to implement
}
class Voting:

    def __init__(self, candidates: List[str], default_voting_system: str = "plurality"):
        self._candidates = candidates
        self._default_voting_system = default_voting_system

    @property
    def candidates(self):
        return self._candidates

    def add_candidate(self, candidate: str):
        self._candidates.append(candidate)

    def remove_candidate(self, candidate: str):
        self._candidates.remove(candidate)

    def set_voting_system(self, system: str):
        self._default_voting_system = system
