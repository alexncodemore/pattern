odd=1
even=2
for i in range(1,7):
    for j in range(1,i+1):
        if i%2==0:
            print(even,end=" ")
            even+=2
        else:
            print(odd,end=" ")
            odd+=2
    print()
