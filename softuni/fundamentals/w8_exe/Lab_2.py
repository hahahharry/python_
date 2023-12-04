class Party:
    def __init__(self):
        self.people = []

party = Party()

cmd = input()
while cmd != "End":
    party.people.append(cmd)
    cmd = input()

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")