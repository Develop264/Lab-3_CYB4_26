n = int(input("Enter n: "))

first = float(input("Enter number: "))
second = float(input("Enter number: "))

if first > second:
    largest = first
    second_largest = second
else:
    largest = second
    second_largest = first

for i in range(2, n):
    number = float(input("Enter number: "))

    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest:
        second_largest = number

print(largest, second_largest)
