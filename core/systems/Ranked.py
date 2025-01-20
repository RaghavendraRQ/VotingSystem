from core.components.ballot import Ballot

class Ranked:
    """
    Definition: Voters rank candidates in order of preference. The candidate with the most first-place votes wins.\n
    Use Case: Some academic and organizational elections.\n
    Advantages: Allows voters to express their preferences more accurately.\n
    Disadvantages: Can be more complex to implement and understand.
    """

    def __init__(self, ballots: list[Ballot]):
        self._ballots = ballots
        self._candidates = self._ballots[0].candidates
        self._vote_counts = {candidate: 0 for candidate in self._candidates}

    @property
    def ballots(self):
        return self._ballots

    @property
    def vote_counts(self):
        return self._vote_counts

    def calculate_results(self):
        """
        Calculate the Range System results.
        Returns:
            A dictionary of candidates and their vote counts.
        """