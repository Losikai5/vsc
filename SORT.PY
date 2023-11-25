'''students = ['okot','kade','kuli','losio','akota']
students.sort(reverse=False)
for i in students:
    print(i)'''

'''students = ('okot','kade','kuli','losio','akota')
sorted_students = sorted(students,reverse=True)
for i in sorted_students:
    print(i)'''

students = (('okot',"A",23),('mary','B',58))
grade = lambda grades:grades[1] 
#students.sort(key=grade) 
sorted_students = sorted(students,key=grade,reverse=True) 
#for i in sorted_students:
  #  print(i)
#print(sorted_students)