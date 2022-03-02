class School:
    # 생성자 정의
    def __init__(self, name, school, grade):
        self.name = name
        self.school = school
        self.grade = grade
    def info(self):
        print("Name : {}\nSchool : {}\nGrade : {}"\
              .format(self.name, self.school, self.grade))

name = input("이름 : " ) # Songjunhyuk
school = input("학교 : ") # Beolmal
grade = int(input("학년 : ")) # 6
# 객체 생성하기
person1 = School(name, school, grade)
person1.info()