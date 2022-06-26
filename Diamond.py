print("Welcome to my diamond printing programme!!", "\n")
rows = int(input("Enter the number of rows for pyramid: "))

a = range(0, rows)
b = reversed(range(0, rows))
c = range(0, rows)
d = reversed(range(0, rows))

for x in a:
    for y in b:
        print(" " * (y+y), end="")
        y -= 1
        print("* " * (x+x+1))
        x += 1
for j in c:
    for i in d:
        print(" " * (j+j), end="")
        j += 1
        print("* " * (i+i+1))
        i -= 1