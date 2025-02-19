from math import factorial
n=6
for i in range(n):
    for k in range(n-i+1):
        print(end=" ")

    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)),end=" ")
    print()
       1 
      1 1 
     1 2 1 
    1 3 3 1 
   1 4 6 4 1 
  1 5 10 10 5 1 

