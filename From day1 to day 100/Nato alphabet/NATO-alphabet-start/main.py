import pandas
data = pandas.read_csv('nato_phonetic_alphabet.csv')

alphabet = {row.letter: row.code for (index, row) in data.iterrows()}


def generator():
    word = input("Enter a word: ").upper()
    try:
        listo = [alphabet[letter] for letter in word]
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
        generator()
    else:
        print(listo)

generator()