# League Builder
import csv
import random

Sharks = {}
Raptors = {}
Dragons = {}

experienced = []
not_experienced = []

def add_dict(dict_name, row):
	name = row['Name']
	exp = row['Soccer Experience']
	guardian = row['Guardian Name(s)']
	dict_name[name] = {'Experience': exp, 'Guardian Name(s)': guardian}

if __name__ == "__main__":
	with open('soccer_players.csv', newline='') as soccerfile:
		sccr_reader = csv.DictReader(soccerfile, delimiter = ',')
		rows = list(sccr_reader)
		#for row in rows:
		#	print(row['Name'])
		

		
		#If player is experienced, add to experienced list. Else, add to not_experienced list.
		for row in rows:
			if row['Soccer Experience']=='YES':
				experienced.append(row)
			else:
				not_experienced.append(row)
		print("Experienced: \n")
		print(experienced)
		print("\nNot experienced: \n")
		print(not_experienced)
		print()
		#Evenly divide up experienced players into teams as dictionaries.
		team = 1
		for row in experienced:
			#Add to sharks
			if team==1:
				add_dict(Sharks, row)
				team += 1
			#Add to raptors
			elif team==2:
				add_dict(Raptors, row)
				team += 1
			#Add to dragons
			elif team==3:
				add_dict(Dragons, row)
				team -= 2
		print(team)
		#Evenly divide up experienced players into teams as dictionaries.
		#Begin cycle on current team number, picking up where previous for loop left off.
		for row in not_experienced:
			#Add to sharks
			if team==1:
				add_dict(Sharks, row)
				team += 1
				print("Team is now " + str(team))
			#Add to raptors
			elif team==2:
				add_dict(Raptors, row)
				team += 1
				print("Team is now " + str(team))
			#Add to dragons
			elif team==3:
				add_dict(Dragons, row)
				team -= 2
				print("Team is now " + str(team))



print(len(Sharks.keys()))
for key in list(Sharks.keys()):
        print(key)
print(len(Raptors.keys()))
for key in list(Raptors.keys()):
        print(key)
print(len(Dragons.keys()))
for key in list(Dragons.keys()):
        print(key)
				
