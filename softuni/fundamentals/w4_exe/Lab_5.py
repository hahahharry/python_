def cost(product, quantity):
    if product == "coffee":
        return f"{quantity * 1.5:.2f}"
    elif product == "coke":
        return f"{quantity * 1.4:.2f}"
    elif product == "water":
        return f"{quantity:.2f}"
    elif product == "snacks":
        return f"{quantity * 2:.2f}"

product_inp = input()
quantity_inp = int(input())
print(cost(product_inp, quantity_inp))