'''def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("losika")
    print(text)
hello(loud)
hello(quiet)'''

'''def bro(self):
    return self.upper()
def sis(self):
    return self.lower() 
def okot(person):
    self = person("kade")
    print(self)   

okot(bro)       
okot(sis) '''

def divisor(y):
    def divided(x):
        return x/y
    return divided
okot = divisor(2)
print(okot(10))     
