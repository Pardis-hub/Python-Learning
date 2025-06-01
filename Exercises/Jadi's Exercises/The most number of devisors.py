
def input_number():
    num = int(input())
    devisor = 2
    for i in range(2 , int(num/2)+1):
        if num % i == 0:
            devisor += 1
    return num, devisor


num, devisor = input_number()
max_devisor = devisor
max_num = num
print(num, devisor)
for i in range(19):
    num, devisor = input_number()
    print(num , devisor)
    if max_devisor < devisor:
        max_devisor = devisor
        max_num = num
    elif max_devisor == devisor and num > max_num:
        max_num = num

print(f"{max_num} has the most devisors which is {max_devisor}")



