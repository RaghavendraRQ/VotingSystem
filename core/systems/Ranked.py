from core.components.ballot import Ballot
from core.systems import BordaCount, InstantRunOff

class Ranked:
    """
    Definition: Voters rank candidates in order of preference.
    The counting process depends on the specific ranked voting system used. Common methods include:\n
    Instant Runoff Voting \n
    Borda Count \n
    Condorcet Method \n
    Use Case: Some academic and organizational elections.\n
    Advantages: Allows voters to express their preferences more accurately.\n
    Disadvantages: Can be more complex to implement and understand.
    """

    def __init__(self, ballots: list[Ballot], method: str):
        self._ballots = ballots
        self._method = method
        self._candidates = self._ballots[0].candidates
        self._vote_counts = {candidate: 0 for candidate in self._candidates}

    @property
    def ballots(self):
        return self._ballots

    @property
    def vote_counts(self):
        return self._vote_counts

    def get_winner(self):
        if self._method == "Instant Runoff":
            system = InstantRunOff(self._ballots)
        else:
            system = BordaCount(self._ballots)
        return system.get_winner()
