import unittest
def oneAway(s1,s2):
  '''
  Time: O(N)
  Space: O(1)
  '''
  dirtyBit = 1
  if (abs(len(s1) - len(s2))>1):
    return False
  i = 0
  j = 0
  
  while(i < len(s1) and j <len(s2)):
    if(s1[i] != s2[j]):
      dirtyBit -= 1
      # check replace
      if(i < (len(s1) - 1) and j < (len(s2) - 1) and s1[i+1] == s2[j+1] ):
        i += 1
        j += 1
      # check remove
      elif (i < (len(s1) - 1) and s1[i+1] == s2[j]):
        i += 1
      # check insert
      elif (j < (len(s2) - 1) and s1[i] == s2[j+1]):
        j += 1
      else:
        i += 1
        j += 1
    else:
      i += 1
      j += 1
  return dirtyBit >= 0

# print(oneAway('a','b'))
print(oneAway('pale', 'pas'))

# print(oneAway('pale','ple'))
# print(oneAway('pales','pale'))
# print(oneAway('pale','bale'))
# print(oneAway('pale','bake'))
# print(oneAway('pakeg','paxy'))

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = oneAway(test_s1, test_s2)
            print(test_s1, test_s2)
            self.assertEqual(actual, expected)

# if __name__ == "__main__":
    # unittest.main()
