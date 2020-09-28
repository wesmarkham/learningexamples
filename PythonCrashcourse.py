#Start Chapter 1
print("Hello World")
examplevariable = "Hello, User, would you like to learn some python today?"
print(examplevariable)
#End Chapter 1
#Start Chapter 2
age = 23
happymessage = 'Happy ' + str(age) + 'rd Birthday'
print(happymessage)
#Say Hello to everyone.
print("Hello Python People")
import this
#End Chaper 2
#Start Chapter 3
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[2])
print(bicycles[-1])

bikemessage = "My first bicycle was a " + bicycles[0].title() +'.'
print(bikemessage)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#motorcycles[0] = 'ducati' former code, appending ducati instead of replacing it

motorcycles.append('ducati')
print(motorcycles)
#motorcycles.insert(0, 'ducati'), had a typo error needed to copy code, GRAMMAR matters *face palm*
motorcycles.insert(0, 'harley')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

second_owned = motorcycles.pop(0)
print("The second motorcycle I owned was a "  + second_owned.title() + ".")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

cars.reverse()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)

#End Chapter 3
