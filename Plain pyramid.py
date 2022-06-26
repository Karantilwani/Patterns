print("Welcome to my pattern printing programme!!", "\n")
rows = int(input("Enter the number of rows for pyramid: "))

a = range(0, rows)
b = reversed(range(0, rows))

for x in a:
    for y in b:
        print(" " * (y+y), end="")
        y -= 1
        print("* " * (x+x+1))
        x += 1
