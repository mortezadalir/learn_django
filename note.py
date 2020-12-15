def shout(word="yes"):
    return word.capitalize()+"!"

#print(shout("morteza"))
#print(shout())
scream=shout

print(scream())
del shout
try:
    print(shout())
except NameError as e:
    print(e)
    
print(scream("ali"))