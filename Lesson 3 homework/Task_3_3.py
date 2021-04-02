b = input("Enter any number ")
b = int(b)
c = 0
while b > 0:
    b //= 2
    print(b)
    c += 1

print("And how many times has the entered number been divided by 2?", str(c) + " times the entered number was divided "
                                                                               "by 2.", sep="\n")
