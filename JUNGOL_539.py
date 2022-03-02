# 539번
# 정수를 입력 받다가 100 이상의 수가 입력 되면 입력된 합계 & 평균 출력

a = [] # 빈 리스트 생성

user = int(input("숫자를 입력해주세요 >> "))
sum = 0
i = 0
while True :
    a.insert(i, user) # 인덱스 지정, 해당 인덱스에  user값 저장
    sum += a[i]
    if a[i] >= 100 :
        break
    i += 1
    user = int(input("숫자를 입력해주세요 >> "))
print(sum)
print("%.1f"%(sum/len(a))) # 소수점 첫째 자리수까지 출력
