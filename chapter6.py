alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])

alien_0 = {'color':'green','points':5}
new_points = alien_0['points']
print(f'You just earned {new_points} points.')

alien_0 = {'color':'green','points':5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

alien_0 = {'color':'green','points':5}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print(f"Original x_position: {alien_0['x_position']}")
alien_0['speed'] = 'fast'
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New x_position: {alien_0['x_position']}")

alien_0 = {'color':'green','points':5}
print(alien_0)
del alien_0['points']
print(alien_0)

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python'
}
language = favorite_languages['sarah'].title()
print(f"Sarah 's favorite language is {language}.")


alien_0 = {'color':'green','speed':'slow'}
print_value = alien_0.get('points','No point value assigned.')
print(print_value)

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for (key, value) in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python'
}
for (name, language) in favorite_languages.items():
    print(f"{name.title()} favorite language is {language.title()}")

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}
for (key,value) in favorite_languages.items():
    print(f"{key.title()} ")
    print(f"{value.title()} ")


favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}
friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(f"Hi,{name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()},I see you love {language}.")

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}
print('The following languages have been mentioned:')
for language in favorite_languages.values():
    print(f"{language.title()}.")

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}
print('The following languages have been mentioned:')
for language in set(favorite_languages.values()):
    print(language.title())

languages = {'python','c','ruby','python'}
print(languages)

alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)



aliens = []
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
for alien in aliens[:30]:
    print(alien)
print('...')
print('Total number of aliens:', len(aliens))


aliens = []
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color'] == 'green':
         alien['color'] = 'yellow'
         alien['speed'] = 'medium'
         alien['points'] = 10
for alien in aliens[:5]:
    print(alien)
print('...')
print('Total number of aliens:', len(aliens))


pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese']
}
print(f"You ordered a {pizza['crust']} crust pizza.\n"
      "with the following toppings:")
for topping in pizza['toppings']:
    print('\t'+topping)

favorite_languages = {
    'jen' : ['python','ruby'],
    'sarah' : ['c'],
    'edward' : ['ruby','go'],
    'phil' : ['python','haskell'],
}
for (name,languages) in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    }
}
for username,user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")