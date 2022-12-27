if __name__ == '__main__':
    N = int(input())
    theList=[]
    commands=[]
    for i in range(N):
        commands.append(input())
    for comArgs in commands:
        if comArgs=="print":
            print(theList)
        else:
            command=comArgs.split()
            comArg=','.join(command[1:])
            exec("theList."+command[0]+'('+comArg+')')
