"""
molssi_math.py
A sample repository for the MOLSSI workshop at UF.

some math functions.
"""


def mean(num_list):
    """
    Calculate the mean/average of a list of numbers.

    Parameters
    ----------
    num_list : list
        The list to make the average of

    Returns
    ----------
    mean_list : float
        The mean of the list
    """

    # check input type list
    if not isinstance(num_list, list):
        raise TypeError('Invalid input %s - Input must be a list' % (num_list))

    # check list not empty
    if num_list == []:
        raise ValueError('Cannot apply mean to empty list')
    try:
        mean_list = sum(num_list) / float(len(num_list))
    except TypeError:
        raise TypeError('Cannot calculate mean of list - all list elements must be numeric')

    return mean_list


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
