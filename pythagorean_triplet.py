def triplets_with_sum(number):
    output = []
    for a in range(1, number // 3 + 1):
        for b in range(a, (number - a) // 2 + 1):
            c = number - a - b
            if a**2 + b**2 == c**2:
                output.append([a, b, c])
    return output
