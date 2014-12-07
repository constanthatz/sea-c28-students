from __future__ import print_function
import io  # For file operations
import string  # For string.punctuation
import random

# OOPS

f = io.open('sherlock.txt', encoding='utf-8')
# Read only lines that are Sherlock Holmes stories
text = f.readlines()[52:12685]
f.close()
# Join all the lines of text into one text string
text = " ".join(text)


# Strip punctuation and newline characters from imported text to make creating
# dictionary of word combinations easier.
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


story = ()


def write_story(story, word_dict):
    """ Return a story using trigrams usign a imported text."""
    pair = random.choice(word_dict.keys())  # Get starting point for story
    story += pair

    third = u"1"
    while third:
        third = find_next_word(pair)  # Find the next word
        story += (third,)  # Append the next word to the story
        pair = story[-2:]  # Select the last two words to get the next one

    return story


def find_next_word(pair):
    """Return the next woprd based on two words using an imported text"""
    third = random.choice(word_dict.get(pair))
    return third

story = write_story(story, word_dict)
print(" ".join(story))

if __name__ == "__main__":
    text = "I wish I may I wish I might"
