def with_index(iterable, start=0):
    for i, item in enumerate(iterable, start):
        yield i, item


names = ['Fadi', 'Tymofii', 'Gandalf']
for i, names in with_index(names, 1):
    print(i, names)
