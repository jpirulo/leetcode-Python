result = 38
print(len(str(result)))
while len(str(result)) != 1:
    temp=0
    for i in str(result):
        print(i)
        temp +=int(i)
        print(f"temp {temp}")
        result=temp
#print(len(str(result)))