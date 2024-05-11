import numpy as np
from src.matrix_ops import matrix_dot_product, matrix_transpose, matrix_reshape

def test_matrix_dot_product():
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    expected_result = np.array([[19, 22], [43, 50]])
    assert np.array_equal(matrix_dot_product(matrix1, matrix2), expected_result)

def test_matrix_transpose():
    matrix = np.array([[1, 2], [3, 4]])
    expected_result = np.array([[1, 3], [2, 4]])
    assert np.array_equal(matrix_transpose(matrix), expected_result)

def test_matrix_reshape():
    matrix = np.array([[1, 2], [3, 4]])
    new_shape = (4,)
    expected_result = np.array([1, 2, 3, 4])
    assert np.array_equal(matrix_reshape(matrix, new_shape), expected_result)

def test_matrix_reshape():
    matrix = np.array([[1, 2], [3, 4]])
    new_shape = (4,)
    expected_result = np.array([1, 2, 3, 4])
    assert np.array_equal(matrix_reshape(matrix, new_shape), expected_result)