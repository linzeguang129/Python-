cars = ['audi','bwm','subaru','toyota']
for car in cars:
    if car == 'bwm':
        print(car.upper())
    else:
        print(car.title())

request_topping = 'mushrooms'
if request_topping != 'anchovies':
    print('hold the anchovies!')

request_toppings = ['mushrooms','onions','pineapples']
if 'mushrooms' in request_toppings:
    print('True')
else:
    print('False')

banned_users = ['andrew','carolina','david']
user = 'marise'
if user not in banned_users:
    print(f'{user.title()}, you can post a response if you want.')

game_active = True
can_edit = False

age = 17
if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')
else:
    print('Sorry, you are too young to vote!')
    print('Please register to vote as soon as you turn 18 !')

age = 12
if age < 4:
    print('you admission cost is 0 dollar')
elif age < 18:
    print('you admission cost is 25 dollars')
else:
    print('you admission cost is 40 dollars')

age = 65
if age < 4:
    print('you admission cost is 0 dollar')
elif age < 18:
    print('you admission cost is 25 dollars')
elif age < 65:
    print('you admission cost is 40 dollars')
else:
    print('you admission cost is 20 dollars')

age = 40
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print('your admission cost is', price,'dollars')

request_toppings = ['mushrooms','extra cheese']
if 'mushrooms' in request_toppings:
    print('Adding mushrooms')
if 'pepperoni' in request_toppings:
    print('Adding pepperoni')
if 'extra cheese' in request_toppings:
    print('Adding extra cheese')
print('\nFinished making your pizza!')

request_toppings = ['mushrooms','green peppers','extra cheese']
for request_topping in request_toppings:
    if request_topping == 'green peppers':
        print('Sorry, we are out of green peppers right now!')
    else:
        print('Adding',request_topping,'.')
print('\nFinished making your pizza!')

request_toppings = []
if request_toppings:
    for request_topping in request_toppings:
        print('Adding',request_topping,'.')
    print('\nFinished making your pizza!')
else:
    print('You are sure you want a plain pizza?')

available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
request_toppings = ['mushrooms','french fries','extra cheese']
for request_topping in request_toppings:
    if request_topping in available_toppings:
        print('Adding',request_topping,'.')
    else:
        print(f'Sorry, we are out of {request_topping}!')
print('\nFinished making your pizza!')

alien_colors = ['green','yellow','red']
for alien_color in alien_colors:
    if alien_color == 'green':
        print('You win 5 points!')
    if alien_color == 'yellow':
        print('You win 10 points!')
    if alien_color == 'red':
        print('You win 50 points!')
    else:
        print(' ')