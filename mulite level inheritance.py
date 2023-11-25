class Phone:
    working = True
class Button_phone(Phone):
    def buttons(self):
        print("The phone has buttons") 


class Smart(Button_phone):
    def screen(self):
        print("It has a touch screen")


Smart1 = Smart()
Smart1.buttons()
Smart1.screen()
print(Smart1.working)