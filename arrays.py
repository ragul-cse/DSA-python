numbers = [10, 20, 30, 40, 50]
print("arrays:", numbers)
print("first element:", numbers[0])
print("last element:", numbers[-1])
print("length:", len(numbers))


numbers = [10, 25, 7, 42, 18, 31]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest number:", largest)
