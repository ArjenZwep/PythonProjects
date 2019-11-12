#refer to the file and set lists
file = open("politicians.csv")
row = []
index = 0

#divide the file into lists and displaying the list
for line in file:
	row_var = line.strip().split(",")
	row.append(row_var)
	first_name = row_var[0]
	last_name = row_var[1]
	birthyear = row_var[2]
	party = row_var[3]
	print(f"{index} : {first_name} {last_name} was born in {birthyear} and is part of {party}")
	index = index + 1
#close the file
file.close()


#giving all the options for modifying the list and making a loop
while True:
	options = input("A: add a person R: remove a person S: save the database Q: quit program").strip().upper()

#adding a person
	if options == "A":
			new_first_name = input("What is the first name?")
			new_last_name = input("What is the last name?")
			new_birthyear = input("What is the birthyear?")
			new_party = input("What is his/her political party?")
			newpoliticanrow = [new_first_name, new_last_name, new_birthyear, new_party]
			row.append(newpoliticanrow)

#removing a person
	elif options == "R":
		remove_number = input("Choose wich person you want to remove based on index number")
		row.pop(int(remove_number))

#saving the database
	elif options == "S":
		file_edit = open("politicians.csv", "w")
		for line in row:
			row_var2 = ",".join(line)
			file_edit.write(row_var2 + "\n")
		file_edit.close()
		print("saved the file to politcians")

#exit the option
	elif options == "Q":
		print("alright bye")
		exit()