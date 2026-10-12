str = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
alphabets = 0
spaces = 0

for ch in str:
    if ch.isalpha():
        alphabets += 1

        if ch in "aeiouAEIOU":
            vowels += 1
        else:
            consonants += 1

    elif ch.isdigit():
        digits += 1

    elif ch.isspace():
        spaces += 1

print("Number of vowels =", vowels)
print("Number of consonants =", consonants)
print("Number of digits =", digits)
print("Number of alphabets =", alphabets)
print("Number of spaces =", spaces)