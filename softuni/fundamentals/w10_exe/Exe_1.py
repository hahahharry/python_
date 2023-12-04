def f1(un):
    if 3 <= len(un) <= 16:
        return True
    return False

def f2(un):
    for chars in un:
        if not (chars.isalnum() or chars == "-" or chars == "_"):
            return False
    return True

def f3(un):
    if " " in un:
        return False
    return True

def f_final(un):
    if f1(un) and f2(un) and f3(un):
        return True
    return False

usernames = input().split(", ")
for i in usernames:
    if f_final(i):
        print(i)



