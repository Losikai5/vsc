store = [("shirt",20.00),
("pants",25.00),
("jacket",50.00),
("sockets",10.00)]

#to_euro = lambda data:(data[0],data[1]*0.82)
#store_euro = map(to_euro,store)
to_dollar = lambda data:(data[0],data[1]/0.82)
store_dollar = map(to_dollar,store)

for i in store_dollar:

    print(i)