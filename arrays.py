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



#linearsearch

a = [4, 9, 15, 22, 31]
target = 22
found = false
for number in a:
    if number==target:
        found=true
        break
if found:
    print("element found")
else:
    print("element not found")


#reversearray
a = [10, 20, 30, 40, 50]
reversed_a = []
for i in range(len(a) - 1, -1, -1):
    reversed_a.append(a[i])
print(reversed_a)


#secondlargest

a = [10, 25, 7, 42, 18, 31]

largest = a[0]
second_largest = a[0]
for number in a:
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest:
        second_largest = number
print("Second largest:", second_largest)
