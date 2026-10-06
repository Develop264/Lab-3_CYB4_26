x = int(input("Enter x: "))
y = int(input("Enter y: "))

while y != 0:
    r = x % y
    x = y
    y = r

print(x)
