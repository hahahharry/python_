number = int(input())
capacity = int(input())

courses = number//capacity
if number % capacity != 0:
    courses += 1
print(courses)