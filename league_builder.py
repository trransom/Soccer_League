# League Builder
import csv
import random

Sharks = {}
Raptors = {}
Dragons = {}

experienced = []
not_experienced = []

if __name__ == "__main__":
	with open('soccer_players.csv', newline='') as soccerfile:
		sccr_reader = csv.reader(soccerfile, delimiter = ',')
		rows = list(sccr_reader)
		
		#If player is experienced, add to experienced list. Else, add to not_experienced list.
		for row in rows[1:-1]:
			if row[2]=='YES':
				experienced.append(row)
			else:
				not_experienced.append(row)
		#Evenly divide up experienced players into teams as dictionaries.
		team = 1
		for row in experienced:
			#Add to sharks
			if team==1:
				name = row[0]
				exp = row[2]
				guardian = row[3]
				Sharks[name] = {'Experience': exp, 'Guardian(s)': guardian}
				team += 1
			#Add to raptors
			elif team==2:
				name = row[0]
				exp = row[2]
				guardian = row[3]
				Raptors[name] = {'Experience': exp, 'Guardian(s)': guardian}
				team += 1
			#Add to dragons
			elif team==3:
				name = row[0]
				exp = row[2]
				guardian = row[3]
				Dragons[name] = {'Experience': exp, 'Guardian(s)': guardian}
				team -= 2
		#Evenly divide up experienced players into teams as dictionaries.
		#Begin cycle on current team member, picking up where previous for loop left off.
		for row in not_experienced:
			#Add to sharks
			if team==1:
				name = row[0]
				exp = row[2]
				guardian = row[3]
				Sharks[name] = {'Experience': exp, 'Guardian(s)': guardian}
				team += 1
			#Add to raptors
			elif team==2:
				name = row[0]
				exp = row[2]
				guardian = row[3]
				Raptors[name] = {'Experience': exp, 'Guardian(s)': guardian}
				team += 1
			#Add to dragons
			elif team==3:
				name = row[0]
				exp = row[2]
				guardian = row[3]
				Dragons[name] = {'Experience': exp, 'Guardian(s)': guardian}
				team -= 2
				
				
