import math

a = float(input("Quadratic term: "))
b = float(input("Linear term: "))
c = float(input("Constant term: "))

x1, x2 = 0, 0
isTrue = True

D = b * b - 4 * a * c

if a == 0:
    x1 = - c / b
elif D >= 0:
    x1 = - b + math.sqrt(D) / (2 * a)
    x2 = - b - math.sqrt(D) / (2 * a)
else:
    isTrue = False

if a >= 0 and b >= 0 and c >= 0:
    eq = f'{a}x^2 + {b}x + {c} = 0'
elif a >= 0 >= c and b >= 0:
    eq = f'{a}x^2 + {b}x - {-c} = 0'
elif a >= 0 and b <= 0 <= c:
    eq = f'{a}x^2 - {-b}x + {c} = 0'
elif a <= 0 <= c and b >= 0:
    eq = f'-{-a}x^2 + {b}x + {c} = 0'
elif a >= 0 >= c and b <= 0:
    eq = f'{a}x^2 - {-b}x + {-c} = 0'
elif a <= 0 and b >= 0 >= c:
    eq = f'-{-a}x^2 + {b}x - {-c} = 0'
elif a <= 0 <= c and b <= 0:
    eq = f'-{-a}x^2 - {-b}x + {c} = 0'
elif a <= 0 and b <= 0 and c <= 0:
    eq = f'-{-a}x^2 - {-b}x - {-c} = 0'

if isTrue and D > 0:
    print(f"The equation {eq} has two roots: x1 = {x1:.2f} and x2 = {x2:.2f}")
elif isTrue and D == 0:
    print(f"The equation {eq} has a double root: x1 = x2 = {x1:.2f}")
else:
    print(f"The equation {eq} has no real roots.")
