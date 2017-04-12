import string

n = '1wordz'
x = string.ascii_lowercase
e = ""

for i in n:
  for i in n:
    if i not in x:
      e += i
    elif i == "z":
      e += 'a'
    else:
      d = x.index(i)
      e += x[d +1]
  print e
  break

for v in e:
  if v in "aeiou":
    print e[e.index(v)].upper()
    print e.replace(e[e.index(v)],e[e.index(v)].upper())
    continue
