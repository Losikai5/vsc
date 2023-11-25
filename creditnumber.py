sumodd = 0
sumeven = 0
total = 0

card_number =input("enter number:")
card_number = card_number.replace("-","")
card_number = card_number.replace(" ","")
card_number = card_number[::-1]

for x in card_number[::2]:
    sumodd += int(x)

for x in card_number[1::2]:
    x = int(x*2)
    if x >= 10:
        sumeven += ( 1 + (x % 10))
    else:
            sumeven += x
total = sumeven + sumodd

if total % 10 ==0:
    print("valid")
else:
    print("invalid")    
