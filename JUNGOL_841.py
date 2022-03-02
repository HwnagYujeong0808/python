#  841 : for문 사용한 반복 제어문

# 자연수 n을 입력받아서,
# 리스트 [n, n-1, ... ,1]을 출력하는 프로그램

a = [] # 빈리스트를 생성
user = int(input("숫자를 입력하세요 : "))

# user, user-1, user-2, ... ,1 (-1씩 감소)
for i in range(user, 0, -1):
    a.append(i)
print(a)

