test_cases=int(input())

for i in range(test_cases):
        sentence=input().split()
        sorteds=['']*len(sentence)
        
        for words in sentence:
                order=0
                filtered=[]
                for chars in words:
                        if chars.isdigit():
                                order=int(chars)
                        else:
                                filtered.append(chars)
                sorteds[order-1]=''.join(filtered)
        print(' '.join(sorteds))
