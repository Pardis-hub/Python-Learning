"""
FizzBuzz Challenge
Write a program that prints numbers from 1 to 100. For multiples of 3, print "Fizz" instead of the number,
and for multiples of 5, print "Buzz". For numbers which are multiples of both 3 and 5, print "FizzBuzz".
"""

def fizzbuzz():
    # Your code here
    for number in range(1,101,1):
        if number % 3 == 0 and number % 5 == 0:    #must be put first
            print('FizzBuzz')
        elif number % 3 == 0:
            print('Fizz')
        elif number % 5 == 0:
            print('Buzz')
        else:
            print(number)

fizzbuzz()