testCases=int(input())

for i in range(testCases):
    word=input()
    if len(word)>10:
        output=word[0]+str(len(word)-2)+word[-1]
        print(output)
    else:
        print(word)
