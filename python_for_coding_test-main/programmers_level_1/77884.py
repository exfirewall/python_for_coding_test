from math import sqrt

def divisor(left, right):
    divisors=[0 for _ in range(right-left+1)]
    for i in range(left, right+1):
        for j in range(1, int(sqrt(i))+1):
            if i%j==0:
                if i//j==j:
                    divisors[i-left]+=1
                else:
                    divisors[i-left]+=2
    return divisors

def solution(left, right):
    answer=divisor(left, right)
    hap=0
    for i in range(left,right+1):
        if answer[i-left]%2==0:
            hap+=i
        else:
            hap-=i
    return hap

print(solution(13,17))