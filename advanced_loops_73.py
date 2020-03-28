# One of the first known examples of encryption was used by Julius Caesar. Caesar
# needed to provide written instructions to his generals, but he didn’t want his enemies
# to learn his plans if the message slipped into their hands. As a result, he developed
# what later became known as the Caesar cipher.
# The idea behind this cipher is simple (and as such, it provides no protection against
# modern code breaking techniques). Each letter in the original message is shifted by
# 3 places. As a result, A becomes D, B becomes E, C becomes F, D becomes G, etc.
# The last three letters in the alphabet are wrapped around to the beginning: X becomes
# A, Y becomes B and Z becomes C. Non-letter characters are not modified by the
# cipher.
# Write a program that implements a Caesar cipher. Allow the user to supply the
# message and the shift amount, and then display the shifted message. Ensure that
# your program encodes both uppercase and lowercase letters. Your program should
# also support negative shift values so that it can be used both to encode messages and
# decode messages

import string
caesar_cipher = ""

message = input("Please enter your message: ").lower()
for letter in message:
    if letter != " " and letter != "."and letter != ",":
        if letter == "x":
            caesar_cipher = caesar_cipher + "a"
        elif letter == "y":
            caesar_cipher = caesar_cipher + "b"
        elif letter == "z":
            caesar_cipher = caesar_cipher + "c"
        else:
            alphabet = string.ascii_lowercase.index(letter)
            cipher = string.ascii_lowercase[alphabet+3]
            caesar_cipher = caesar_cipher + cipher
    else:
        caesar_cipher = caesar_cipher + letter
print(caesar_cipher)
decipher = input("Decipher? ").lower()
if decipher[0] == "y":
    message = caesar_cipher
    caesar_cipher = ""
    for letter in message:
        if letter != " " and letter != "." and letter != ",":
            if letter == "a":
                caesar_cipher = caesar_cipher + "x"
            elif letter == "b":
                caesar_cipher = caesar_cipher + "y"
            elif letter == "c":
                caesar_cipher = caesar_cipher + "z"
            else:
                alphabet = string.ascii_lowercase.index(letter)
                cipher = string.ascii_lowercase[alphabet - 3]
                caesar_cipher = caesar_cipher + cipher
        else:
            caesar_cipher = caesar_cipher + letter
print(caesar_cipher)