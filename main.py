import pandas

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass

# import pandas

# student_data_frame = pandas.DataFrame(student_dict)

# # Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter: row.code for (index, row) in df.iterrows()}
# print(new_dict)
# 2. Create a list of the phonetic code words from a word that the user inputs.
# create try exception to loop until user privides correct values
def generate_phonetic():
    user_word = input("Please enter name to convert: \n").upper()
    try:
        alpha_conversion = [new_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(alpha_conversion)

generate_phonetic()
