# 양수, 음수 판별 후 0일때 종료 하는 프로그램

# break문은 while문 안에서 작동
while True :
    num = int(input("숫자를 입력해주세요 >> "))
    if num > 0 :
        print("양수입니다~")
    elif num < 0:
        print("음수입니다~")
    else : # else문에는 조건 X
        print("프로그램 종료")
        break


