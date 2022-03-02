def function(a, b):
    return a**b

a = int(input("10 이하의 정수를 입력하시오 >> "))
while(a > 10) : # 10보다 a가 클 때
    a = int(input("10 이하의 정수를 다시 입력하시오 >> "))
    # a가 10보다 작아지면 while문 빠져나감

b = int(input("10 이하의 정수를 입력하시오 >> "))
while(b > 10) : # 10보다 a가 클 때
    b = int(input("10 이하의 정수를 다시 입력하시오 >> "))
print(function(a, b))
