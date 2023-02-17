import v1

text=input("give input")
longWord= "fwuehuewfjhwriafoiaerf "+text
longWord=list(longWord.split(" "))
print(longWord)
if "say" in longWord:
    indexOfsay=longWord.index("say")
    del longWord[:indexOfsay]
    
print(longWord)