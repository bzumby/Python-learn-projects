import string

def LetterChanges(str):
    n = str
    x = string.ascii_lowercase
    e = ""

    # code goes here 
    



    for i in n:
        for i in n:
            if i not in x:
                e += i
            elif i == "z":
                e += 'a'
            else:
                d = x.index(i)
                e += x[d +1]
        break

    for v in e:
        if v in "aeiou":
            e = e.replace(e[e.index(v)],e[e.index(v)].upper())
    
    return e
    
# keep this function call here  
print LetterChanges(raw_input())
