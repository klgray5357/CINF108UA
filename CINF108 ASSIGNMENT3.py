
length = 8
width = 4
area = length * width
print("Area of the rectangle:", area)  # output: Area of the rectangle: 32


name = "kelsey"
age = 17
print(f"hello {name}, you are {age} years old its nice to meet you!")


number = 8 
if number % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")


numbers = {9, 7, 5, 4, 15}
max_value = max(numbers)
min_value = min(numbers)
print("maximum:", max_value)  # output: maximum: 15
print("minimum:", min_value)  # output: minimum: 4


def is_palindrome(s):
    return s == s[::-1]
string = "puppy"
print(is_palindrome(string))  # output: False


principal = 4000
rate = 5 / 100  # 5%
time = 3  # years
amount = principal * (1 + rate) ** time
compound_interest = amount - principal
print("compound interest:", compound_interest)  # output: compound interest: 630.9999999999991


total_days = 365
years = total_days // 365
weeks = (total_days % 365) // 7
days = (total_days % 365) % 7
print(f"{total_days} days is approximately {years} years, {weeks} weeks, and {days} days.")

numbers=[-8,6,-9,4,2,1,-3,5]
positive_numbers=sum(num for num in numbers if num>0)
print("sum of positive numbers:", positive_numbers) #output:sum of positive numbers:18

numbers = [-8, 6, -9, 4, 2, 1, -3, 5]
positive_numbers = sum(num for num in numbers if num > 0)
print("sum of positive numbers:", positive_numbers)  # output: sum of positive numbers: 18


sentence = "my name is kelsey and this is my favorite sentence lol idk what to put here"
words_count = len(sentence.split())
print("number of words:", words_count)  # output: number of words: 13


a = 56
b = 43
a, b = b, a
print("a:", a, "b:", b)  # output: a: 43 b: 56

