#Staircase

def staircase(n):
    # Write your code here    
    symbol='#'    
    for i in range(n):
        result=(' ' * (n-i-1) + (symbol)*(i+1))
        print(result)
        

'''
for i in range(n):
    result = ' '*(n-i-1) +('#')*(i+1)
    print(result
'''