def secondMaxArg(*numbers):
    numbers = list(numbers)
    numbers.sort()
    if numbers.count(numbers[-1]) == 1:
        return numbers[-2]
    else:
        return numbers[(numbers.index(numbers[-1]) - 1)]


if __name__ == "__main__":
    print(secondMaxArg(12, 23, 8888, 8888, 123, 9999, 23, 456, 9999, 9999))