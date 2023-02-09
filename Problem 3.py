sentence = input("Please enter your sentence: ")
count = 0
item = "e"
for char in sentence:
    if item == char:
        count += 1
print(count)


