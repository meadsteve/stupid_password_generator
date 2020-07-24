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
    return _apply_to_each_letter(
        " ".join(random.choice(part) for part in parts),
        _randomly_caps_letter,
        _randomly_leet_letter
    )


def _apply_to_each_letter(input_string, *funcs):
    letters = (letter for letter in input_string)
    for func in funcs:
        letters = (func(letter) for letter in letters)
    return "".join(letters)


def _randomly_caps_letter(letter):
    if random.random() > 0.5:
        return letter.upper()
    else:
        return letter.lower()


def _randomly_leet_letter(letter):
    replacements = {"e": "3", "a": "4", "o": "0"}
    if letter.lower() not in replacements or random.random() < 0.8:
        return letter
    return replacements.get(letter.lower(), letter)


if __name__ == "__main__":
    print(generate())
