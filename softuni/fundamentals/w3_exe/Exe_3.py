cmd = input()
flt_cmd = cmd.split(" ")
team_a = team_b = 11
team_a_sentoff = []
team_b_sentoff = []

for i in range(len(flt_cmd)):
    if "A" in flt_cmd[i]:
        if flt_cmd[i] not in team_a_sentoff:
            team_a_sentoff.append(flt_cmd[i])
            team_a -= 1
        else:
            continue
    elif "B" in flt_cmd[i]:
        if flt_cmd[i] not in team_b_sentoff:
            team_b_sentoff.append(flt_cmd[i])
            team_b -= 1
        else:
            continue

if team_a < 7:
    print(f"Team A - {team_a}; Team B - {team_b}")
    print("Game was terminated")
elif team_b < 7:
    print(f"Team A - {team_a}; Team B - {team_b}")
    print("Game was terminated")
else:
    print(f"Team A - {team_a}; Team B - {team_b}")