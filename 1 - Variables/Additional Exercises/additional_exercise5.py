#16-01-2012
#additional exercise 5
#sample solution



lift():
liftW = input("13W")
liftH = input("10H")
liftD = input("20D")
fridge():
fridgeW = input("5W")
fridgeH = input("3H")
fridgeD = input("11D")
volume("lift + fridge"):
liftV = liftW * liftH * liftD
fridgeV = fridgeW * fridgeH * fridgeD
liftSpace = liftV - fridgeV
print("The lift's volume is {2600}.".(liftV))
print("The fridge's volumne is {165}.".(fridgeV))
print("The lift has {2435} of remaining space.".(liftSpace))
