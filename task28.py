# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
# *Пример:*
# 2 2
# 4

def SumTwoNumbers(numA, numB):
   if numB == 0:
       return numA
   return 1 + SumTwoNumbers(numA, numB-1)

numberA = abs(int(input('Введите число A: ')))
numberB = abs(int(input('Введите число B: ')))

result = SumTwoNumbers(numberA, numberB)
print(f"Сумма чисел {numberA} и {numberB} = {result}")