from typing import List, Dict


class Ballot:
    def __init__(self, candidates: List[str], voter_id: str):
        self._candidates: List[str] = candidates
        self._voter_id: str = voter_id
        self._ballot_results: Dict[str, int | None] = {
            candidate: None for candidate in candidates
        }

    @property
    def candidates(self):
        return self._candidates

    @property
    def voter_id(self):
        return self._voter_id

    @property
    def get_ranking(self) -> Dict[str, int | None]:
        return self._ballot_results

    def sort_ranking(self) -> Dict[int, str]:
        """
        Sort the ranking of candidates.
        Returns:
            A dictionary of ranks and corresponding candidates.
        """
        return {v: k for k, v in sorted(self._ballot_results.items(), key=lambda item: item[1])}

    def vote(self, ranking: Dict[str, int]) -> bool:
        """
        Vote for candidates in order of preference.
        Args:
            ranking: A dictionary of candidates and their rank.

        Returns:
            True if the vote was successful.
        """
        self._validate_ranks(ranking)

        for candidate, rank in ranking.items():
            if self._validate_candidate(candidate):
                self._ballot_results[candidate] = rank
            else:
                raise ValueError(f"{candidate} is not a valid candidate.")
        return True

    def most_preferred(self) -> str:
        """
        Get the most preferred candidate.
        Returns:
            The most preferred candidate.
        """
        return min(self._ballot_results, key=self._ballot_results.get)

    def preferred_n(self, n: int) -> str:
        """
        Get the nth most preferred candidate.
        Args:
            n: The rank of the candidate.

        Returns:
            The nth most preferred candidate.
        """
        return sorted(self._ballot_results, key=self._ballot_results.get)[n - 1]

    def _validate_candidate(self, candidate: str):
        if candidate not in self._candidates:
            raise ValueError(f"{candidate} is not a valid candidate.")
        return True

    def _validate_ranks(self, ranking: Dict[str, int]):
        if len(ranking) != len(self._candidates):
            raise ValueError("Ranking does not match number of candidates.")
        if set(ranking.values()) != set(range(1, len(self._candidates) + 1)):
            raise ValueError("Invalid ranking values.")
        return True

    def __repr__(self):
        return f"Ballot({self._voter_id})"
