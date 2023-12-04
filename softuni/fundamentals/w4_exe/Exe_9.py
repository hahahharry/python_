def pass_checker(login):
    check_1, check_2, check_3 = False, False, False
    if 6 <= len(login) <= 10:
        check_1 = True

    if login.isalnum():
        check_2 = True

    digit_count = 0
    for k in login:
        if k.isdigit():
            digit_count += 1
        if digit_count >= 2:
            check_3 = True

    result = ""
    if check_1 and check_2 and check_3:
        result += "Password is valid"
    else:
        if not check_1:
            result += "Password must be between 6 and 10 characters"
        if not check_2:
            if check_1:
                result += "Password must consist only of letters and digits"
            else:
                result += "\nPassword must consist only of letters and digits"
        if not check_3:
            if check_1 or check_2:
                result += "Password must have at least 2 digits"
            else:
                result += "\nPassword must have at least 2 digits"
    return result

pass_input = input()
print(pass_checker(pass_input))
