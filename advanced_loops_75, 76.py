# A string is a palindrome if it is identical forward and backward. For example “anna”,
# “civic”, “level” and “hannah” are all examples of palindromic words.Write a program
# that reads a string from the user and uses a loop to determine whether or not it is a
# palindrome. Display the result, including a meaningful output message.

import string
flag = True
word = input("Please enter a word: ").lower()
if len(word) % 2 == 0:
    for letter in word:
        position = word.index(letter)
        if letter != word[-(position + 1)]:
            print(f"The word {word} is not a palindrome.")
            flag = False
            break
else:
    middle = (len(word) - 1) / 2 + 1
    for letter in word:
        position = word.index(letter)
        if position != middle:
            if letter != word[-(position + 1)]:
                print(f"The word {word} is not a palindrome.")
                flag = False
                break
if flag:
    print(f"The word {word} is a palindrome.")


# There are numerous phrases that are palindromes when spacing is ignored. Examples
# include “go dog”, “flee to me remote elf” and “some men interpret nine memos”,
# among many others. Extend your solution to Exercise 75 so that it ignores spacing
# while determining whether or not a string is a palindrome. For an additional challenge,
# further extend your solution so that is also ignores punctuation marks and treats
# uppercase and lowercase letters as equivalent.

import string
flag = True
word = ""
phrase = input("Please enter a phrase: ").lower()
for i in phrase:
    if i != " " and i != "."and i != ",":
        word = word + i
if len(word) % 2 == 0:
    for letter in word:
        position = word.index(letter)
        if letter != word[-(position + 1)]:
            print(f"The phrase {phrase} is not a palindrome.")
            flag = False
            break
else:
    middle = (len(word) - 1) / 2 + 1
    for letter in word:
        position = word.index(letter)
        if position != middle:
            if letter != word[-(position + 1)]:
                print(f"The phrase {phrase} is not a palindrome.")
                flag = False
                break
if flag:
    print(f"The phrase {phrase} is a palindrome.")
