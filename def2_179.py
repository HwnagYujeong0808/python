# 반올림 round()
#  함수 2 형성평가 5

def avg(num1, num2, num3) :
    sum = num1 + num2 + num3
    avg = sum / 3
    avg_round = round(avg)
    return avg_round # 반올림된 평균
a = float(input("실수를 입력해주세요 >> "))
b= float(input("실수를 입력해주세요 >> "))
c = float(input("실수를 입력해주세요 >> "))
print(avg(a, b, c))