# 583 : 함수2 - 자가진단 5
# 반올림
# 올림 : math.ceil(소수)
# 내림 : math.floor(소수)
# -1000 이상 1000 이하
import math
a = float(input("첫 번째 실수를 입력해 주세요 >> "))
b= float(input("두 번째 실수를 입력해 주세요 >> "))
c = float(input("세 번째 실수를 입력해 주세요 >> "))

if a > b :
    max = a
    min = b
else :
    max = b
    min = a
if c > max :
    max = c
if c <min :
    min = c
print(math.ceil(max))
print(math.floor(min))
if (a != max) and (a != min):
    middle = a
if (b != max) and (b != min):
    middle = b
if (c != max) and (c != min):
    middle = c

print(round(middle))