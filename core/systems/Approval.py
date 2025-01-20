from typing import List
from core.components.ballot import Ballot


class Approval:
    """
    Definition: Voters approve or disapprove of each candidate. The candidate with the most approvals wins.\n
    Use Case: Some academic and organizational elections.\n
    Advantages: Simple and allows support for multiple candidates.\n
    Disadvantages: Can lead to strategic voting.
    """

    def __init__(self, ballots: List[Ballot]):
        self._ballots = ballots
        self._candidates = self._ballots[0].candidates
        self._vote_counts = {}

    @property
    def ballots(self):
        return self._ballots

    @property
    def vote_counts(self):
        return self._vote_counts

    def calculate_results(self):
        """
        Calculate the Approval System results.
        Returns:
            A dictionary of candidates and their vote counts.
        """
        self._vote_counts = {candidate: 0 for candidate in self._candidates}
        for ballot in self._ballots:
            for candidate in ballot.get_ranking:
                self._vote_counts[candidate] += 1
        return self._vote_counts

    def get_winner(self):
        """
        Get the winner of the election.
        Returns:
            The candidate with the most votes.
        """
        if not self._vote_counts:
            self.calculate_results()
        winner = max(self._vote_counts, key=self._vote_counts.get)
        return winner

    def add_ballot(self, ballot: Ballot):
        """
        Add a ballot to the system.
        Args:
            ballot: A Ballot object.
        """
        if not self._candidates:
            self._candidates = ballot.candidates
            self._vote_counts = {candidate: 0 for candidate in self._candidates}
        self._ballots.append(ballot)
        return True

