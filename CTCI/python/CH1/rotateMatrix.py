import unittest
# Time O(N x N)
# Space O(1)

def rotateMatrix(matrix):
  n = len(matrix)
  for layer in range(n // 2):
    head = layer
    tail = n - layer - 1
    for index in range(head, tail):
      # Save top
      top = matrix[layer][index]

      # top = left
      matrix[layer][index] = matrix[n - index - 1][layer]

      # left = bottom
      matrix[n - index - 1][layer] = matrix[n - layer - 1][n - index - 1]

      # bottom = right
      matrix[n - layer - 1][n - index - 1] = matrix[index][n - layer - 1]

      # right = top
      matrix[index][n - layer - 1] = top

  return matrix

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]

    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = rotateMatrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()