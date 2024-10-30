#asking user ofr input
x = int(input("Please enter a number: "))

#checking if the number is divisible by 3 and 5, if so it will print it
for i in range(1, x):
    if i % 3 == 0 and i % 5 == 0:
        print(i)