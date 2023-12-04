#This Program calculates and displays travel expense
#October 19, 2023
#CTI-110 P1HW2-Travel Expense
#This program should store the grades entered in a list





print('This program calculates and displays travel expenses')
print()
budget = int(input('Enter Budget:'))
print()
loc = input('Enter your travel destination:')
print()
gas = int(input('How much do you think you will spend on gas?'))
print()
accom = int(input('Approximately, how much will you need for accomodation/hotel?'))
print()
food = int(input('Last, how much do you need for food?'))

#Total Values
exp = food + gas + accom
remain = budget - exp

print()
print('----------Travel Expenses----------')
print('Location:',loc)
print('Initial Budget: ',budget)
print()
print('Fuel:',gas)
print('Accomodation:',accom)
print('Food:',food)
print()
print('Remaining Balance:',remain)
