# League Builder
import csv

Sharks = {}
Raptors = {}
Dragons = {}

experienced = []
not_experienced = []

if __name__ == "__main__":
	with open('soccer_players.csv', newline='') as soccerfile:
		sccr_reader = csv.reader(soccerfile, delimiter = ',')
		rows = list(sccr_reader)
		for row in rows[1:-1]:
			if row[2]=='YES':
				experienced.append(row)
			else:
				not_experienced.append(row)
		print("experienced: ")
		for name in experienced:
			print(name)
		print("not experienced: ")
		for name in not_experienced:
			print(name)
