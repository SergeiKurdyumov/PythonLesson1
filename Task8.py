print('Введите размер и сколько отломить')
n = int(input())
m = int(input())
k = int(input())
if k <= n*m and (k % m ==0 or k % n == 0):
    print('yes')
else:
    print('no')