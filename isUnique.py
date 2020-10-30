# Space: O(n). 
# Time: O(n). 

def isUnique(s):
  seen = dict()
  for c in s:
    if c not in seen:
      seen[c] = 1
    else:
      return False
  return True

assert isUnique('abcd') == True
assert isUnique('s4fad') == True
assert isUnique('23ds2') == False
assert isUnique('hb 627jh=j ()') == False