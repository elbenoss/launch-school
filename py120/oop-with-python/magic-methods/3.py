# Challenge: Create the classes needed to make the following code work as shown:


class Candidate:

    def __init__(self, name):
        self._name = name
        self._votes = 0

    def __iadd__(self, other):
        self._votes += 1
        return self._votes

        


class Election:

    def __init__(self, candidates):
        self._result = []
        self._total_votes = 0
        for candidate in candidates:
            self._result.append(f"{candidate._name}: {candidate._votes}")
            self._total_votes += candidate._votes


    def results(self):
        print('\n'.join(self._result))
        print([x for x in self._result])
        print(f" _ won: {self._total_votes} of votes")





mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1


election = Election(candidates)
election.results()

"""
Mike Jones: 3 votes
Susan Dore: 4 votes
Kim Waters: 1 votes

Susan Dore won: 50.0% of votes
"""


# Don't worry about ties or whether votes should be singular.

