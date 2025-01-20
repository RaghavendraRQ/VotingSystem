from typing import List
import logging
from core.components.ballot import Ballot

logger = logging.getLogger('system.plurality')


class Plurality:
    """
    Definition: The candidate with the most votes wins, even if they don't have a majority (>50%).\n
    Use Case: Common in single-member districts.\n
    Advantages: Simple to understand and implement.\n
    Disadvantages: Can lead to minority rule.

    """

    def __init__(self, ballots: List[Ballot] | None = None):
        self._ballots: List[Ballot] = ballots or []

        # Cross-reference the ballots to get the candidates
        if self._ballots:   # If ballots are provided
            self._candidates: List[str] = self._ballots[0].candidates
            self._vote_counts: dict = {candidate: 0 for candidate in self._candidates}
        else:
            self._candidates = []
            self._vote_counts = {}

    @property
    def ballots(self):
        return self._ballots

    @property
    def vote_counts(self):
        return self._vote_counts

    def get_winner(self) -> str | None:
        """
        Get the winner of the election.
        Returns:
            The candidate with the most votes.
        """
        self._validate_ballots()
        self._count_votes()

        winner = max(self._vote_counts, key=self._vote_counts.get)
        if list(self._vote_counts.values()).count(self._vote_counts[winner]) > 1:
            logger.warning(f"No clear winner. {self._vote_counts.get(winner)}.")
            return None
        return winner

    def _count_votes(self) -> dict:
        """
        Count the votes for each candidate.
        Returns:
            A dictionary of candidates and their vote counts.
        """
        self._validate_ballots()

        for ballot in self._ballots:
            self._vote_counts[ballot.most_preferred()] += 1
        return self._vote_counts

    def add_ballot(self, ballot: Ballot) -> bool:
        """
        Add a ballot to the system.
        Args:
            ballot: A Ballot object.

        Returns:
            True if the ballot was added.
        """
        # Check if it is the first ballot
        if not self._candidates:
            self._initialize_system(ballot)
            return True

        # Check if the ballot has the same candidates
        if ballot.candidates != self._candidates:
            raise ValueError("Ballot does not match system candidates.")

        self._ballots.append(ballot)
        self._vote_counts = self._count_votes()
        return True

    def _validate_ballots(self):
        if not self._ballots:
            raise ValueError("No ballots to count.")
        return True

    def _initialize_system(self, ballot: Ballot):
        self._candidates = ballot.candidates
        self._vote_counts = {candidate: 0 for candidate in self._candidates}
        self._ballots.append(ballot)
        self._vote_counts = self._count_votes()
