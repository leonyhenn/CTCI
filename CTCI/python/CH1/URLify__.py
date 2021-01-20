import unittest

def HengsURLify(s,l):
  '''
  Time: O(N^2)
  Space: O(N)

  NOT OPT SOL.
  '''
  i = 0
  ls = list(s)
  while i < (l-1):
    if ls[i] == " ":
      for j in range(l-1,i,-1):
        ls[j+2] = ls[j]
      ls[i] = '%'
      ls[i+1] = '2'
      ls[i+2] = '0'
      l += 2
    i += 1
  return ''.join(ls)
# assert(HengsURLify('1 23  ',4) =='1%2023' )
# print(HengsURLify('Mr John Smith    ',13))
# print(HengsURLify('much ado about nothing      ', 22))
def SolUrlify(string, length):
    '''function replaces single spaces with %20 and removes trailing spaces
    O(N)
    '''
    new_index = len(string)

    for i in reversed(range(length)):
        if string[i] == ' ':
            # Replace spaces
            string[new_index - 3:new_index] = '%20'
            new_index -= 3
        else:
            # Move characters
            string[new_index - 1] = string[i]
            new_index -= 1

    return string

# assert(SolUrlify(list('1 23  '),4) =='1%2023' )
print(SolUrlify(list('1 23  '),4))
print(SolUrlify(list('Mr John Smith    '),13))
print(SolUrlify(list('much ado about nothing      '), 22))


class Test(unittest.TestCase):
    '''Test Cases'''
    # Using lists because Python strings are immutable
    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = SolUrlify(test_string, length)
            self.assertEqual(actual, expected)

# if __name__ == "__main__":
#     unittest.main()