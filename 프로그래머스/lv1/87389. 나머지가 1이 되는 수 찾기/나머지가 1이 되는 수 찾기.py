def solution(n):
    answer = 0
    for i in range(2, (n-1) +1) : #2부터~반값까지 
        if (n-1) % i == 0: #약수가 있다면
            answer = i 
            break #탈출
        else: 
            answer = n-1 #약수가 없다면 본인
    return answer