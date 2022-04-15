import pandas
data = pandas.read_csv('nato_phonetic_alphabet.csv')

alphabet = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()
listo = [alphabet[letter] for letter in word]
print(listo)
