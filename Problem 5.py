numbers = [20, 36, 12, 24, 20, 48, 74, 353, 23, 98]
print(numbers)
for i in range(len(numbers)):
    if numbers[i] == 353:
        numbers[i] = 53

print(numbers)
