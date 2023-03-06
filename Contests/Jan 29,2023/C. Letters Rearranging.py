tc=int(input())

for i in range(tc):
    word=input()
    
    fake=word.split("")
    # if word!=word[::-1]:
    #     print()
    for i in range(len(word)):
        word[i],word[i+1]=word[i+1],word[
        if word!=word[::-1]:
            fake=word
            break
        else:
            continue
    print(fake)

    
