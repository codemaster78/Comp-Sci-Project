import random
import time
import names

f = open("charecters.txt", "w")
count = int(input("Enter how many charecters you want: "))

for i in range(1, count + 1):
  print(f'Charecter #{i}\n')
  f.write(f'Charecter #{i}\n\n')
    
  #getting the ranges for all the charecteristics
  minage = int(input("Enter the minimum age of the charecter: "))
  maxage = int(input("Enter the maximum age of the charecter: "))
    
  #getting a random age from the ranges given
  age = random.randint(minage, maxage)
  print(f'age: {age}')
  f.write(f'age: {age}\n')
    
  #getting height of charecter
  feet = random.randint(4, 7)
  inch = random.randint(1, 11)
  time.sleep(0.75)
  print(f'height: {feet} feet and {inch} inches')
  f.write(f'height: {feet} feet and {inch} inches\n')
    
  #getting extra values
  health = round(random.randrange(1, 10), 2)
  time.sleep(0.75)
  print(f'health: {health}/10')
  f.write(f'health: {health}/10\n')
  speed = random.randint(1, 100)
  time.sleep(0.75)
  print(f'speed: {speed}')
  f.write(f'speed: {speed}\n')
    
  #getting gender
  gender = random.choice(["male", "female"])
  time.sleep(0.75)
  print(f'gender: {gender}\n')
  f.write(f'gender: {gender}\n')

  #getting the Name
  name = names.get_full_name(gender = gender)
  print(f'Name: {name}')
  f.write("Name: " + name + "\n")

  #Language
  lang = random.choice([True, False])
  time.sleep(0.75)
  print(f'English speaker: {lang}\n\n\n')
  f.write(f'English speaker: {lang}\n\n\n')

print("Charecters have been created")
f.close()
