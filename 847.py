a = list(map(int, input("점수를 입력해주세요 : ").split()))
avg = sum(a) /len(a) # 총합 / 길이
print("avg : {}".format(avg))

if avg >= 80:
    print("pass")
else:
    print("fail")