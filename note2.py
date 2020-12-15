def getTalk(kind="shout"):
    def shout(word="yes"):
        return word.capitalize()+"!"
        
    def whisper(word="yes"):
        return word.lower()+"..."
        
    if kind=="shout":
        return shout
        
    else:
        return whisper
     
     
#talk=getTalk()
print(getTalk()())
#print(talk())