#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_02."""

from data import FRUIT


def get_cost_per_item(shoplist):
    """Function iterates the argumentusing key from FRUIT.
    Args:
        shoplist(dict):the key is item name from FRUIT and its value is an
            integer which indicates no. of units to be purchased
    Return:
        returns a dictionary keyed by name of fruit with total cost per item
            reflected.
    Examples:
        >>> shoplist = {'Beet': 1, 'Apple': 2.08, 'Lime': 12, 'Peach': 24}
        >>> get_cost_per_item(shoplist)
    {'Peach': 95.76, 'Lime': 7.08}
    """
    return {somekey: shoplist[somekey] * FRUIT[somekey]
            for somekey in shoplist.iterkeys() if somekey in FRUIT}


def get_total_cost(shoplist):
    """ Function retrieve per item cost
    Args:
        shoplist(dict): key of shoplist is item found in FRUIT and value
            is an integer indicating no. of units to be purchased
    Return:
        returns the total cost by adding up values of resultant dictionary
    Examples:
        >>> shoplist = {'Beet': 1, 'Apple': 2.08, 'Lime': 12, 'Peach': 24}
        >>> get_total_cost(shoplist)
    102.84
    """
    return sum(someval for someval in get_cost_per_item(shoplist).itervalues())
