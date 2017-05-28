CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.',

        '.': '.-.-.-', ',': '--..--', '!': '-.-.--',
        ':': '---...', '?': '..--..', ' ': '       '
        }

valid_chars = []
user_input = input('what you say').upper()
morse_output = []

for char in CODE:
    valid_chars.append(char)

print(valid_chars)

for i in user_input:
    if i in valid_chars:
        morse_output.append(CODE[i])
    else:
        morse_output.append('/')

print(''.join(morse_output))
        



























