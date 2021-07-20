#!/usr/bin/env python3
"""
Write a type-annotated function sum_list which
takes a list input_list of floats as argument
and returns their sum as a float.
"""
# define type alias floatList which is a list of floats
floatList = [float]


def sum_list(input_list: floatList) -> float:
    """
    Sum a list of floats.
    """
    return sum(input_list)
