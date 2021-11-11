print(2+3)

print(int.__mul__(2,3))

class student_mark:

    def __init__(self, mark1, mark2):
        self.mark1=mark1
        self.mark2=mark2
    
    def __add__(self,other):
        m1=self.mark1+other.mark1
        m2=self.mark2+other.mark2
        return student_mark(m1,m2)

student_mark1=student_mark(50,35)
student_mark2=student_mark(40,60)

student=student_mark1+student_mark1
print(student.mark1)
print(student.mark2)
