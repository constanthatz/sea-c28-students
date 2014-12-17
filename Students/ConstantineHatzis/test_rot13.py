#!/usr/bin/env python

import pytest
import string
from rot13 import rot13


def test_encrypt_alphabet():
    # Test case 1: Does it properly encrypt the alphabet?
    key13 = u"nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
    alphabet = unicode(string.ascii_letters)

    assert rot13(alphabet) == key13


def test_encrypt_punctuation():
    # Test case 1: Does it properly encrypt the alphabet?
    # Test case 2: Does it ignore punctuation adn white space?
    punc = unicode(string.punctuation)

    assert rot13(punc) == punc
