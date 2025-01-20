from core.components.ballot import Ballot

class Range:
    """
    Definition: Voters score each candidate on a scale. The candidate with the highest total score wins.\n
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
        for ballot in self._ballots:
            for candidate, score in ballot.get_ranking.items():
                self._vote_counts[candidate] += score
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