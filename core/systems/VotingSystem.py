from typing import List


class Voting:
    VOTING_SYSTEMS = {
        "plurality": "Plurality",
        "majority": "Majority",
        "borda": "Borda",
        "approval": "Approval",
        "range": "Range",
        "ranked": "Ranked",
        "condorcet": "Condorcet",
        "instant-runoff": "Instant Runoff",
        "single-transferable-vote": "Single Transferable Vote",
        "mixed-member-proportional": "Mixed Member Proportional"
    }

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
