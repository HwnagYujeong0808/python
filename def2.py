# shift + F10 실행
# RUN 표시 누르면 실행

def circle(r):
    circle_area =  r * r * 3.14
    return circle_area

user = int(input("반지름의 길이를 입력하시오 >>> "))
print(circle(user)) # r = 10 # 넓이 = 314.0