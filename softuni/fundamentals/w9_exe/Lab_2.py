stock = input().split()
stock_dict = {}

for i in range(0, len(stock), 2):
    product = stock[i]
    quantity = int(stock[i+1])
    stock_dict[product] = quantity

products_search = input().split()

for j in products_search:
    if j in stock_dict.keys():
        print(f"We have {stock_dict[j]} of {j} left")
    else:
        print(f"Sorry, we don't have {j}")