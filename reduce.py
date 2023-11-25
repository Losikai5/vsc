import functools
letters = ['L','O','S','I','K','A']
WORD = functools.reduce(lambda X,Y: X+Y,letters)
print(WORD)

NUMBERS = [2,3,4,5,7,8]
FACTOR = functools.reduce(lambda X,Y:X*Y,NUMBERS)
print(FACTOR)
names = ["losika", "nicholas","losio"]
name = functools.reduce(lambda x,y:x+y,names)
print(name)
