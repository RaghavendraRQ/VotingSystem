from core.components.ballot import Ballot
from core.systems import Approval, BordaCount, InstantRunOff, Majority, Plurality, Range, Ranked, Condorcet

candidates = ["Alice", "Bob", "Charlie"]

ballot1 = Ballot(candidates, "voter1")
ballot2 = Ballot(candidates, "voter2")
ballot3 = Ballot(candidates, "voter3")
ballot4 = Ballot(candidates, "voter4")
ballot5 = Ballot(candidates, "voter5")
ballot6 = Ballot(candidates, "voter6")

rankings1 = {"Alice": 1, "Bob": 3, "Charlie": 2}
rankings2 = {"Bob": 1, "Alice": 3, "Charlie": 2}
rankings3 = {"Charlie": 1, "Bob": 2, "Alice": 3}
rankings4 = {"Alice": 1, "Charlie": 2, "Bob": 3}
rankings5 = {"Bob": 1, "Charlie": 2, "Alice": 3}
rankings6 = {"Charlie": 1, "Alice": 2, "Bob": 3}


ballot1.vote(rankings1)
ballot2.vote(rankings1)
ballot3.vote(rankings3)
ballot4.vote(rankings4)
ballot5.vote(rankings5)
ballot6.vote(rankings6)


print(f'Ballot 1: {ballot1.sort_ranking()}')
print(f'Ballot 2: {ballot2.sort_ranking()}')
print(f'Ballot 3: {ballot3.sort_ranking()}')
print(f'Ballot 4: {ballot4.sort_ranking()}')
print(f'Ballot 5: {ballot5.sort_ranking()}')
print(f'Ballot 6: {ballot6.sort_ranking()}')

ballots = [ballot1, ballot2, ballot3, ballot4, ballot5, ballot6]

system = Plurality(ballots)
print(f'\033[32mWinner in Plurality: {system.get_winner()}')

system = InstantRunOff(ballots)
print(f'\033[32mWinner in InstantRunOff: {system.get_winner()}\033[0m')

system = BordaCount(ballots)
print(f'\033[32mResults in BordaCount: {system.get_winner()}\033[0m')

system = Approval(ballots)
print(f'\033[32mWinner in Approval: {system.get_winner()}\033[0m')

system = Majority(ballots)
print(f'\033[32mWinner in Majority: {system.get_winner()}\033[0m')

system = Range(ballots)
print(f'\033[32mWinner in Range: {system.get_winner()}\033[0m')

system = Ranked(ballots, "Instant Runoff")
print(f'\033[32mWinner in Ranked: {system.get_winner()}\033[0m')

system = Condorcet(ballots)
system.pairwise_matrix()
print(f'\033[32mWinner in Condorcet: {system.get_winner()}\033[0m')
