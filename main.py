import random

print("Hello it is very nice to meet you! My name is Vedant and I'm very excited to get to know you. ")
name = input("What is your name: ")

print(f"It is very nice to meet you {name}!")
print("\n")

age = int(input("How old are you? "))

if age <= 13:
  print("Enjoy the rest of your childhood and make a lot of fun memories!")
elif age <= 18:
  print("Make lots of friends in your teenage years!")
else:
  print("Don't forget to have fun during your life!")

print("\n")

sports = input("Do you play any sports? If you play more than one, please put a space between them: ")

pointer = 0
sportsNumber = sports.count(" ") + 1
sportsArr = []
for i in range(sportsNumber):
  index = sports.find(" ", pointer)
  sportsArr.append(sports[pointer:index])
  pointer = index + 1
  
sportsArr[sportsNumber - 1] += sports[len(sports)-1:len(sports)]
#print(sportsArr)
print("\n")

print("I am now going to ask you questions based on a random sport that you play just to get a feel of your relationship with that sport!")
pickedSport = random.choice(sportsArr)
#print(pickedSport)

like = input(f"Do you enjoy {pickedSport}? ")
print("Interesting")
print("\n")

long = int(input(f"How many years have you been playing {pickedSport}? "))
if long <= 1:
  print("Looks like you haven't been playing the sport for a while!")
elif long <= 4:
  print("Wow thats a pretty long time!")
else:
  print("You have been playing this sport for such a long time you must really like it!")

print("\n")
print("Well it was very fun to talk with you, I hope you enjoy your day! See you later!")