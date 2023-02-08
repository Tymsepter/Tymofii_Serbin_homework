# Use a list comprehension to make a list containing tuples (i, j)
# where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.

list_1 = []

i = tuple(range(1, 11))
for j in i:
    j = (j, j ** 2)
    list_1.append(j)
print(list_1)
new_list = [m := (j, j ** 2) for j in i]
print(new_list)
