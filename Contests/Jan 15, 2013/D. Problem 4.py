inputs=input()

hello=['o','l','l','e','h']
for i in inputs:
    if hello[-1]==i:
        hello.pop()
        if len(hello)==0:
             break
if hello:
    print("NO")
else:
    print("YES")
