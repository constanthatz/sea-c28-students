#!/usr/bin/env python
from __future__ import print_function
from __future__ import division

# Data structure for donors and donations using dictionary
donors = {}
donors[u"John Doe"] = [1010.75, 537.25, 5300]
donors[u"Jane Doe"] = [1234]
donors[u"Diana Prince"] = [30730.25, 15300.25]
donors[u"Indiana Jones"] = [301, 130.50, 201.75]
donors[u"Beric Dondarrion"] = [1320.75, 5020.25]
donors[u"Marie Curie"] = [1000, 3200.50]


def safe_input(prompt):
    """Return user input after catching KeyboardInterrupt and EOFError"""
    try:
        reply = raw_input(prompt)
    except (EOFError, KeyboardInterrupt):
        return quit()
    else:
        return reply


def first_level_prompt():
    """Return user input. Quit, send thank you email to donor, or create report
        or donors."""

    # Ask user what they want to do
    prompt = u"\n1: Send a Thank You \n2: Create a Report \nq: Quit \n?: "
    reply = safe_input(prompt)

    reply = unicode(reply)  # Convert input to unicode

    if reply.lower() == u"q":
        quit()
    elif reply == u"1":
        reply = thank_you_prompt()
    elif reply == u"2":
        reply = create_report()
    else:
        print(u"\nNot a valid choice, please choose again.")
        reply = first_level_prompt()
    return reply


def thank_you_prompt():
    """Return user input. Prompt user (1) to see list of donors, (2) for donor
        name and their donation amount and create a thank you note. If it is a
        new donor, add their name to the list of donors."""

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
    """Return name of donor and their donation amount."""
    donors.setdefault(name, [])
    donation = new_donation()
    donors.get(name).append(donation)
    return name, donation


def new_donation():
    """Return donation amount."""
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
    """Print thank you email from template"""

    template = u"\n\t{}, thank you for your generous donation of${:.2f}." \
        .format(name, donation)
    print(template)
    reply = first_level_prompt()
    return reply


def create_report():
    """Return a report of all donors, average donation amount, number of
    donations, and total donations"""
    report_matrix = {}
    for x in donors:
        donations = donors[x]
        total_donations = sum(donations)
        number_donations = len(donations)
        avg_donation = total_donations / number_donations
        report_matrix[x] = [total_donations, number_donations, avg_donation]

    header = [u"Donor", u"Total Donations", u"Number of Donations",
              u"Average Donations"]

    print(u"{0:<20}{1:>20}{2:>30}{3:>30}\n".format(*header))
    for x in report_matrix:
        args = [x, "${:.2f}".format(report_matrix[x][0]), report_matrix[x][1],
                "${:.2f}".format(report_matrix[x][2])]
        print(u"{0:<20}{1:>20}{2:>30}{3:>30}\n".format(*args))

    reply = first_level_prompt()
    return reply


reply = first_level_prompt()
