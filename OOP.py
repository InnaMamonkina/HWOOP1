class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name) 
    def rate_hw(self, student, course, grade):
        if isinstance(student, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
     def __rate_hw(self, dic):
        sum = 0
        count = 0
        for m in dic.values():
            for i in m:
                sum += i
                count += 1
        if count == 0:
            return "Оценок еще нет!"
        return round(sum / count, 1) 
    def __str__(self):
        res = f'Имя:{self.name} \n Фамилия:{self.surname} \n Средняя оценка за домашние задания:{self.__rate_hw} \n Курсы в процессе изучения: {.join(self.courses_in_progress)} \n Завершенные курсы:{.join(self.finished_courses)}'
        return res     
    
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
 
class Lecturer (Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
    def __average_rating(self, dic):
        sum = 0
        count = 0
        for m in dic.values():
            for i in m:
                sum += i
                count += 1
        if count == 0:
            return "Оценок еще нет!"
        return round(sum / count, 1) 
    def __str__(self):
        res = f'Имя:{self.name} \n Фамилия:{self.surname} \n Средняя оценка за лекции:{self.__average_rating}'
        return res




  
class Reviewer (Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'  
    def __str__(self):
        res = f'Имя:{self.name} \n Фамилия:{self.surname}'
        return res

def __lt__(self.average_rating, self.rate_hw):
    return len(self.average_rating) < len(self.rate_hw)




some2_student = Student('Anna', 'Stepanova', 'your_gender')
some2_student.courses_in_progress += ['Python']

some2_reviewer = Reviewer('Pavel', 'Petrov')
some2_reviewer.courses_attached += ['Python']

some2_lecturer = Lecturer('Fedor', 'Popov')
some2_lecturer.courses_attached += ['Python']

some2_reviewer.rate_hw(some2_student, 'Python', 8)
some2_reviewer.rate_hw(some2_student, 'Python', 2)
some2_reviewer.rate_hw(some2_student, 'Python', 9)

some2_student.rate_hw(some2_lecturer, 'Python', 6)
some2_student.rate_hw(some2_lecturer, 'Python', 7)
some2_student.rate_hw(some2_lecturer, 'Python', 9)

print(some2_reviewer)
print(some2_lecturer)
print(some2_student)
print(some2_lecturer.average() > some2_student.average())



def average_rating_for_course(course, student_list):
    sum_rating = 0
    quantity_rating = 0
    for stud in student_list:
        for course in stud.grades:
            stud_sum_rating = stud.av_rating_for_course(course)
            sum_rating += stud_sum_rating
            quantity_rating += 1
    average_rating = round(sum_rating / quantity_rating, 2)
    return average_rating

  
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
 
print(best_student.grades)