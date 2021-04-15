def leap(x):
    if x % 4 != 0:
        return "False"
    elif x % 100 == 0:
        if x % 400 == 0:
            return "True"
        else:
            return "False"
    else:
        return "True"


if __name__ == "__main__":
    n = int(input("Enter the year to find out if it is a leap year: "))
    print(leap(int(n)))
