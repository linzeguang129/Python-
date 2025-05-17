magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title())

magicians = ['alice','david','carolina']
for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')
print('Thank, you, everyone. That was a great magic show!')

pizzas = ['1','2','3','4']
for pizza in pizzas:
    print(pizza)

for value in range(1,5):
    print(value)
print('that is all')

numbers = list(range(1,6))
print(numbers)

squares = []
for value in range(1,11):
    squares.append(value ** 2)
print(squares)

digits = list(range(0,10))
min(digits)
print(min(digits))
max(digits)
print(max(digits))
sum(digits)
print(sum(digits))

squares = [value**2 for value in range(1,11)]
print(squares)

numbers = list(range(1,21))
for number in numbers:
    print(number)

players = ['charles','martina','michael','florence','eli']
print('Here is the first three players on my team:')
for player in players[:3]:
    print(player.title())

my_food = ['pizza','falafel','carrot cake']
friend_food = my_food
my_food.append('cannoli')
friend_food.append('ice cream')
print('my favorite food are:', my_food)
print('my friend food are:', friend_food)

dimensions = (200,50)
print('Original dimensions:')
for dimension in dimensions:
    print(dimension)

dimensions = (400,10)
print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)

foods = (0,1,2,3,4)
foods = (0,4,2,3,6)
for food in foods:
    print(food)


