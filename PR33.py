def Task1():
	number = 424+2*(-2)*424+2*(-2)
	print("Number: " + number)

def Task2():
	number = 9*19-int(float(9*19))
	print("Number: " + number)

def Task3():
	x = input()
	y = input()
	print(int(x) + int(x))
	
def Task4(minutes):
	hours = int(int(minutes) / 60)
	minutes %= 60
	print(hours)
	print(minutes)

def Task5(hoursSleep, minutesSleep, timeToSleep):
	weakUpHours = int(hoursSleep) + int(int(timeToSleep) / 60)
	weakUpMinutes = int(minutesSleep) + int(int(timeToSleep) % 60)
	print(weakUpHours)
	print(weakUpMinutes)
	
def Task6(recomendSleep, higestToSleep, currentSleep):
	if(currentSleep == recomendSleep):
		print("Это норма")
	elif(currentSleep > recomendSleep):
		print("Пересып")
	else:
		print("Недосып")

def Task7(year):
	if((year % 4 == 0 and year % 100 !=0) or year % 400 == 0):
		print("Високосный")
	else:
		print("Невисокосный")

def Task8(firstNum, secondNum, operator):
	if(operator == '+'):
		print(int(firstNum) + int(secondNum))
	elif(operator == '-'):
		print(int(firstNum) - int(secondNum))
	elif(operator == '/'):
		if(secondNum == 0):
			print("Деление на ноль")
			return
		print(int(firstNum) / int(secondNum))
	elif(operator == '*'):
		print(int(firstNum) * int(secondNum))
	elif(operator == "mod"):
		print(int(firstNum) % int(secondNum))
	elif(operator == "pow"):
		print(pow(firstNum, secondNum))
	elif(operator == "div"):
		print(int(firstNum) // int(secondNum))
			
def Task9(typeShape, a = 0, b = 0, c = 0, r = 0):
	if(typeShape == "Triangle"):
		p = (a + b + c) / 2.0  # Полупериметр
		S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
		print("Square =", S)
	elif(typeShape == "Rectangle"):
		print(a*b)
	elif(typeShape == "Circle"):
		radius = float(a)
		S = 3.14 * radius * radius
		print("Square =", S)
		
def Task10(a, b, c):
	if(a > b):
		if(a > c):
			print("Max", a)
			if(b > c):
				print("Min", c)
				print("Average", b)
			else:
				print("Min", b)
				print("Average", c)
		else:
			print("Max", c)
			print("Min", b)
			print("Average", a)
	elif(a > c):
		print("Max", b)
		print("Min", c)
		print("Average", a)
	elif(c > b):
		print("Max", c)
		print("Min", a)
		print("Average", b)
	else:
		print("Max", b)
		print("Min", a)
		print("Average", c)

def Task10OtherMethod(a, b, c):
	array = []
	array.append(a)
	array.append(b)
	array.append(c)
	array.sort()
	print(array[2]) #Max
	print(array[1]) #Average
	print(array[0])	#Min

def Task11(countProg):
	if (countProg % 10 == 1 and countProg % 100 != 11):
		print(countProg, "программист")
	elif (countProg % 10 in [2, 3, 4] and not countProg % 100 in [12, 13, 14]):
		print(countProg, "программиста")
	else:
		print(countProg, "программистов")
