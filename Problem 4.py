sentence = input("Please enter a sentence: ")
character = input("Please enter a character: ")


def check(a, b):
    count = 0
    for char in a:
        if b == char:
            count += 1
    print(count)


check(sentence, character)
