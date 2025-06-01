import csv
# For the average
from statistics import mean


def calculate_averages(input_file, output_file):

    rows = []
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)

    means = {}
    names = []
    grades = []
    for row in rows:
        for grade in row[1:]:
            grades.append(float(grade))
        average = mean(grades)
        names.append(row[0])
        means[row[0]] = average
        grades = []

    with open(output_file, 'w') as file:
        writer = csv.writer(file)
        for i in range(len(names)):
            writer.writerow([names[i], means[names[i]]])




def calculate_sorted_averages(input_file, output_file):

    rows = []
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)

    means = {}
    names = []
    grades = []
    averages = []
    for row in rows:
        for grade in row[1:]:
            grades.append(float(grade))
        average = mean(grades)
        averages.append(average)
        names.append(row[0])
        means[row[0]] = average
        grades = []

    sorted_avg_list = sorted(means.items(), key=lambda x: (x[1], x[0]))

    with open(output_file, 'w') as file:
        writer = csv.writer(file)
        for name, avg in sorted_avg_list:
            writer.writerow([name, avg])



def calculate_three_best(input_file, output_file):
    rows = []
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)

    means = {}
    names = []
    grades = []
    averages = []
    for row in rows:
        for grade in row[1:]:
            grades.append(float(grade))
        average = mean(grades)
        averages.append(average)
        names.append(row[0])
        means[row[0]] = average
        grades = []

    sorted_avg_list = sorted(means.items(), key=lambda x: (-x[1], x[0]))

    with open(output_file, 'w') as file:
        writer = csv.writer(file)
        i = 1
        for name, avg in sorted_avg_list:
            if i < 4:
                writer.writerow([name, avg])
            i += 1



def calculate_three_worst(input_file, output_file):
    rows = []
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)

    means = {}
    names = []
    grades = []
    averages = []
    for row in rows:
        for grade in row[1:]:
            grades.append(float(grade))
        average = mean(grades)
        averages.append(average)
        names.append(row[0])
        means[row[0]] = average
        grades = []

    sorted_avg_list = sorted(means.items(), key=lambda x: (x[1], x[0]))

    with open(output_file, 'w') as file:
        writer = csv.writer(file)
        i = 1
        for name, avg in sorted_avg_list:
            if i < 4:
                writer.writerow([avg])
            i += 1


def calculate_average_of_averages(input_file, output_file):
    rows = []
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)

    means = {}
    names = []
    grades = []
    averages = []
    for row in rows:
        for grade in row[1:]:
            grades.append(int(grade))
        average = mean(grades)
        averages.append(average)
        grades = []

    with open(output_file, 'w') as file:
        writer = csv.writer(file)
        average_of_averages = mean(averages)
        writer.writerow([average_of_averages])


calculate_three_worst('data.csv', 'three_worst_averages.csv')




