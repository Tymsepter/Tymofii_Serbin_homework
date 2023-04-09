def in_range(start, end, step=1):
    result = []
    while start < end:
        result.append(start)
        start += step
    return result


even_numbers = in_range(0, 10, 2)
print(even_numbers)
