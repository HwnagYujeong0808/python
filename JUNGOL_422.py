class School:
    # 생성자 (초기값을 지정)
    def __init__(self, school="Jejuelementary", grade = "6학년"):
        self.school = school
        self.grade = grade
    # 정보 출력 함수
    def info(self):
        print("{} grade in {} school".format(self.grade, self.school))

# 객체 생성(인스턴스)
person1 = School() # 초기 생성자 유지
person2 = School("seoulelementary", "3학년")
person1.info() # info함수 불러오기
person2.info()

