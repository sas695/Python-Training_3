def squareplustwo(n):
    return n*n+2;


def ispalindrome(s):
    reversed_s = s[::-1]
    if s==reversed_s:
        return True     
    else:
        return False


def secondgreatest(l):
    aList = sorted(l)
    second_greatest = aList[-2]
    return second_greatest


def flip(d):
    new_d={}
    dup=[]
    for key, value in d.items():
        if value in dup:
            return None
        else:    
            new_d[value] = key    
            dup.append(value)     
    return new_d  
    

def weightedsum(l,d):
    sum=0
    for e in l:
        sum=sum+d[e]
    return sum


#print(squareplustwo(10))
#print(ispalindrome('racecar'))
#print(secondgreatest([1,5,4,2,3]))
#print(flip({'alpha':10, 'beta':20, 'gamma':10}))
#print (weightedsum([1,2,3,2,1], {1:5.0, 2:0,3:1.2}))