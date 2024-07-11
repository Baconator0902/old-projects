import requests
import json

def jprint(obj):

	pokimoninfo = json.dumps(obj, sort_keys=True, indent=4)
	message = []

	#stats
	name = obj["forms"][0]["name"]
	health = obj["stats"][0]['base_stat']
	attack = obj["stats"][1]['base_stat']
	special_attack = obj["stats"][3]['base_stat']
	special_defense = obj["stats"][4]['base_stat']
	speed = obj["stats"][5]['base_stat']

	message.append('\n Your pokimon - ' + str(name) + "\n")
	message.append('STATS \n ----- \n health: ' + str(health))
	message.append('attack: ' + str(attack))
	message.append('special attack: ' + str(special_attack))
	message.append('special defense: ' + str(special_defense))
	message.append('speed: ' + str(speed))

	#list of moves
	x = 0
	message.append('\n MOVES \n -----')
	for move in obj['moves']:
		move1 = str(obj['moves'][x]['move']['name'])
		x = x + 1
		message.append(move1)


	#list of abilities
	x = -1
	message.append('\n ABILITIES \n ---------')
	for thing in obj["abilities"]:
		x = x + 1
		abilname = obj["abilities"][x]["ability"]["name"]
		message.append(str(abilname))


		response2 = requests.get(obj["abilities"][x]["ability"]["url"])
		abilinfo = json.dumps(response2.json(), sort_keys=True, indent=4)
		return message
