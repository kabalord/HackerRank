# Simple Array Sum

def simpleArraySum(ar):
    sum=0
    for i in range(len(ar)):
        sum+=ar[i]
    return sum
print(simpleArraySum([5,10,15,20]))
