# League Builder
import csv
import random

Sharks = {'Team Name': 'Sharks'}
Raptors = {'Team Name': '\n\nRaptors'}
Dragons = {'Team Name': '\n\nDragons'}

experienced = []
not_experienced = []

def add_dict(dict_name, row):
	name = row['Name']
	exp = row['Soccer Experience']
	guardian = row['Guardian Name(s)']
	dict_name[name] = {'Experience': exp, 'Guardian Name(s)': guardian}
	

def write_to_file(team1):
        text_file = open("teams.txt", "a")
        text_file.write(team1['Team Name']+"\n")
        text_file.close()
        with open('teams.txt', 'a') as txtfile:
                fieldnames = ['Name', 'Experience', 'Guardians']
                teamwriter = csv.DictWriter(txtfile, fieldnames=fieldnames)
                for key, value in team1.items():
                        if key != 'Team Name':
                                teamwriter.writerow({
                                        'Name': key,
                                        'Experience': value['Experience'],
                                        'Guardians': value['Guardian Name(s)']
                                        })
           


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
			#Add to raptors
			elif team==2:
				add_dict(Raptors, row)
				team += 1
			#Add to dragons
			elif team==3:
				add_dict(Dragons, row)
				team -= 2



##print(len(Sharks.keys()))
##for key in list(Sharks.keys()):
##	print(key)
##print(len(Raptors.keys()))
##for key in list(Raptors.keys()):
##	print(key)
##print(len(Dragons.keys()))
##for key in list(Dragons.keys()):
##	print(key)

##for keys,values in Sharks.items():
##    print(keys)
##    print(values)

	
write_to_file(Sharks)
write_to_file(Raptors)
write_to_file(Dragons)


	
				
