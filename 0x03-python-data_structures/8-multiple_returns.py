#!/usr/bin/python3

# A function that returns a tuple with the length of a string
# and its first character.
# If the sentence is empty, the first character should be equal to None
def multiple_returns(sentence):
    first_letter = None
    if sentence:
        first_letter = sentence[0]
    return (len(sentence), first_letter)
