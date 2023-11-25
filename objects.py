class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def checks_marks(self):
        if self.marks >= 60:
           return 'passed'
        else:
            return 'falied'              



student1 = student('okot',97)
student2 = student('losika', 45)
did_pass = student1.checks_marks()
print(did_pass)
did_pass = student2.checks_marks()
print(did_pass)





   

 