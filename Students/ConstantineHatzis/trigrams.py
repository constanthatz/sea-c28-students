from __future__ import print_function
import io  # For file operations
import string  # For string.punctuation

f = io.open('sherlock_small.txt', encoding='utf-8')
text = f.read()
f.close()


# Strip punctuation and newline characters from imported text to make creating
# dictionary of word combinations easier. Make all word lowercase to help
# eliminate case sensitivity later
lower_text = text.lower()
split_text = text.split()
stripped_text = [i.strip(string.punctuation) for i in split_text]

# Generate dictionary of every
# ["first_word", "second_word": ["third_word_1", "third_word_2", ... ]
# combination in imported text

word_dict = {}  # Initialize word dictionary
for i in range(len(stripped_text)-2):
    # For loop should only iterate until the third to last word
    first_word = stripped_text[i]
    second_word = stripped_text[i+1]
    third_word = stripped_text[i+2]
    word_dict.setdefault((first_word, second_word), []).append(third_word)



if __name__ == "__main__":
    text = "I wish I may I wish I might"
