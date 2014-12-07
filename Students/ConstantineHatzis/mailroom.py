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



def original_prompt():
    """ Ask the user if they want to quit, send a thank you, create report """
    reply = ask_for_input(u"Send a Thank You or Create a Report")

    if quit:
        quit()
    elif reply_is_send_thank_you:
        thank_you()
    elif reply_is_create_report:
        create_report()
    else:
        print(choose_again_error)
        reply = original_prompt()
    return reply


def thank_you():
    """ Prompt user to see the list of donors, or for a name of a donor, their
        donation create a thank you note. If it is a new donor, add the name to
        the list of donors. """

    reply = ask_for_input(u"list of donors or name or quit")

    if quit:
        original_prompt()
    elif reply_is_list_of_donors:
        print(donors)
    elif reply_is_name:
        if name_is_old:
            amount = new_donation()
            compose_thank_you(name, amount)
        else:
            add_new_donor(name)
            amount = new_donation()
            compose_thank_you(name, amount)
    return reply


def new_donation(name, amount):
    """ Update donors dict with new donation """
    update_donors_dict_with_amount
    return amount


def add_new_donor(name):
    """ Update donors dict with new donor """
    update_donors_dict_with_name
    return name


def compose_thank_you(name, amount):
    """ Compose thank you email, print it, and return to original prompt """

    print(thank_you_letter, name, amount)
    original_prompt
    return name, amount


def create_report():
    """ Create report of donors and donations after calculating the total
        donations, numbder of donations, and average donations for each
        donor and print them in order of total donations """
    total_donation = calculate_total_donation
    numder_donations = calculate_number_of_donations
    average_donation = calculate_average_donation

    (print(donors_in_nice_table, total_donation, numder_donations,
           average_donation))
    original_prompt()
    return total_donation, numder_donations, average_donation

original_prompt()
