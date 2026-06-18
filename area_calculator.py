length = float(input("please type length:"))
width = float(input("please type width:"))
price = float(input("how much for 1 meter? :"))
area = length * width 
total_price = area * price

print (f"the total area is: {area}")
print (f"give the guy: ${total_price}")
