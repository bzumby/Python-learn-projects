from string import ascii_lowercase

def LetterChanges(str):
    x = ascii_lowercase
    e = ""
    str = str.lower()
    # code goes here 
    



    
    for i in str:
      if i not in x:
        e += i
      elif i == "z":
        e += 'a'
      else:
        d = x.index(i)
        e += x[d +1]

    for v in e:
        if v in "aeiou":
            e = e.replace(e[e.index(v)],e[e.index(v)].upper())
        else:
          return e
    
# keep this function call here  
print LetterChanges(raw_input())
