marks = [23,45,78,90,45]


def average(marks):
    sum_marks = sum(marks)
    numbreofsubjects = len(marks)
    average_got = sum_marks/numbreofsubjects
    return average_got

def computer_grade(ave):
    if ave >= 60:
        grade = 'A'
    elif ave >= 80:
        grade = 'B'
    else:
        grade = 'c'
    return grade

ave = average(marks)
print('the average :', ave)
graded = computer_grade(ave)
print('the grade is', graded)

















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































  