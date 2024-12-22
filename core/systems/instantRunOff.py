from typing import List

from core.components.ballot import Ballot


class InstantRunOff:
    def __init__(self, ballots: List[Ballot]):
        self._ballots = ballots
        self._vote_counts = None
        self._vote_storage = _VoteStorage(ballots)

    @property
    def ballots(self):
        return self._ballots

    @property
    def vote_counts(self):
        return self._vote_counts

    def _calculate_vote_counts(self) -> dict:
        """
        Count the votes for each candidate.
        Returns:
            A dictionary of candidates and their vote counts.
        """
        self._vote_counts = {candidate: 0 for candidate in self._ballots[0].candidates}

        for ballot in self._ballots:
            self._vote_counts[ballot.most_preferred()] += 1
        return self._vote_counts

    def _round_off(self) -> str:
        """
        Conduct a round of voting.
        eliminate the candidate with the least votes and redistribute the votes.

        Returns:
            The candidate with the least votes.
        """

        # Get the candidate with the least votes
        loser = min(self._vote_counts, key=self._vote_counts.get)
        print(f'Loser: {loser}')

        loser_n_preferred = self._vote_storage.get_ballot_n_preferred(loser, 1)

        for ballot_id in loser_n_preferred:
            self._vote_counts[self._vote_storage.get_n_preferred(ballot_id, 2)] += 1

        self._vote_storage.eliminate_candidate(loser)
        self._vote_counts.pop(loser)
        pass

    def get_winner(self) -> str:
        """
        Get the winner of the election.
        Returns:
            The candidate with the most votes.
        """
        self._calculate_vote_counts()
        while len(self._vote_counts) > 1:
            self._round_off()

        return list(self._vote_counts.keys())[0]


class _VoteStorage:

    def __init__(self, ballots: List[Ballot]):
        self._ballots = {ballot.voter_id: list(ballot.sort_ranking().values()) for ballot in ballots}

    @property
    def ballots(self):
        return self._ballots

    def get(self, ballot_id: str) -> List[str]:
        """
        Get the votes for a ballot.
        Args:
            ballot_id: The id of the ballot.

        Returns:
            The votes.
        """
        return self._ballots[ballot_id]

    def get_ballot_n_preferred(self, candidate: str, n: int) -> List[str]:
        """
        Get the nth most preferred ballots for a candidate.
        Args:
            candidate: The candidate.
            n: The rank of the candidate.

        Returns:
            The ballots.
        """
        return [ballot_id for ballot_id, ranking in self._ballots.items() if ranking[n - 1] == candidate]

    def get_n_preferred(self, ballot_id: str, n: int) -> str:
        """
        Get the nth most preferred candidate for a ballot.
        Args:
            ballot_id: The id of the ballot.
            n: The rank of the candidate.

        Returns:
            The candidate.
        """
        return self._ballots[ballot_id][n - 1]

    def eliminate_candidate(self, candidate: str):
        """
        Eliminate a candidate from the ballots.
        Args:
            candidate: The candidate to eliminate.
        """
        for ballot in self._ballots.values():
            if candidate in ballot:
                ballot.remove(candidate)

    def __iter__(self):
        return iter(self._ballots)

    def __repr__(self):
        return f'{self._ballots}'
