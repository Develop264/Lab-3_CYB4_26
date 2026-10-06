n = int(input("Enter n: "))

ascending = True
descending = True
previous = int(input("Enter number: "))

for i in range(1, n):
    current = int(input("Enter number: "))

    if current <= previous:
        ascending = False
    if current >= previous:
        descending = False

    previous = current

if n > 1 and ascending:
    print("ascending sequence")
elif n > 1 and descending:
    print("descending sequence")
else:
    print("neither ascending nor descending sequence")
