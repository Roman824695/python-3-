number = int(input('Введите число длины списка  :  '))
char = []

for i in range(number): 
  from random import randint
  char.append(randint(0, 100))
print(char)

num = int(input('Введите искомое число :  '))
sum = 0

   
for i in range(len(char)):
  if char[i] == num:
    sum += 1
  
   

print(f"число {num} встречается : {sum} раз ")
