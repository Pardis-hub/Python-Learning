def check_laptops(number, cost, quality):
    for i in range(n - 1):
        if quality_list[i] > quality_list[i + 1]:
            if cost_list[i] < cost_list[i + 1]:
                return 'happy irsa'
        if quality_list[i] < quality_list[i + 1]:
            if cost_list[i] > cost_list[i + 1]:
                return 'happy irsa'

    return 'poor irsa'

n = int(input('Please enter number of laptops: '))
cost_list = []
quality_list = []
for i in range(n):
    cost, quality = input('Please enter cost and quality of the laptop separated by a space: ').split()
    cost_list.append(int(cost))
    quality_list.append(int(quality))

result = check_laptops(n,cost_list, quality_list)
print(result)


