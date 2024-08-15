# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
# more fekad up
# new_list = [code for (letter, code) in phonetic_dict.items() if letter in user_input]
print(output_list)