#!/usr/bin/env python
from __future__ import print_function
from __future__ import division
from operator import itemgetter

# Data structure for donors and donations using dictionary
donors = {
    u"John Doe": [1010.75, 537.25, 5300],
    u"Jane Doe": [1234],
    u"Diana Prince": [30730.25, 15300.25],
    u"Indiana Jones": [301, 130.50, 201.75],
    u"Beric Dondarrion": [1320.75, 5020.25],
    u"Marie Curie": [1000, 3200.50]
    }


def safe_input(prompt):
    """Return user input after catching KeyboardInterrupt and EOFError"""
    try:
        reply = raw_input(prompt)
    except (EOFError, KeyboardInterrupt):
        quit()
    else:
        return reply.decode('utf-8')  # Convert input to unicode


def first_level_prompt():
    """Return user input. Quit, send thank you email to donor, or create report
        or donors."""

    # Ask user what they want to do
    prompt = u"\n1: Send a Thank You \n2: Create a Report \nq: Quit \n?: "
    reply = safe_input(prompt)

    # Parse user input. "q" for quit, "1" to write thank you email
    # "2" to create report, and catch invalid choices
    if reply.lower() == u"q":  # Quit mailroom
        quit()
    elif reply == u"1":
        thank_you_prompt()  # Create thank you email
    elif reply == u"2":
        create_report()  # Create donor report
    else:
        # Reject invalid choice
        print(u"\nNot a valid choice, please choose again.")
        first_level_prompt()


def thank_you_prompt():
    """Return user input. Prompt user (1) to see list of donors, (2) for donor
        name and their donation amount and create a thank you note. If it is a
        new donor, add their name to the list of donors."""

    # Ask user what they want to do
    prompt = u"\nFull Name (q: quit, s: start over): "
    reply = safe_input(prompt)

    # Parse user input. "q" for quit, "s" back to start over
    # "list" to see donors, or donor name
    if reply.lower() == u"q":  # Quit mailroom
        quit()
    elif reply == u"s":  # Go back to first prompt
        first_level_prompt()
    elif reply.lower() == u"list":  # Print list of donors and return to prompt
        print(u"\n")
        for x in donors.keys():
            print(u"{}".format(x))
        thank_you_prompt()
    else:
        name, donation = name_donation(reply)  # Check user inputted name
        compose_thank_you(name, donation)  # Compose thank you email


def name_donation(name):
    """Return name of donor and their donation amount."""
    donors.setdefault(name, [])  # Add name to donor list if not in list
    donation = new_donation()  # Ask for donation amount
    donors.get(name).append(donation)  # Add donation amont to donor list
    return name, donation


def new_donation():
    """Return donation amount."""

    # Ask user what they want to do
    prompt = u"\nDonation Amount (q: quit, s: start over): "
    reply = safe_input(prompt)

    # Parse user input. "q" for quit, "s" back to start over
    # donation amount
    if reply.lower() == u"q":  # Quit mailroom
        quit()
    elif reply == u"s":  # Go back to original prompt
        reply = first_level_prompt()
        return reply
    else:  # Validate user input as a real number
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

    # Email template
    template = u"\n\t{}, thank you for your generous donation of ${:.2f}." \
        .format(name, donation)
    print(template)
    first_level_prompt()  # Go back to original prompt


def create_report():
    """Return a report of all donors, average donation amount, number of
    donations, and total donations"""
    report_matrix = []  # Initialize report data dictionary

    for x in donors:
        donor = x
        donations = donors[x]  # List of donations
        total_donations = sum(donations)  # Total donations
        number_donations = len(donations)  # Total number of donations
        avg_donation = total_donations / number_donations  # Average donation
        report_matrix += [[
                          donor, total_donations,
                          number_donations,
                          avg_donation]]

    # Sort report matrix by total donor amount in decending order.
    sorted_report_matrix = sorted(
        report_matrix, key=itemgetter(1), reverse=True)

    # Column titles
    header = [u"Donor", u"Total Donations", u"Number of Donations",
              u"Average Donation"]

    # Print column titles
    print(u"{0:<20}{1:>20}{2:>30}{3:>30}\n".format(*header))
    for x in range(len(report_matrix)):  # Print table

        # Format report data so that I can right align in the columns when I
        # print the table, but still have the dollar sign next to the numbers
        args = [
            sorted_report_matrix[x][0],
            "${:.2f}".format(sorted_report_matrix[x][1]),
            sorted_report_matrix[x][2],
            "${:.2f}".format(sorted_report_matrix[x][3])]

        print(u"{0:<20}{1:>20}{2:>30}{3:>30}\n".format(*args))

    first_level_prompt()  # Go back to original prompt

if __name__ == '__main__':
    # Start the mailroom
    first_level_prompt()
