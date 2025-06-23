# star pattern n=3
'''  
  *
 ***
***** 
'''

n = int(input("Enter row number: ")) 

for i in range(1, n+1):
    print(" " * (n-i), end ="")
    print("*" * (2*i-1), end ="")
    print("")  # blank print - to get the next line. \n - dile print er ekta line
                # abar \n er ekta line. so gap bere jabe.







