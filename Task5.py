print('Введите трёхзначное число')
a = int (input())
sum = 0
while a > 0:
    end = a % 10
    sum = sum + end
    a = a / 10

print(int(sum))