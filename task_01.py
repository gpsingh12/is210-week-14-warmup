#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Pet module"""

from pet import Pet


class Dog(Pet):
    """ Pet is the parent class for Dog.
    Attributes:
        None
    """
    def __init__(self, has_shots=False, **kwargs):
        """ Constructor for Dog class.
        Attributes:
            has_shots(bool): False
            arb_arg(dict): argument dictionary
        Args:
            has_shots(bool): defaults to False.
            arb_arg(dict): an arbitrary arguments dictionary.
        """
        self.has_shots = has_shots
        super(Dog, self).__init__(**kwargs)
