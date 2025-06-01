from math import sqrt
n = int(input('Enter how many numbers: '))
number = []
truncated_number = []
for i in range(n):
    number.append(float(input('Enter the number: ')))

for i in number:
    print("%.4f" % int((sqrt(i) * 10000)/10000))

