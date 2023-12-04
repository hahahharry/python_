# num = int(input())
# check = "is pure."
#
# for _ in range(num):
#     text = input()
#
#     if "," in text or "." in text or "_" in text:
#         check = "is not pure!"
#
#     print(f"{text} {check}")

num = int(input())

for _ in range(num):
    text = input()

    if "," in text or "." in text or "_" in text:
        print(f"{text} is not pure!")
    else:
        print(f"{text} is pure.")