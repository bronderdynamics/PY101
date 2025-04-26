#Exercise 1
#False or (True and False) = 0
#True or (1 + 2) = 1
#(1 + 2) or True = 3
#True and (1 + 2) = 3
#False and (1 + 2) = 0
#(1 + 2) and True = 1
#(32 * 4) >= 129 = 0
#False != (not True) = 0
#True == 4 = 0
#False == (847 == '847') = 1

#Exercise 2
def even_or_odd(number):
    if number % 2 == 0:
        print('even')
    else:
        print('odd')

#Exercise 3
#Product 2
#Product not found! - the function looks for a string and an integer was passed

#Exercise 4
#if foo():
#    return 'bar'
#else:
#    return qux()

#Exercise 5
#It would print empty since there's nothing in the list

#Exercise 6
def upper_if_ten_or_more(string):
    if len(string) > 10:
        return string.upper()
    else:
        return string
print(upper_if_ten_or_more("hello"))

def number_range(number):
    if (number >= 0) and (number <= 50):
        return f"{number} is between 0 and 50"
    elif (number >= 51) and (number <= 100):
        return f"{number} is between 51 and 100"
    elif (number > 100):
        return f"{number} is greater than 100"
    else:
        return f"{number} if less than 0"
print(number_range(0))
print(number_range(25))
print(number_range(50))
print(number_range(75))
print(number_range(100))
print(number_range(101))
print(number_range(-1))