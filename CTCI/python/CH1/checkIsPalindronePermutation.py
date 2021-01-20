import unittest

def checkIsPalindronePermutation(s):
  '''
  Time: O(N):
  Space: O(1);
  '''
  
  s = s.replace(" ","")
  s = s.lower()
  seen = dict()
  for char in s:
    if char not in seen:
      seen[char] = 1
    else:
      seen[char] += 1

  singleCount = 0
  for key in seen.keys():
    if seen[key] % 2 != 0:
      singleCount += 1
  if singleCount > 1:
    return False
  return True


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = checkIsPalindronePermutation(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()