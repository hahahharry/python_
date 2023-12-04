countries = input().split(", ")
cities = input().split(", ")

#pairs = {countries[i]: cities[i] for i in range(len(countries))}

pairs_opt = dict(zip(countries, cities))

for k, v in pairs_opt.items():
    print(f"{k} -> {v}")

