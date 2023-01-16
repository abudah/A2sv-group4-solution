from collections import defaultdict

testCases=int(input())
for i in range(testCases):
        n=int(input())
        integers=[int(i) for i in input().split()]
        strings=input()
        flag="YES"
        locations=defaultdict(list)

        for i in range(len(integers)):
            locations[integers[i]].append(i)

        for key,values in locations.items():
            char=strings[values[0]]
            for i in values:
                if strings[i]!=char:
                    flag="NO"
        print(flag)
