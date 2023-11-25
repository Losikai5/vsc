'''towns_ugandan_c = {'kasese':40,'kampala':50,'masinde':80,'hioma':78}
#towns_ugandan_f = {key:((value - 32)/5/10)for(key,value) in towns_ugandan_c.items()}
#print(towns_ugandan_f)
towns_doouble = {key:value*2 for(key,value) in towns_ugandan_c.items()}
print(towns_doouble)'''
'''towns = {'hima':'sunny','hoima':'sunny','kable':'cold','bwera':'cold','kampala':'cold'}
sunny = {key:value for(key,value) in towns.items() if value == 'sunny'}
print(sunny)'''
'''towns2 = {'hima':45,'hoima':65,'kable':25,'bwera':35,'kampala':30}
weather = {key:'warm' if value >= 40 else 'cold' for(key,value) in towns2.items()}
print(weather)'''
def temp(value):
    if value >= 40:
        return "hot"
    elif value >= 26:

        return "warm" 
    else:
       
        return "cold" 

towns2 = {'hima':45,'hoima':65,'kable':25,'bwera':35,'kampala':30}
weather = {key:temp(value)for(key,value) in towns2.items()}
print(weather)

