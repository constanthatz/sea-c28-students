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
    u"""Return the words that the user inputed plus a random third word from
        the dictionary."""
    try:
        prompt = u"""Type one word, two words, a punctuation mark (.?!,), or \
FIN to end your story: """
        words = raw_input(prompt)
    except (EOFError, KeyboardInterrupt):
        return u" FIN"
    else:
        u_words = unicode(words)

        if u_words == u"FIN":
            trigram = u" " + u_words
        elif u_words == u"." or u_words == u"?" or u_words == u"!" or \
                u_words == u"," or u_words == u"\t":
            trigram = u_words
        elif u_words == "":
            trigram = u"\n"
        else:
            list_u_words = u_words.split()

            if len(list_u_words) == 1:
                trigram = u" " + u" ".join(list_u_words)
            elif len(list_u_words) != 2:
                print(u"That was not {} or {} words, try again: ".format(1, 2))
                trigram = ask_for_words()
            else:
                look_up_words = tuple([x.lower() for x in list_u_words])
                if word_dict.get(look_up_words):
                    next_word = random.choice(word_dict.get(look_up_words))
                    list_u_words.append(next_word)
                    trigram = u" " + u" ".join(list_u_words)
                else:
                    print(u"You chose poorly, try again: ")
                    trigram = ask_for_words()
    return trigram


def write_story(story):
    trigram = u""
    while trigram != u" FIN":
        trigram = ask_for_words()
        story += trigram
        print(story)
    return story

story = ""
story = write_story(story)
print(story)

if __name__ == "__main__":
    text = "I wish I may I wish I might"
