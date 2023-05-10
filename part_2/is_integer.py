def is_decimal(string: str):
    if string[0] == "-":
        string = string[1:]

    return string.isdecimal()


print(is_decimal("199.1"))
