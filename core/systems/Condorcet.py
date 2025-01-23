from itertools import pairwise

from core.components.ballot import Ballot

class Condorcet:
    """
    Definition: The Condorcet voting system determines the winner as the candidate who would win in every head-to-head match-up against other candidates.
    If no such candidate exists (due to cycles or ties), a Condorcet completion method is used to resolve the ambiguity \n
    Use Case: Some academic and organizational elections.\n
    Advantages: Ensures that the winner is preferred over all other candidates.\n
    Disadvantages: Can be more complex to implement and understand.\n
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

    def _pairwise_comparison(self, candidate1: str, candidate2: str):
        """
        Compare two candidates in a pairwise match-up.
        Args:
            candidate1: The first candidate.
            candidate2: The second candidate.
        Returns:
            The candidate who is preferred in the match-up.
        """
        candidate1_wins = 0
        candidate2_wins = 0
        for ballot in self._ballots:
            if ballot.is_preferred(candidate1, candidate2):
                candidate1_wins += 1
            else:
                candidate2_wins += 1

        if candidate1_wins > candidate2_wins:
            return candidate1
        return candidate2 if candidate2_wins > candidate1_wins else None

    def pairwise_matrix(self, display: bool = True):
        """
        Create a matrix of pairwise match-ups.

        Args:
            display (bool): If True, print the matrix. Default is True.

        Returns:
            A dictionary of dictionaries representing the match-ups.
        """
        if not self._candidates:
            raise ValueError("Candidates list is empty. Initialize the system with candidates.")

        pairwise_matrix = {}

        for candidate in self._candidates:
            pairwise_matrix[candidate] = {}
            for opponent in self._candidates:
                if candidate == opponent:
                    continue
                pairwise_matrix[candidate][opponent] = self._pairwise_comparison(candidate, opponent)

        if display:
            print("\nPairwise Matrix:")
            print("-" * (len(self._candidates) * 20))
            for candidate, match_ups in pairwise_matrix.items():
                formatted_matchups = ", ".join(
                    f"{opponent}: {votes}" for opponent, votes in match_ups.items()
                )
                print(f"{candidate} --> {formatted_matchups}")
            print("-" * (len(self._candidates) * 20))

        return pairwise_matrix

    def get_winner(self) -> str | None:
        """
        Determine the Condorcet winner.

        Returns:
            The name of the Condorcet winner if one exists, else None.
        """
        pairwise_matrix = self.pairwise_matrix(display=False)

        for candidate in self._candidates:
            is_winner = True

            for opponent in self._candidates:
                if candidate == opponent:
                    continue
                if pairwise_matrix[candidate][opponent] != candidate:
                    is_winner = False
                    break
            if is_winner:
                return candidate

        return None

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