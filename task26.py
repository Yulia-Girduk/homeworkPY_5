# Задача 26:  Напишите программу, которая на вход принимает 
# два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 

def ApowerB(numA, numB):
   if numB == 0:
       return 1 
   return numA * ApowerB(numA, numB-1)

numberA = abs(int(input('Введите число A: ')))
numberB = abs(int(input('Введите число B: ')))

result = ApowerB(numberA, numberB)
print(f"Число {numberA} в степени {numberB} = {result}")