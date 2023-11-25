menu = {'soda': 2000,'pizza':35000,"rice":5000,'posho':6000}
cart = []
total = 0 


print("................MENU................")


for keys,values in menu.items():
    print(f"{keys:10}: shs.{values:.2f}")

print("................MENU................")    



while True:    
     food = input("ENTER UR CHOICE:").lower()
     if food == 'k':
        break
     elif menu.get(food) is not None:
        cart.append(food)
for food in cart:
    total += menu.get(food)
    print(food)


print(f"YOUR TOTAL IS SHS.{total:.2f}")
        
