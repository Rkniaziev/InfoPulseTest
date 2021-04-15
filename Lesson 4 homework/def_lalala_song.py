def lalala_song(lalastring=3, count=3, end=False):
    if end:
        return "{}!".format(((("la " * count).rstrip("-") + " ") * lalastring).rstrip(" "))
    else:
        return "{}.".format(((("la " * count).rstrip("-") + " ") * lalastring).rstrip(" "))


if __name__ == "__main__":
    print(lalala_song(4, 4, 0))
