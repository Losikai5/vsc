class Dad:
    tall = True
    honest = True
    Lair = False
    def responsibility(self):
        print("PAYS FEES FOR CHILDREN")
class Jula(Dad):
    rich = True
    hardworking = True
    def leader(self):
        print("HE LEADS OTHERS")
class Chance(Dad):
    lazy = True
    kind = True
    def drunk(self):
        print("ALWAYS HIGH")

LENA = Jula()
LUBANG = Chance()
print(LENA.tall)
print(LENA.Lair)
print(LUBANG.honest)
LENA.leader()
LUBANG.drunk()
print('''THE BEGININNG IS ALWAYS HARD
SO BE STRONG MY BOY ''')