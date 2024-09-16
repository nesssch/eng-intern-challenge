ENG_TO_BRAILLE = { #converts English characters to Braille
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......"
}

BRAILLE_TO_ENG_LET = {}
BRAILLE_TO_ENG_NUM = {}

for key, value in ENG_TO_BRAILLE.items(): #Fills Braille dictionaries
    if key.isalpha():
        BRAILLE_TO_ENG_LET[value] = key
    else:
        BRAILLE_TO_ENG_NUM[value] = key

def convert_e_to_b(text):
    """Converts input text in English to its corresponding Braille text"""
    braille = ""
    for char in text:
        if char.isupper():
            braille = braille + ".....O"
            braille_char = ENG_TO_BRAILLE[char.lower()]
        else:
            braille_char = ENG_TO_BRAILLE[char]
        braille = braille + braille_char
    return braille

def b_lookup (b_char, is_cap, is_num):
    """great documentation"""
    if is_num:
        return BRAILLE_TO_ENG_NUM[b_char]
    e_char = BRAILLE_TO_ENG_LET[b_char]
    if is_cap:
        return e_char.upper()
    return e_char

def convert_b_to_e(text):
    """Converts input text in Braille to its corresponding English text"""
    english = ""
    is_cap = False
    is_num = False
    for i in range(0, len(text), 6):
        b_char = text[i:i+6]
        if b_char == ".....O":
            is_cap = True
        if b_char == ".O.OOO":
            is_num = True

        else:
            e_char = b_lookup(b_char, is_cap, is_num)
            english = english + e_char

        if b_char == "......":
            is_num = False
        is_cap = False








    

