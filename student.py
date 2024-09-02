# 1.Write a code to get name and marks of a student.If a student scores less than 50 
# display that the student has failed. if the student scores between 50 and 60 then 
# display that the student has to improve.if the student scores between 60 and 70 then
# display put more effort.if the student scores between 70 and 80 then display good.if 
# the student scores between 80 and 90 then display v.good.if the student scores between 90 and 99 
# then display Excellent.if the student scores 100 then display keep it up.

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print(f"the name of student is {self.name}")
        print(f"marks secured by the student is {self.marks}")
        if(self.marks<50):
            print("failed")
        elif(self.marks>=50 and self.marks<=60):
            print("student has to improve")
        elif(self.marks>=60 and self.marks<=70):
            print("student has to put more effort")
        elif(self.marks>=70 and self.marks<=80):
            print("good")
        elif(self.marks>=80 and self.marks<=90):
            print("v.good") 
        else:
            print("EXCELLENT")
stu=student("MANI",70)
stu.display()
                                   