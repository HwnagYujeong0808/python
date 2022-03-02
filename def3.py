#  반복문
#  for 문
def square(r):
    count = 1
    for i in range(r):
        for j in range(r):
            print("%d"%count, end = " ")
            count += 1
        print("")
user = int(input("숫자를 입력하시오 >> "))
square(user)



