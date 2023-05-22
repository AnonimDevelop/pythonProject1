#  4.83, 4.84
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

summ = 0

# if num1 > 5:
#     summ = summ + num1
# if num2 > 5:
#     summ = summ + num2
# if num3 > 5:
#     summ = summ + num3
# if num4 > 5:
#     summ = summ + num4

if num1 % 3 == 0:
    summ = summ + num1
if num2 % 3 == 0:
    summ = summ + num2
if num3 % 3 == 0:
    summ = summ + num3
if num4 % 3 == 0:
    summ = summ + num4

print('summa = ' + str(summ))
