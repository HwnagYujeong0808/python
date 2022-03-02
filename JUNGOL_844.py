# 1부터 입력 받은 수 까지의 짝수 출력


num = int(input("숫자를 하나 입력해주세요 >> "))
# 입력 받는 수는 2 이상 100 이하의 정수
while True:
    if (num < 2) or (num> 100) :
        num = int(input("숫자를 다시 입력해주세요 >> "))
    else:
        break
for i in range(1, num+1): # 입력받은 수가 짝수, 홀수 모두 해당
    if i % 2 ==0 : # 입력받은 수 중 짝수만 출력
        print(i, end=" ")