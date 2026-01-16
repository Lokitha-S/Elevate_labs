name=input("Enter your name:")
roll_no=int(input("Enter ur roll no:"))
price=float(input("enter the price:"))
qualified=True
#the type of each variable using type().
print(type(name))
print(type(roll_no))
print(type(price))
print(type(qualified))
#arithmetic operations using numeric values
a=int(input('a:'))
b=int(input('b:'))
add=a+b
sub=a-b
mul=a*b
div=a/b

print('add:',add)
print('subtraction:',sub)
print('multiplication:',mul)
print('division:',div)
#Convert string input to integer and float using type casting
names='100'
nameint=int(names)
namefloat=float(names)
print("name in int:",nameint)
print("name in float:",namefloat)

#Handle invalid input using basic error handling.
na = 'Hlo'
try:
    naint = int(na)
    nafloat = float(na)
    print("name in int:", naint)
    print("name in float:", nafloat)
except ValueError:
    print(f"Error: Cannot convert '{na}' to a number&float.")

#Concatenate strings and numbers properly
print(f"Roll no:{roll_no} name is {name}")

#Demonstrate dynamic typing by reassigning variable values.
ty=13
print(f"ty:{ty} Type:{type(ty)}")
ty="Hlo"
print(f"ty:{ty} Type:{type(ty)}")

