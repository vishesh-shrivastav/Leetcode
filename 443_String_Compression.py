"""
This is the solution to CTCI 1.6
May not be the exact solution for LC443
"""
def string_compression(s):
  compressed = []
  counter = 0

  for i in range(len(s)):
    if i != 0 and s[i-1] != s[i]:
      compressed.append(s[i-1] + str(counter))
      counter = 0
    counter += 1
  
  compressed.append(s[-1] + str(counter))

  return min(s, ''.join(compressed), key = len)

print(string_compression("aabcccccaaa"))
print(string_compression("abcdef")) 
