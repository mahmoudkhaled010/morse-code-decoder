def decode_bits(bits):
    bits = bits.strip("0")

    if not bits:
        return ""

    groups = []
    current_group = bits[0]

    for bit in bits[1:]:
        if bit == current_group[0]:
            current_group += bit
        else:
            groups.append(current_group)
            current_group = bit

    groups.append(current_group)

    unit = min(len(group) for group in groups)

    morse = ""

    for group in groups:
        length = len(group)

        if group[0] == "1":
            if length >= 3 * unit:
                morse += "-"
            else:
                morse += "."
        else:
            if length >= 7 * unit:
                morse += "   "
            elif length >= 3 * unit:
                morse += " "

    return morse


def decode_morse(morseCode):
    morseCode = morseCode.strip()

    if not morseCode:
        return ""

    words = morseCode.split("   ")
    decoded_words = []

    for word in words:
        letters = word.split(" ")
        decoded_word = ""

        for letter in letters:
            decoded_word += MORSE_CODE[letter]

        decoded_words.append(decoded_word)

    return " ".join(decoded_words)