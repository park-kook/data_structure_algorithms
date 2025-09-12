def matches_abbrev(word: str, pattern: str)->bool:
  """
  check if pattern maches word, where digits in pattern mean skipped characters
  example: "internationalization", "i18n"->True
  """
  i = 0 #pointer for word
  j = 0#pointer for pattern
  n, m = len(word), len(pattern)

  while j < m:
    if pattern[j].isdigit():
      if pattern[j] == '0' and pattern[j+1].isdigit(): #reject leading zero in numbers like "01" (common interview requirement)
        return False
      num=0
      while j<m and pattern[j].isdigit():
        num = 10*num + int(pattern[j])
        j+=1
      i+=num
      if i> n:
        return False
    else:
      if i>=n or word[i] != pattern[j]:
        return False
      i+=1
      j+=1
  return i == n


