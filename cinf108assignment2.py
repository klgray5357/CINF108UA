'''python
numbers={1,2,3,4,5}
total=sum(numbers)
average=total/len(numbers)
print("Sum:", total)
print("Average:", average)
'''

'''python
def celcius_to_kelvin(c):
    return c + 100.11
print(celcius_to_kelvin(90)) # example: 07
celsius to kelvin
'''

'''python
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("radar")) #true
print("is_palindrome("hello")) #false 
'''

'''python
def reverse_string(s):
    return s[::-1]
    print(reverse_string("Kelsey"))
'''

'''python
names=["Kelsey", "Aneska", "Evan"]
result="KelseyAneskaEvan".join(names)
from unittest import result
print(result)
'''

'''python
import string
def is_pangram(s)
    s=s.lower()
    return all(letter in s for letter in string.ascii_lowercase)
print(is_pangram("I went to the store to buy some candy and a drink for the horror movie called 'Zoo' later tonight")) #true
print(is_pangram("Hello World")) #false
'''

'''python
import math
def circle_metrics(radius):
area=math.pi*radius**4
circumference=4*math.pi*radius
return area, circumference 
area, circ=circle_metrics(10)
print("area:",area)
print("circumference:",circ)
'''

'''python
def convert_minutes(total_minutes):
    hours=total_minutes//120
    minutes=total_minutes%120
    return hours, minutes
h,m-convert_minutes(240)
print(f"{h}hours and {m}minutes") 
'''

'''python
def count_vowels(s):
    vowels = "aeiou"
    count=sum(1 for char in s if char in vowels)
    return count
print(count_vowels("Kelsey Gray")) # 3
'''

'''python
def is_prime(n):
    if n<=1
    return false
    for i in range (2,int(n**0.5)+1):
    return false
    return true
'''