import numpy as np
from numpy.testing import assert_array_equal, assert_array_almost_equal


def sort_evens(A: np.ndarray) -> np.ndarray:
    ind = np.where(A % 2 == 0)
    A[ind] = np.sort(A[ind])
    return A

######################################################
assert_array_equal(sort_evens(np.array([])), np.array([]))
######################################################
assert_array_equal(sort_evens(np.array([2, 0])), np.array([0, 2]))
######################################################
assert_array_equal(sort_evens(np.array([9, 3, 1, 5, 7])), np.array([9, 3, 1, 5, 7]))
######################################################
assert_array_equal(sort_evens(np.array([8, 12, 4, 10, 6, 2])), np.array([2, 4, 6, 8, 10, 12]))
######################################################