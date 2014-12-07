from __future__ import print_function
import io  # For file operations
import string  # For string.punctuation
import random

f = io.open('sherlock.txt', encoding='utf-8')
text = f.read()
f.close()


# Strip punctuation and newline characters from imported text to make creating
# dictionary of word combinations easier. Make all word lowercase to help
# eliminate case sensitivity later
lower_text = text.lower()
split_text = lower_text.split()
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


def ask_for_words():
    u"""Return the words that the user inputed plus a third word fromthe dictionary."""
    try:
        words = raw_input(u"Type two words, a punctuation mark (.?!,), or FIN to end your story: ")
    except (EOFError, KeyboardInterrupt):
        return None
    else:
        words = unicode(words)

        if words == u"FIN":
            words_list = words
        elif words == u"." or words == u"?" or words == "!" or words == ",":
            words_list = list(words)
        else:
            words_list = words.split()

            if len(words_list) != 2:
                print(u"That was not {} words, try again: ".format(2))
                words_list = ask_for_words()
            else:
                words = tuple([x.lower() for x in words_list])
                if word_dict.get(words):
                    next_word = random.choice(word_dict.get(words))
                    words_list.append(next_word)
                else:
                    print(u"You chose poorly, try again: ")
                    words_list = ask_for_words()
    return words_list


def write_story(story_list):
    word_combo = []
    while word_combo != u"FIN":
        word_combo = ask_for_words()
        story_list += word_combo
        story = " ".join(story_list)
        print(story)
    return story

story_list = []
story = write_story(story_list)
print(story)

if __name__ == "__main__":
    text = "I wish I may I wish I might"
