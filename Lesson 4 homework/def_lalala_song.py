def lalala_song(lalastring=3, count=3, end=False):
    if end:
        return "{}!".format(((("la-" * count).rstrip("-") + "\n") * lalastring).rstrip("\n"))
    else:
        return "{}.".format(((("la-" * count).rstrip("-") + "\n") * lalastring).rstrip("\n"))


if __name__ == "__main__":
    print(lalala_song(4, 4, 0))
