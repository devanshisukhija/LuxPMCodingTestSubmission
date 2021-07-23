"""
1) Generates first n odd numbers from 0.

Parameters:
-----------
- n_odds: (int) number of first odd numbers to generate from 0.

Returns:
--------
List of first n odd numbers from 0.
"""

def listOfFirstNOddsFromZero(n_odds=20):
    return list([x for x in range(1, n_odds*2+1, 2)])

# hardcoded test
assert len(listOfFirstNOddsFromZero()) ==20 , f"Assertion Failed: Length of return value {len(listOfFirstNOddsFromZero())}"


"""
2) Insert odd number digits in reverse order
    in between letters of a word.

Parameters:
-----------
- word: given word to insert digits in between.
- n_last_digits: number of digits to insert between words.

Return:
-------
Modified String (str): contains revered odd digits in between letters of the words.

**Function code only works if length of the word is equal to or one more than number of digits
needed to be inserted between word's letters.

"""
def stringOddDigitsBtwLetters(word="LuxPMsoft", n_last_digits=8):
    # Following code only works if length of word and n_last_digits is same or length of word is one more, hence,
    assert len(word)== n_last_digits or len(word) == n_last_digits+1, "Word lenght must match number of digits to be inserted or should be only one more than digits to be inserted."

    reversed_odds = listOfFirstNOddsFromZero()
    reversed_odds.reverse()
    reversed_odds = reversed_odds[:n_last_digits]

    word =list(word)

    result = [None] * (len(reversed_odds)+len(word))
    result[1::2] = reversed_odds
    result[::2] = word

    result = [str(x) for x in result]
    return "".join(result)

# print(stringOddDigitsBtwLetters())
