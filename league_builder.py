# League Builder
import csv
import random

Sharks = {'Team Name': 'Sharks'}
Raptors = {'Team Name': 'Raptors'}
Dragons = {'Team Name': 'Dragons'}

experienced = []
not_experienced = []

# Adds a row of data to the specified dictionary.
# In this program, add_dict is used to evenly divide players into three teams.
def add_dict(dict_name, row):
	name = row['Name']
	exp = row['Soccer Experience']
	guardian = row['Guardian Name(s)']
	dict_name[name] = {'Experience': exp, 'Guardian Name(s)': guardian}
	

# Writes a row of data to a txt file containing the
# player's name, whether they've played soccer before,
# and the name(s) of the player's legal guardians.
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

# Generates a file with text for a 'Welcome' letter for each player's guardian.
def generate_letter(name, parent_name, team_name):
	s = name.split(" ")
	text_name = s[0] + '_' + s[1] + '.txt'
	letter = open(text_name, "a")
	letter.write("Dear " + parent_name + ",\n\n" +
		     "Congratulations! " + s[0] + " has been placed onto the " + team_name +
		     " soccer team.\nWe look forward to " + s[0] + " playing in our junior " +
		     "soccer league. The first \npractice will be at 2:00 p.m. at the Marsbury " +
		     "Field at 219 West 29th \nStreet on Tuesday, May 26th.\n\nWe thank you again " +
		     "for your participation.\n\nSincerely,\n\nBuena Vista Soccer League")

def letters(team1, team2, team3):
        for key, value in team1.items():
                if key != 'Team Name':
                        generate_letter(key, value['Guardian Name(s)'], team1['Team Name'])
        for key, value in team2.items():
                if key != 'Team Name':
                        generate_letter(key, value['Guardian Name(s)'], team2['Team Name'])
        for key, value in team3.items():
                if key != 'Team Name':
                        generate_letter(key, value['Guardian Name(s)'], team3['Team Name'])


# Central sorting logic of the program. Places players into two different
# lists based on their experience level, and then distributes those players
# evenly into teams defined as dictionaries.
if __name__ == "__main__":
	with open('soccer_players.csv', newline='') as soccerfile:
		sccr_reader = csv.DictReader(soccerfile, delimiter = ',')
		rows = list(sccr_reader)
		
		#If player is experienced, add to experienced list. Else, add to not_experienced list.
		for row in rows:
			if row['Soccer Experience']=='YES':
				experienced.append(row)
			else:
				not_experienced.append(row)
				
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
				
		#Evenly divide up non-experienced players into teams as dictionaries.
		#Begins cycle on current 'team' integer, picking up where previous for-loop left off.
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
				

	# Writes each dictionary to the new .txt file.  
	write_to_file(Sharks)
	write_to_file(Raptors)
	write_to_file(Dragons)

	# Generate letter for all parents
	letters(Sharks, Raptors, Dragons)
	
				
