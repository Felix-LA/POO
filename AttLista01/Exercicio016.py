def mediaFloats(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)


print(mediaFloats(2.5, 3.5, 4.0))