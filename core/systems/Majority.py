from core.components.ballot import Ballot


class Majority:
    """
    Definition: A candidate must receive more than 50% of the votes to win.\n
    Use Case: Common in multi-member districts.\n
    Advantages: Ensures the winner has broad support.\n
    Disadvantages: Can be costly and time-consuming.
    """

    def __init__(self, ballots: list[Ballot] | None = None):
        self._ballots = ballots or []
        self._candidates = self._ballots[0].candidates if self._ballots else []
        self._vote_counts = {
            candidate: 0 for candidate in self._candidates
        }



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

    def calculate_result(self):
        """
        Calculate the Majority System results.
        Returns:
            A dictionary of candidates and their vote counts.
        """
        for ballot in self._ballots:
            self._vote_counts[ballot.most_preferred()] += 1
        return self._vote_counts

    def get_winner(self):
        """
        Get the winner of the election.
        Returns:
            The candidate with the most votes.
        """
        if not self._vote_counts:
            self.calculate_result()
        total_votes = sum(self._vote_counts.values())
        # TODO: Handle edge case where no candidate has more than 50% of the votes
        for candidate, votes in self._vote_counts.items():
            if votes > total_votes / 2:
                return candidate
        print(f'\033[91mNo candidate has more than 50% of the votes.\033[0m')
        return None     # No candidate has more than 50% of the votes
