def correct_coordinates(coordinates: list[str]):

    float_coordinates = [tuple(c.strip("()").split(", ")) for c in coordinates]
    float_coordinates = [(float(x), float(y)) for x, y in float_coordinates]

    bools_list = []
    for x, y in float_coordinates:
        if not -90 <= x <= 90:
            bools_list.append(False)
        elif not -180 <= y <= 180:
            bools_list.append(False)
        else:
            bools_list.append(True)

    return bools_list


coordinates = [c.strip() for c in open(0)]


print(*correct_coordinates(coordinates), sep="\n")
