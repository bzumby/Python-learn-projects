

direction_words = ["north", "south", "east", "west", 
            "down", "up", "left", "right", "back"]
verbs = ["go", "stop", "kill", "eat"]
stop_words = ["the", "in", "of", "from", "at", "it"]
nouns = ["door", "bear", "princess", "cabinet"]

def scan(stuff):
    words = stuff.split()
    result = []
    for word in words:
        if convert_number(word): # checking if it is a digit
            result.append(tuple(("number", int(word))))
        elif word in direction_words:
            result.append(tuple(("direction", word)))
            # return result
        elif word in verbs:
            result.append(tuple(("verb", word)))
            # return result
        elif word in nouns:
            result.append(tuple(("noun", word)))
            # return result
        elif word in stop_words:
            result.append(tuple(("stop", word)))
    
    return result


def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return False
        

# scan("go 1")
# print(scan("go 1"))


