# madlib using input function

name = ''
color = ''
result = ''

start_lib = ('Please fill in the blanks below: ')
my_lib = "___(name)___'s favorite color is  ___(color)___"

print(start_lib)
print(my_lib)

name = input('What is your name? ')
color = input('What is your favorite color? ')

result = f"{name}'s favorite color is {color}."

print(result)