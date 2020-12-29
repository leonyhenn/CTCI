def checkPerm(s1,s2):
  if len(s1) != len(s2):
    return False
  seen = dict()
  for c1 in s1:
    if c1 not in seen:
      seen[c1] = 1
    else:
      seen[c1] += 1
  
  for c2 in s2:
    if c2 not in seen:
      return False
    else:
      if seen[c2] > 0:
        seen[c2] -= 1
      else:
        return False

  return True

assert(checkPerm('abc','cba') == True)
assert(checkPerm('abcd','cbad') == True)
assert(checkPerm('abbb','abbc') == False)
assert(checkPerm('abb','abbb') == False)
assert(checkPerm('abcd', 'bacd') == True)
assert(checkPerm('3563476', '7334566') == True)
assert(checkPerm('wef34f', 'wffe34') == True)
assert(checkPerm('abcd', 'd2cba') == False)
assert(checkPerm('2354', '1234') == False)
assert(checkPerm('dcw4f', 'dcw5f') == False)

      
  