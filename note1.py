def talk():
    def whisper(word="yes"):
        return word.lower()+"..."
        
    print(whisper())
    
    
    
    
talk()

try:
    print(whisper())
except NameError as e:
    print(e)