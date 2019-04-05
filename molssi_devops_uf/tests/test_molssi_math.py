"""
Tests for the molssi_math module.
"""

# Import package, test suite, and other packages as needed
import molssi_devops_uf as md_uf
import pytest


def test_mean():
    num_list = [1,2,3,4,5]
    observed = md_uf.mean(num_list)
    expected = 3

    assert observed == expected

def test_mean_wrong_type():
    test_input = 'this is not a list'

    with pytest.raises(TypeError):
        md_uf.mean(test_input)
