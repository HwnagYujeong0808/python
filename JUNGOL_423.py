import math # 모듈 불러오기
class Score:
    def __init__(self, name, Korean, English):
        self.name = name
        self.Korean = Korean
        self.English = English

Junho = Score("Junho", 88, 100)
Seonbin = Score("Seonbin", 95, 96)
# math 모듈 사용하기 - floor (내림)
# round (반올림) 는 파이썬 내장 함수
K_avg = math.floor((Junho.Korean +Seonbin.Korean)/2)
E_avg = math.floor((Junho.English +Seonbin.English)/2)

print("avg {} {}".format(K_avg, E_avg))
