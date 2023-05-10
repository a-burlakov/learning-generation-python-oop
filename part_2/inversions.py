def inversions(seq: list[int]):

    # Втупую через O(n^2).
    inversions_count = 0
    for i, num_i in enumerate(seq):
        for j, num_j in enumerate(seq[i + 1 :]):
            if num_i > num_j:
                inversions_count += 1

    return inversions_count


sequence = [3, 1, 4, 2]

print(inversions(sequence))
