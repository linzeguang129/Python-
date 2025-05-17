from calendar import firstweekday

bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
print(len(bicycles))
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])

message = f"My first bicycle was a {bicycles[0].title()}"
print(message)

motorcycles = ['honda','yamada','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = ['honda','yamada','suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamada')
motorcycles.append('suzuki')
motorcycles.append('ducati')

motorcycles = ['honda','yamada','suzuki']
print(motorcycles)
motorcycles.insert(1,'ducati')
print(motorcycles)

motorcycles = ['honda','yamada','suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)

motorcycles = ['honda','yamada','suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()  #删除列表末尾元素并赋予到变量popped_motorcycles
print(motorcycles)
print(popped_motorcycles)

motorcycles = ['honda','yamada','suzuki']
last_owned = motorcycles.pop()
print(f'The last motorcycle I owned was a {last_owned.title()}')

motorcycles = ['honda','yamada','suzuki']
first_owned = motorcycles.pop(0)
print(f'The last motorcycle I owned was a {first_owned.title()}')

motorcycles = ['honda','yamada','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda','yamada','suzuki','ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f'\nA {too_expensive.title()} is too expensive for me.')

cars = ['bwm','audi','toyota','subaru']
print(cars)
cars.sort()
print(cars)

cars = ['bwm','audi','toyota','subaru']
print(cars)
print('Here is the original list:')
print(cars)
print('\nHere is the sorted list:')
print(sorted(cars))
print('\nHere is the original list again:')
print(cars)

cars = ['bwm','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)

cars = ['bwm','audi','toyota','subaru']
print(len(cars))