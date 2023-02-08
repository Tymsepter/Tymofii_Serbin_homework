def count_lines(name):
    with open(name, 'r') as file:
        lines = file.readlines()
    return len(lines)


def count_chars(name):
    with open(name, 'r') as file:
        chars = file.read()
    return len(chars)


def test(name):
    print("Number of lines:", count_lines(name))
    print("Number of characters:", count_chars(name))
