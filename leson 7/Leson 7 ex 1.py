
# Порада: використай словник, де ключем буде слово, а значенням – кількість (скільки зустрічається в реченні).

# підраховуватиме слова та створюватиме словник де слова ключ а їх кількість це значення
list_1 = []
d = dict()
sentence = input("Print sentence:")
input_line = input("Enter a Line : ")
list_of_words = input_line.split()
for word in list_of_words:
    count[word] = count.get(word, 0) + 1
print('Word Frequency')
for key in count.keys():
    print(key, count[key])