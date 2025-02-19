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
'''
1 
2 4 
3 5 7 
6 8 10 12 
9 11 13 15 17 
14 16 18 20 22 24 
'''
