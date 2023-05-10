def darts():

    size = int(input())

    darts_desk = ""
    for i in range(size):
        for j in range(size):
            # Расчёт двух расстояний от края матрицы:
            # 1) на основании размера матрицы и максимального индекса ячейки;
            # 2) на основании минимального индекса ячейки.
            # Минимальное из этих расстояний - и есть расстояние от края матрицы.
            side_distance_1 = size - max(i, j)
            side_distance_2 = min(i, j) + 1
            darts_desk += " " + f"{min(side_distance_1, side_distance_2)}"
        darts_desk += "\n"

    print(darts_desk)


darts()
