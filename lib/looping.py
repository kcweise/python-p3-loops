#!/usr/bin/env python3

def happy_new_year():
    i= 10
    while i>=0:
        if i>0:
            print(f"{i}")
        else:
            print("Happy New Year!")
        i-= 1
    pass

def square_integers(int_list): 
    return [num*num for num in int_list]
    pass

def fizzbuzz():
    i = 1
    while i<=100:
        if i % 3 == 0 and i % 5==0:
            print("FizzBuzz")
            
        elif i % 3 ==0:
            print("Fizz")
            
        elif i % 5 == 0:
            
            print("Buzz")
        else:
            print(i)
        i+=1
    pass
