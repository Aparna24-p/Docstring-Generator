"""Temporary upload utilities.

This module provides sample functions and classes
for demonstration and validation purposes.
"""

import streamlit as st


@st.cache_data
def outer_func(a):
    """
    Apply a nested transformation.

    Parameters
    ----------
    a : int or float
        Input value to be processed.

    Returns
    -------
    int or float
        Result after applying the inner function.
    """
    def inner_func(b):
        """Double the input value."""
        return b * 2

    return inner_func(a)


class EmptyClass:
    """
    Example empty class.

    This class currently has no attributes or methods.
    It is used only for demonstration.
    """
   
    pass
