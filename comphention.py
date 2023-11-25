'''suquare = []
for i in range(1,11):
    suquare.append(i*i)
print(suquare)'''


#square = [i*i for i in range(1,11)]  
#print(square)
students = [45,78,90,89,78,69,45,88,99,34,78]
#passed_students = [i for i in students if i > 60]
passed_students = [i if i > 60 else "FAILED"  for i in students]
print(passed_students)