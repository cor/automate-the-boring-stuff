#! python3
# pig_latin.py - Translates text into pig latin.

print('Enter the English message to translate into Pig Latin:')
message = input()
pig_latin = []

for word in message.split():
    # Separate the non-letters at the start of this word:
    prefix_non_letters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefix_non_letters += word[0]
        word = word[1:]

    # If the word does not contain letters, add it to pig latin:
    if len(word) == 0:
        pig_latin.append(prefix_non_letters)
        continue

    # Separate the non-letters at the end of this word:
    suffix_non_letters = ''
    while not word[-1].isalpha():
        suffix_non_letters += word[-1]
        word = word[:-1]

    # Remember if the word was in uppercase or title case.
    was_upper = word.isupper()
    was_title = word.istitle()

    word = word.lower()  # Make the word lowercase for translation.

    # Separate the consonants at the start of this word:
    prefix_constants = ''
    while len(word) > 0 and not word[0] in 'aeiouy':
        prefix_constants += word[0]
        word = word[1:]

    # Add the Pig Latin ending to the word:
    word_ending = 'ay' if prefix_non_letters != '' else 'yay'
    word += word_ending

    # Set the word back to uppercase or title case:
    if was_upper:
        word = word.upper()
    if was_title:
        word = word.title()

    # Add the non-letters back to the start or end of the word.
    pig_latin.append(prefix_constants + word + suffix_non_letters)

# Join all the words back together into a single string:
print(' '.join(pig_latin))
