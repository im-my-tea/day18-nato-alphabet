import pandas

nato = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato.iterrows()}

result = [nato_dict[l] for l in input("Enter a word: ").upper()]
print(result)