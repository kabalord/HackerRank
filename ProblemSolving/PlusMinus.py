# plusMinus

def plusMinus(arr):
    # Write your code here
    positive=0
    negative=0
    zero=0
    
    for i in arr:
        if i>0:
            positive+=1
        elif i<0:   
            negative+=1
        else:
            zero+=1
    res = [positive/len(arr), negative/len(arr), zero/len(arr)]
    
    for i in res:
        print(i)

plusMinus([-4, 3, -9, 0, 4, 1])
            

