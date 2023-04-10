num1 = input('Enter top number: ')
try:
    num1 = int(num1)
except:
    if type(num1) == str:
        print('Error: Numbers must only contain digits. ')
        quit()
if num1 > 9999:
    print('Error: Numbers cannot be more than four digits. ')
    quit()

print('')

print(f'  {num1}\n------')

print('')

num2 = input('Enter bottom number: ')
try:
    num2 = int(num2)
except:
    if type(num2) == str:
        print('Error: Numbers must only contain digits. ')
        quit()
if num2 > 9999:
    print('Error: Numbers cannot be more than four digits. ')
    quit()

print('')

print(f'  {num1}\n  {num2}\n------')

print('')

sym = input('Add (enter +) or subtract (enter -): ')
if sym == '+':
    result = num1 + num2
elif sym == '-':
    result = num1 - num2
else:
    print("Error: Operator must be '+' or '-'")
    quit()


num1 = str(num1)
num2 = str(num2)
result = str(result)

print('')

print(f'  {num1}\n{sym} {num2} \n------\n  {result}')
