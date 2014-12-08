#!/usr/bin/env python
from __future__ import print_function
import io

# Data structure for donors and donations using dictionary
donors = {}
donors[u"John Doe"] = [1010.75, 537.15, 5300]
donors[u"Jane Doe"] = [1234]
donors[u"Diana Prince"] = [30730.11, 15300.25]
donors[u"Indiana Jones"] = [301, 130.13, 201.95]
donors[u"Beric Dondarrion"] = [1320.67, 5020.34]
donors[u"Marie Curie"] = [1000, 3200.50]


def first_level_prompt():
    """ Ask the user if they want to quit, send a thank you, create report """
    # Ask user what they want to do

    try:
        prompt = u"\n1: Send a Thank You \n2: Create a Report \nq: Quit \n?: "
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
            print(u"\nNot a valid choice, please choose again.")
            reply = first_level_prompt()
        return reply


def thank_you_prompt():
    """ Prompt user to see the list of donors, or for a name of a donor, their
        donation create a thank you note. If it is a new donor, add the name to
        the list of donors. """

    try:
        prompt = u"\nFull Name (q: quit, s: start over): "
        reply = raw_input(prompt)
    except (EOFError, KeyboardInterrupt):
        return None
    else:
        reply = unicode(reply)  # Convert input to unicode

        if reply.lower() == u"q":
            quit()
        elif reply == u"s":
            reply = first_level_prompt()
        elif reply.lower() == u"list":
            for x in donors.keys():
                print(u"\n")
                print(u"{}".format(x))
            reply = thank_you_prompt()
        else:
            name, donation = name_donation(reply)
            reply = compose_thank_you(name, donation)

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
        prompt = u"\nDonation Amount (q: quit, s: start over): "
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
        else:
            try:
                donation = float(reply)
            except ValueError:
                print(u"\nThat is not a number, please try again.")
                donation = new_donation()
            else:
                donation = donation
    return donation


def compose_thank_you(name, donation):
    """ Compose thank you email, print it, and return to original prompt """

    print(u"\n {}, thank you for your generous donation of ${:.2f}.".format(name, donation))
    reply = first_level_prompt()
    return reply



reply = first_level_prompt()
