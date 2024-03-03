#amirhossein
#40213160281828
def main():
    while(True):
        check = False
        inp = input("write:")  
        for x in inp:
            if(x == ","):
                check = True
                break
        if(inp.isnumeric()):
            out = int(inp)
        else:
            out = inp
        if(check == True):
            out = inp.split(",") 
        print(out)
        print(type(out))
        ex = input("press q to end||press anything to continue:")
        if(ex == "q"):
            break
main()        
   