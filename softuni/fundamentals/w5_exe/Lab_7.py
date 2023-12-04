def happiness():
    happiness_list = list(map(int, input().split()))
    happiness_factor = int(input())
    improved_happiness = [happiness_factor * x for x in happiness_list]
    average_happiness = sum(improved_happiness) / len(improved_happiness)
    h_counter = sum(x >= average_happiness for x in improved_happiness)

    message = "happy" if h_counter >= len(improved_happiness) / 2 else "not happy"
    result= f"Score: {h_counter}/{len(improved_happiness)}. Employees are {message}!"
    return result

print(happiness())