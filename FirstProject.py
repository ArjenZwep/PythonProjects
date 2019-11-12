#introduction statement and welcome message
print("Welcome to my new social network, some people like to call it facebook 2.0, i like to call arjenbook ")
firstname = input("What is your first name? ")
print(f"welcome {firstname} to arjenbook")

#checking the last name and comparing it to my name
ownlast = "zwep"
lastname = input("What is your last name? ").strip().lower()
if lastname == ownlast:
	print("wow your part of my awesome family, very nice indeed! ")

#checking birthday and if the age is old enough
birthday = input("What is your year of birth? ")
birthday_cac = 2018 - int(birthday)
if birthday_cac <= 18:
	exit = input("warning you are not old enough to enter this social network, would you like to quit?yes/no ")
	exit = exit.strip()
	if exit == "yes":
		import sys
		sys.exit()
	else:
		print("alright badass continue then")

#some more questions for getting value data
gender = input("What is your gender male/female ").strip().lower()
openday = input("Estimated, how many times do you open facebook on a daily basis? ")
openday = int(openday)

#estimate a value with age
if 0 <= birthday_cac <= 18:
	value1 = 1
elif 19 <= birthday_cac <= 36:
	value1 = 3
elif birthday_cac > 36:
	value1 = 2

#estimate a value with gender
if gender == "female":
	value2 = 4
else:
	value2 = 2

#estimate a value with how many times he opens facebook
if 0 <= int(openday) <= 4:
	value3 = 0
elif 5 <= int(openday) <= 9:
	value3 = 2
else:
	value3 = 3
valuetotal = value1 + value2 + value3
print(F"on a scale from 1-10 the potential value of this user {valuetotal}")

#last questions for some extra data
askvalue = input("what do you think about your value? ")
print("interesting reply")
betterask = input("do you think arjenbook will be better then facebook?yes/no ").strip().lower()
if betterask == "yes":
	print("nice, you are part of the new generation, welcome to the future")
else:
	print("keep living in the past scrub")
print("Thanks, the registration is now complete")