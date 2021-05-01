def solution(a, b):
    answer = ''
    month=[31,29,31,30,31,30,31,31,30,31,30,31]
    day=['FRI','SAT','SUN','MON','TUE','WED','THU']
    tmp=0
    for i in range(a-1):
        tmp+=month[i]
    answer=day[(tmp+b)%7-1]
    return answer