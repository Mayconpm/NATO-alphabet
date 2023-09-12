import pandas as pd

student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}

# Looping through dictionaries:
for key, value in student_dict.items():
    # Access key and value
    pass

student_data_frame = pd.DataFrame(student_dict)

# Loop through rows of a data frame
for index, row in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
df_nato_phonetic_alphabet = pd.read_csv("nato_phonetic_alphabet.csv")


nato_dict = {row.letter: row.code for _, row in df_nato_phonetic_alphabet.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetic_list():
    user_word = input("Enter a word: ")
    try:
        phonetic_list = [nato_dict[letter.upper()].title() for letter in user_word]
        print(phonetic_list)
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic_list()


generate_phonetic_list()
