'''friends = [("okot",22),("losika",17),("nicholas",56),("losio",68),("kiden",58)]
age = lambda data: data[1] >= 18
drinkers = list(filter(age,friends))

for i in drinkers:
    print(i)'''

names = [("losika",22),("losio",65),("eric",28),("jula",30),("kenyi",33),("kuli",19),("kade",14)]    
age = lambda age: age[1] > 24
driving_age = list(filter(age,names))
for i in driving_age:
    print(i)