# 1부터 15까지 차례로 출력하는 프로그램

# while 문 이용
A = 1 # 변수  A에 1 할당
while A <= 15 :
    print(A, end = " ") # 띄어쓰기 후 출력
    A += 1

# for 문 이용
for A in range(15) : # 0-14 (15)
    print(A+1, end= " ")


