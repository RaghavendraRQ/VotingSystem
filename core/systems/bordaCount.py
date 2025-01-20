from typing import List

from core.components.ballot import Ballot


class BordaCount:
    """
    Definition: Voters rank candidates. Points are assigned based on rank (e.g., 1st = N**2 points, 2nd = N-1**2 points, etc.), and the candidate with the highest total wins.\n
    Use Case: Decision-making in small groups or organizations.\n
    Advantages: Considers voters' preferences more comprehensively\n
    """

    def __init__(self, ballots: List[Ballot], borda_values: List[int] | None = None):
        self._ballots = ballots
        self._candidates = self._ballots[0].candidates
        self._borda_values = borda_values or self._calculate_borda_values()
        self._results = {}

    @property
    def borda_values(self):
        return self._borda_values

    def calculate_results(self):
        """
        Calculate the Borda count results.
        Returns:
            A dictionary of candidates and their Borda count.
        """
        self._results = {candidate: 0 for candidate in self._candidates}
        for ballot in self._ballots:
            for candidate, rank in ballot.get_ranking.items():
                self._results[candidate] += self._borda_values[rank]
        return self._results

    def get_winner(self):
        """
        Get the winner of the election.
        Returns:
            The candidate with the most votes.
        """
        if not self._results:
            self.calculate_results()
        winner = max(self._results, key=self._results.get)
        return winner

    def _calculate_borda_values(self):
        # Calculate the Borda values
        # The Borda value for the first index is 0. Never accessed.
        # Next index is squared.
        # Example: [0, n**2, n-1**2,  ..., 9, 4, 2, 1 ]
        return [0] + [i ** 2 for i in range(len(self._candidates), 0, -1)]
