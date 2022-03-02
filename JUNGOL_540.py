# 540

# break - while True 무한루프 생성
while True :
    user = int(input("숫자를 입력해주세요 : "))
    if user % 3 == 0 :
        print(user//3)
    elif user % 3 != 0 :
        if user == -1 :
            break
        continue
    elif user == -1 :
        break
