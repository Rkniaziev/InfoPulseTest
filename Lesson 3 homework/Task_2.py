x = input("Enter text to see some magic: ")
if len(x) % 2 == 0:
    print(x[:(len(x)+1) // 2])
else:
    print(x[(len(x)+1) // 2:] + x[:(len(x) + 1) // 2])
