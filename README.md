# Morse Code Decoder

A Python solution for decoding Morse code from a stream of binary signals.

This project was created as part of a technical assessment for an ERP Developer position.

## Overview

The decoder works in two stages:

1. `decode_bits(bits)`
   - Removes extra zeros from the beginning and end.
   - Detects the transmission time unit.
   - Converts groups of binary signals into Morse code using dots, dashes, and spaces.

2. `decode_morse(morse_code)`
   - Splits Morse code into words and characters.
   - Converts the Morse symbols into readable text using the preloaded Morse code dictionary.

## Example

Input bits:

text
1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011

Decoded Morse:
.... . -.--   .--- ..- -.. .

Decoded message:
HEY JUDE
