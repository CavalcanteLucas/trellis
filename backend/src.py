from math import ceil


def translate(input: str) -> str:
    if not input:
        raise ValueError("Input number not detected!")
    if not input.isdigit():
        raise ValueError("Only positive integer numbers are allowed!")
    input = int(input)
    if input == 0:
        return "zero"
    if input > 999999999999999:
        raise ValueError("Input number is too high!")
    return process(str(input)).replace("  ", " ")


def process(input: str) -> str:
    one_digit_names = {
        "0": "",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
    }
    two_digit_names = {
        "10": "ten",
        "11": "eleven",
        "12": "twelve",
        "13": "thirtheen",
        "14": "fourteen",
        "15": "fifteen",
        "16": "sixteen",
        "17": "seventeen",
        "18": "eighteen",
        "19": "nineteen",
    }
    tens_names = {
        "0": "",
        "2": "twenty",
        "3": "thirty",
        "4": "forty",
        "5": "fifty",
        "6": "sixty",
        "7": "seventy",
        "8": "eighty",
        "9": "ninety",
    }
    powers_of_ten_names = {
        1: "hundred",
        2: "thousand",
        3: "million",
        4: "billion",
        5: "trillion",
    }

    size = len(input)
    if size == 1:
        return one_digit_names[input]

    digits = list(input)
    if size == 2:
        if digits[0] == "1":
            return two_digit_names["".join(input)]
        else:
            head = tens_names[digits[0]]
            tail = "".join(digits[1:])
            return " ".join(
                [
                    head,
                    process(tail),
                ]
            )

    if size == 3:
        head = digits[0]
        head_level = powers_of_ten_names[1]
        tail = "".join(digits[1:])
        return " ".join(
            [
                process(head),
                head_level,
                process(tail),
            ]
        )

    power_place = size % 3 or 3
    head = "".join(digits[:power_place])
    head_level = powers_of_ten_names[ceil(size / 3)]
    tail = "".join(digits[power_place:])
    return " ".join(
        [
            process(head),
            head_level,
            process(tail),
        ]
    )
