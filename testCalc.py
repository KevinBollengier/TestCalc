def main():
    getal1 = input("Input number 1: ...")
    getal2 = input("Input number 2: ...")
    calc(int(getal1), int(getal2))


def calc(getal1: int, getal2: int):
    total = getal1 + getal2
    print(total)


if __name__ == '__main__':
    main()
