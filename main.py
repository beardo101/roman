import roman


def roman_convert():
    number = input("Please type your number to covert it to or from Roman numerals: ")

    try:
        number = int(number)
    except ValueError:
        number = number.upper()

    if isinstance(number, int):
        s = roman.toRoman(number)
        print(s)
    else:
        i = roman.fromRoman(number)
        print(i)


if __name__ == "__main__":
    roman_convert()
