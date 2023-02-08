# Make a list that contains all integers from 1 to 100,
# then find all integers from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list.
# Finally, print the list.
# Constraint: use only while loop for iteration

list_1 = []
for x in range(1, 101):
    if x % 7 == 0 and x % 5 != 0:
        list_1.append(x)
print(list_1)

c = 0
list_2 = []
while c < 100:
    if c % 7 == 0 and c % 5 != 0:
        list_2.append(c)
    c += 1

print(list_2)

start_list = list(range(1,101))
c = 1
list_3 = []
while c < len(start_list):
    if c % 7 == 0 and c % 5 != 0:
        list_3.append(c)
    c += 1

print(list_3)

