#!/usr/bin/env python

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
text = u" ".join(text)


# Strip punctuation and newline characters from imported text to make creating
# dictionary of word combinations easier.
split_text = text.split()
stripped_text = [i.strip(string.punctuation) for i in split_text]

# Remove words with numbers or punctuation inside of them
# This makes adding random punctuation easier later.
# These words will not be caught by str.strip
for x in stripped_text[:]:
    if not x.isalpha():
        stripped_text.remove(x)


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


def write_story(story, word_dict):
    """Return a story using trigrams usign a imported text."""
    pair = random.choice(word_dict.keys())  # Get starting point for story
    story += pair

    # The while will run until a next word can't be found, and the story ends.
    third = u"1"
    i = 0
    while third and len(story) < 5000:
        i += 3  # Count words
        third = find_next_word(pair)  # Find the next word
        story += (third,)  # Append the next word to the story

        # Insert random sentence ender or comma after either 9, 12, or 15 words
        if i % random.choice([27, 81]) == 0:
            punctuation = [u".", u"!", u"?", u",", ""]
            story += (random.choice(punctuation),)

        # Start new paragrap randomly after 300, 600, or 900 words
        if i % random.choice([300, 600, 900]) == 0:
            story += (u"\n\n",)

        #  Select the next pair of words to be used to find the trigram, while
        # not choosing the punctuation
        j = 1
        pair = ()
        while len(pair) < 2:
            if story[-j].isalnum():
                pair = (story[-j],) + pair

            j += 1

    story += (u"\n\nFIN.",)
    return story


def find_next_word(pair):
    """Return the next word based on two words using an imported text"""
    third = random.choice(word_dict.get(pair))
    return third

if __name__ == "__main__":
    story = (u"A", u"Sherlock", u"Holmes", u"Mystery")
    story = write_story(story, word_dict)
    print(" ".join(story))
    print(u"\nThis story is {} words long.".format(len(story)))
