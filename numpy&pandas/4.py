import numpy as np
from numpy.testing import assert_array_equal, assert_array_almost_equal
def num_sum(np_arr: np.ndarray) -> np.ndarray:

    max_len = len(str(np.max(np_arr)))
    powers_of_10 = 10 ** np.arange(max_len)[:, np.newaxis]
    digits = (np_arr // powers_of_10) % 10
    sum_of_digits = np.sum(digits, axis=0)

    return sum_of_digits


######################################################
assert_array_equal(num_sum(np.array([82])), np.array([10]))
######################################################
assert_array_equal(num_sum(np.array([1241, 354, 121])), np.array([8, 12, 4]))
######################################################
assert_array_equal(
    num_sum(np.array([1, 22, 333, 4444, 55555])), np.array([1, 4, 9, 16, 25]))
######################################################