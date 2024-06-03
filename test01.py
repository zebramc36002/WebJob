# create a function output the square of input number
def square_number(num):
  return num ** 2

print(square_number(5))

# create a function output the triple of input number 

def double_even_numbers(lst):
  return [num * 2 for num in lst if num % 2 == 0]
