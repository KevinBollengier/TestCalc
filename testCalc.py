import fileinput

def main():
    lines = []
    for line in fileinput.input():
        lines.append(line)
    getal1 = lines[0]
    getal2 = lines[1]

    # g1, g2 = [int(line) for line in fileinput.input()]
    calc(int(getal1), int(getal2))


def calc(getal1: int, getal2: int):
    total = getal1 + getal2
    print(total)


if __name__ == '__main__':
    main()
