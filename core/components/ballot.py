from typing import List, Dict, Optional


class Ballot:
    def __init__(self, candidates: List[str], voter_id: str):
        self._candidates: List[str] = candidates
        self._voter_id: str = voter_id
        self._ballot_results: Dict[str, Optional[int]] = {
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
        for candidate in ranking.keys():
            self._validate_candidate(candidate)

        unranked_candidates = set(self._candidates) - set(ranking.keys())
        unranked_start_rank = max(ranking.values(), default=0) + 1

        for idx, candidate in enumerate(unranked_candidates):
            ranking[candidate] = unranked_start_rank + idx

        self._validate_ranks(ranking)
        self._ballot_results.update(ranking)
        return True

    def most_preferred(self) -> str:
        """
        Get the most preferred candidate.
        Returns:
            The most preferred candidate.
        """
        if None in self._ballot_results.values():
            raise ValueError("Ballot is incomplete.")
        return min(self._ballot_results, key=self._ballot_results.get)

    def preferred_n(self, n: int) -> str:
        """
        Get the nth most preferred candidate.
        Args:
            n: The rank of the candidate.

        Returns:
            The nth most preferred candidate.
        """
        if None in self._ballot_results.values():
            raise ValueError("Ballot is incomplete.")
        return sorted(self._ballot_results, key=self._ballot_results.get)[n - 1]

    def _validate_candidate(self, candidate: str):
        if candidate not in self._candidates:
            raise ValueError(f"{candidate} is not a valid candidate.")
        return True

    def _validate_ranks(self, ranking: Dict[str, int]):
        expected_ranks = set(range(1, len(self._candidates) + 1))
        actual_ranks = set(ranking.values())
        if len(ranking) != len(self._candidates):
            raise ValueError(f"Expected {len(self._candidates)} ranks but got {len(ranking)}.")
        if actual_ranks != expected_ranks:
            raise ValueError(f"Invalid ranking values. Expected ranks {expected_ranks}, but got {actual_ranks}.")

    def __repr__(self):
        return f"Ballot({self._voter_id})"

    def is_preferred(self, candidate1, candidate2):
        """
        Check if candidate1 is preferred over candidate2.
        Args:
            candidate1: The first candidate.
            candidate2: The second candidate.
        Returns:
            True if candidate1 is preferred.
        """
        return self._ballot_results[candidate1] < self._ballot_results[candidate2]
