import glob

def name(said):
    name=str(input().split(" "))
    x=glob.glob('your*')
    y=' '.join(x)
    if((name.find(y)+1)!=0 or (name.find("name")+1)!=0 or (name.find("call")+1)!=0):
        print("My Name is Mr.Bola!!What help do you need??")
        name="My Name is Mr.Bola!!What help do you need??"
    else:
        pass
    return name