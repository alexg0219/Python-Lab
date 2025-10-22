import numpy as np
from numpy.testing import assert_array_equal, assert_array_almost_equal


def replace_nans(X: np.ndarray) -> np.ndarray:
    median = np.nanmedian(X, axis=0)
    nan_idx = np.isnan(X)
    median[np.isnan(median)] = 0
    #print(nan_idx,median)
    X = np.where(nan_idx, median,X)
    return X


assert_array_equal(replace_nans(
    np.array([[np.nan], [np.nan],  [np.nan]])),
    np.array([[0. ],[ 0. ],[ 0. ]])
)
######################################################
assert_array_equal(replace_nans(
    np.array([[0, 42,  42]])),
    np.array([[0, 42 , 42]])
)
######################################################
assert_array_equal(replace_nans(
    np.array([[np.nan], [1], [np.nan]])),
    np.array([[1.] ,[ 1.] ,[ 1. ]])
)
######################################################
assert_array_equal(replace_nans(
    np.array([[4], [1],  [np.nan]])),
    np.array([[4 ], [1] ,[ 2.5]])
)
######################################################
assert_array_equal(replace_nans(
    np.array([[np.nan, np.nan,  np.nan],
              [     4, np.nan,       5],
              [np.nan,      8,  np.nan]]).T),
    np.array([[0. , 0. , 0. ],
              [4. , 4.5, 5. ],
              [8. , 8. , 8. ]]).T
)
######################################################