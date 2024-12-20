from core.components.ballot import Ballot
from core.systems.plurality import Plurality

candidates = ["Alice", "Bob", "Charlie"]

ballot1 = Ballot(candidates, "voter1")
ballot2 = Ballot(candidates, "voter2")
ballot3 = Ballot(candidates, "voter3")

rankings1 = {"Alice": 1, "Bob": 2, "Charlie": 3}
rankings2 = {"Bob": 1, "Alice": 2, "Charlie": 3}
rankings3 = {"Charlie": 1, "Bob": 2, "Alice": 3}

ballot1.vote(rankings1)
ballot2.vote(rankings2)
ballot3.vote(rankings1)
print(f'Ballot 1: {ballot1.most_preferred()}')
print(f'Ballot 2: {ballot2.most_preferred()}')
print(f'Ballot 3: {ballot3.most_preferred()}')

system = Plurality()
# print(f'Vote Counts: {system.vote_counts}')
# print(f'Winner: {system.get_winner()}')
# Adding a ballot to the system

system.add_ballot(ballot3)

print(f'Vote Counts: {system.vote_counts}')
print(f'Winner: {system.get_winner()}')
