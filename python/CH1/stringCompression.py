import unittest
def stringCompression(s):
  '''
  runs in 
  time complexity O(N)
  space complexity O(N)
  '''
  res = ""
  i = 0
  cur = ""
  count  = 1
  while i < len(s):
    cur = s[i]
    if((i + 1) < len(s) and s[i+1] == cur ):
      count += 1
      i += 1
    else:
      res += cur + str(count)
      count = 1
      i += 1
  #这里用min() 更好
  if(len(res) >= len(s)):
    return s
  return res
class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = stringCompression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()