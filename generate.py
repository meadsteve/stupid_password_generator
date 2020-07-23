import random

parts = [
    ["1 2", "2", "1 two", "one 2", "one two"],
    ["3", "three"],
    ["4", "four"],
    ["5", "five"],
    ["6", "six"],
    ["7", "seven"],
    ["8", "eight"],
    ["9", "nine"]
]


def generate():
    return _randomly_caps_string(
        _randomly_leet_string(
            " ".join(random.choice(part) for part in parts)
        )
    )


def _randomly_caps_string(input_string):
    return "".join(_randomly_caps_letter(letter) for letter in input_string)


def _randomly_leet_string(input_string):
    return "".join(_randomly_leet_letter(letter) for letter in input_string)


def _randomly_caps_letter(letter):
    if random.random() > 0.5:
        return letter.upper()
    else:
        return letter.lower()


def _randomly_leet_letter(letter):
    if random.random() > 0.8:
        return {"e": "3", "a": "4", "o": "0"}.get(letter.lower(), letter)
    return letter


if __name__ == "__main__":
    print(generate())
