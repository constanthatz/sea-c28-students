#!/usr/bin/env python
from __future__ import print_function
import io

# Data structure for donors and donations using dictionary
donors = {}
donors[u"John Doe"] = [1000, 500, 5000]
donors[u"Jane Doe"] = [1000]
donors[u"Diane Prince"] = [30000, 15000]
donors[u"Indiana Jones"] = [300, 100, 200]
donors[u"Beric Dondarrion"] = [1000, 5000]
donors[u"Marie Curie"] = [1000, 3000]


def first_level_prompt():
    """ Ask the user if they want to quit, send a thank you, create report """
    # Ask user what they want to do

    try:
        prompt = u" 1: Send a Thank You \n 2: Create a Report \n q: Quit \n ?: "
        reply = raw_input(prompt)
    except (EOFError, KeyboardInterrupt):
        return None
    else:
        reply = unicode(reply)  # Convert input to unicode

        if reply.lower() == u"q":
            quit()
        elif reply == u"1":
            reply = thank_you_prompt()
        elif reply == u"2":
            reply = 2
        else:
            print(u"Not a valid choice, please choose again.")
            reply = first_level_prompt()
        return reply


def thank_you_prompt():
    """ Prompt user to see the list of donors, or for a name of a donor, their
        donation create a thank you note. If it is a new donor, add the name to
        the list of donors. """

    try:
        prompt = u"Full Name (q: quit, s: start over): "
        reply = raw_input(prompt)
    except (EOFError, KeyboardInterrupt):
        return None
    else:
        reply = unicode(reply)  # Convert input to unicode

        if reply.lower() == u"q":
            quit()
        elif reply == u"s":
            reply = first_level_prompt()
        else:
            name, donation = name_donation(reply)
            compose_thank_you(name, donation)

    return reply


def name_donation(name):
    """ Update donors dict with new donation and name if necessary"""
    donors.setdefault(name, [])
    donation = new_donation()
    donors.get(name).append(donation)
    return name, donation


def new_donation():
    """ Update donors dict with new donor """
    try:
        prompt = u"Donation Amount (q: quit, s: start over): "
        reply = raw_input(prompt)
    except (EOFError, KeyboardInterrupt):
        return None
    else:
        reply = unicode(reply)  # Convert input to unicode

        if reply.lower() == u"q":
            quit()
        elif reply == u"s":
            reply = first_level_prompt()
            return reply
        elif not reply.isnumeric():
            print(u"That is not a number, please try again.")
            donation = new_donation()

    return donation


def compose_thank_you(name, donation):
    """ Compose thank you email, print it, and return to original prompt """

    print(u"{}, thank you for your generous donation of ${}.".format(name, donation))
    reply = first_level_prompt
    return reply
