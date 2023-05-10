def is_fraction(string: str):

    if not string:
        return False

    if string[0] == "-":
        string = string[1:]

    if "/" not in string:
        return False

    numbers = string.split("/")
    if len(numbers) != 2:
        return False

    numerator, denominator = numbers

    if (
        not numerator.isdigit()
        or not denominator.isdigit()
        or denominator == "0"
        or "-" in denominator
    ):
        return False

    return True


print(is_fraction("-54/9"))
