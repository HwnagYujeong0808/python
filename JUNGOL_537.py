user = int(input("숫자를 입력해주세요 >> "))
i = 1
sum = 0

# 100보다 user 가 클 때
while user > 100:
    user = int(input("숫자를 다시 입력해주세요 >> "))

while i <= user :
    sum += i
    i += 1
print("숫자의 총합은 {}입니다.".format(sum))