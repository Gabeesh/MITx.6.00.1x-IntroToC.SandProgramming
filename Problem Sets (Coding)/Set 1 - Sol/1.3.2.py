def solve(strs):
  maxx = strs[0]
  for i in xrange(len(strs)):
      for j in xrange(i+1, len(strs)):
          s = strs[i:j+1]
          if ''.join(sorted(s)) == s:
              maxx = max(maxx, s, key=len)
          else:
              break
  return maxx

print solve(s)