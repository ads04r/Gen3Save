import json, struct, sys, os
from operator import xor

class Gen3Save:

	def speciesname(self, id):

		names = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot", "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran (F)", "Nidorina", "Nidoqueen", "Nidoran (M)", "Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat", "Venomoth", "Diglett", "Dugtrio", "Meowth", "Persian", "Psyduck", "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag", "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop", "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool", "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash", "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetch'd", "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer", "Muk", "Shellder", "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute", "Exeggutor", "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung", "Koffing", "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela", "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie", "Mr. Mime", "Scyther", "Jynx", "Electabuzz", "Magmar", "Pinsir", "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto", "Eevee", "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte", "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew", "Chikorita", "Bayleef", "Meganium", "Cyndaquil", "Quilava", "Typhlosion", "Totodile", "Croconaw", "Feraligatr", "Sentret", "Furret", "Hoothoot", "Noctowl", "Ledyba", "Ledian", "Spinarak", "Ariados", "Crobat", "Chinchou", "Lanturn", "Pichu", "Cleffa", "Igglybuff", "Togepi", "Togetic", "Natu", "Xatu", "Mareep", "Flaaffy", "Ampharos", "Bellossom", "Marill", "Azumarill", "Sudowoodo", "Politoed", "Hoppip", "Skiploom", "Jumpluff", "Aipom", "Sunkern", "Sunflora", "Yanma", "Wooper", "Quagsire", "Espeon", "Umbreon", "Murkrow", "Slowking", "Misdreavus", "Unown", "Wobbuffet", "Girafarig", "Pineco", "Forretress", "Dunsparce", "Gligar", "Steelix", "Snubbull", "Granbull", "Qwilfish", "Scizor", "Shuckle", "Heracross", "Sneasel", "Teddiursa", "Ursaring", "Slugma", "Magcargo", "Swinub", "Piloswine", "Corsola", "Remoraid", "Octillery", "Delibird", "Mantine", "Skarmory", "Houndour", "Houndoom", "Kingdra", "Phanpy", "Donphan", "Porygon2", "Stantler", "Smeargle", "Tyrogue", "Hitmontop", "Smoochum", "Elekid", "Magby", "Miltank", "Blissey", "Raikou", "Entei", "Suicune", "Larvitar", "Pupitar", "Tyranitar", "Lugia", "Ho-Oh", "Celebi", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Treecko", "Grovyle", "Sceptile", "Torchic", "Combusken", "Blaziken", "Mudkip", "Marshtomp", "Swampert", "Poochyena", "Mightyena", "Zigzagoon", "Linoone", "Wurmple", "Silcoon", "Beautifly", "Cascoon", "Dustox", "Lotad", "Lombre", "Ludicolo", "Seedot", "Nuzleaf", "Shiftry", "Nincada", "Ninjask", "Shedinja", "Taillow", "Swellow", "Shroomish", "Breloom", "Spinda", "Wingull", "Pelipper", "Surskit", "Masquerain", "Wailmer", "Wailord", "Skitty", "Delcatty", "Kecleon", "Baltoy", "Claydol", "Nosepass", "Torkoal", "Sableye", "Barboach", "Whiscash", "Luvdisc", "Corphish", "Crawdaunt", "Feebas", "Milotic", "Carvanha", "Sharpedo", "Trapinch", "Vibrava", "Flygon", "Makuhita", "Hariyama", "Electrike", "Manectric", "Numel", "Camerupt", "Spheal", "Sealeo", "Walrein", "Cacnea", "Cacturne", "Snorunt", "Glalie", "Lunatone", "Solrock", "Azurill", "Spoink", "Grumpig", "Plusle", "Minun", "Mawile", "Meditite", "Medicham", "Swablu", "Altaria", "Wynaut", "Duskull", "Dusclops", "Roselia", "Slakoth", "Vigoroth", "Slaking", "Gulpin", "Swalot", "Tropius", "Whismur", "Loudred", "Exploud", "Clamperl", "Huntail", "Gorebyss", "Absol", "Shuppet", "Banette", "Seviper", "Zangoose", "Relicanth", "Aron", "Lairon", "Aggron", "Castform", "Volbeat", "Illumise", "Lileep", "Cradily", "Anorith", "Armaldo", "Ralts", "Kirlia", "Gardevoir", "Bagon", "Shelgon", "Salamence", "Beldum", "Metang", "Metagross", "Regirock", "Regice", "Registeel", "Kyogre", "Groudon", "Rayquaza", "Latias", "Latios", "Jirachi", "Deoxys", "Chimecho", "Pok\u00e9mon Egg", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown"]
		if id>len(names):
			return ""
		return names[id - 1]

	def movename(self, id):

		moves = ["Pound", "Karate Chop", "Double Slap", "Comet Punch", "Mega Punch", "Pay Day", "Fire Punch", "Ice Punch", "Thunder Punch", "Scratch", "Vice Grip", "Guillotine", "Razor Wind", "Swords Dance", "Cut", "Gust", "Wing Attack", "Whirlwind", "Fly", "Bind", "Slam", "Vine Whip", "Stomp", "Double Kick", "Mega Kick", "Jump Kick", "Rolling Kick", "Sand Attack", "Headbutt", "Horn Attack", "Fury Attack", "Horn Drill", "Tackle", "Body Slam", "Wrap", "Take Down", "Thrash", "Double-Edge", "Tail Whip", "Poison Sting", "Twineedle", "Pin Missile", "Leer", "Bite", "Growl", "Roar", "Sing", "Supersonic", "Sonic Boom", "Disable", "Acid", "Ember", "Flamethrower", "Mist", "Water Gun", "Hydro Pump", "Surf", "Ice Beam", "Blizzard", "Psybeam", "Bubble Beam", "Aurora Beam", "Hyper Beam", "Peck", "Drill Peck", "Submission", "Low Kick", "Counter", "Seismic Toss", "Strength", "Absorb", "Mega Drain", "Leech Seed", "Growth", "Razor Leaf", "Solar Beam", "Poison Powder", "Stun Spore", "Sleep Powder", "Petal Dance", "String Shot", "Dragon Rage", "Fire Spin", "Thunder Shock", "Thunderbolt", "Thunder Wave", "Thunder", "Rock Throw", "Earthquake", "Fissure", "Dig", "Toxic", "Confusion", "Psychic", "Hypnosis", "Meditate", "Agility", "Quick Attack", "Rage", "Teleport", "Night Shade", "Mimic", "Screech", "Double Team", "Recover", "Harden", "Minimize", "Smokescreen", "Confuse Ray", "Withdraw", "Defense Curl", "Barrier", "Light Screen", "Haze", "Reflect", "Focus Energy", "Bide", "Metronome", "Mirror Move", "Self-Destruct", "Egg Bomb", "Lick", "Smog", "Sludge", "Bone Club", "Fire Blast", "Waterfall", "Clamp", "Swift", "Skull Bash", "Spike Cannon", "Constrict", "Amnesia", "Kinesis", "Soft-Boiled", "High Jump Kick", "Glare", "Dream Eater", "Poison Gas", "Barrage", "Leech Life", "Lovely Kiss", "Sky Attack", "Transform", "Bubble", "Dizzy Punch", "Spore", "Flash", "Psywave", "Splash", "Acid Armor", "Crabhammer", "Explosion", "Fury Swipes", "Bonemerang", "Rest", "Rock Slide", "Hyper Fang", "Sharpen", "Conversion", "Tri Attack", "Super Fang", "Slash", "Substitute", "Struggle", "Sketch", "Triple Kick", "Thief", "Spider Web", "Mind Reader", "Nightmare", "Flame Wheel", "Snore", "Curse", "Flail", "Conversion 2", "Aeroblast", "Cotton Spore", "Reversal", "Spite", "Powder Snow", "Protect", "Mach Punch", "Scary Face", "Feint Attack", "Sweet Kiss", "Belly Drum", "Sludge Bomb", "Mud-Slap", "Octazooka", "Spikes", "Zap Cannon", "Foresight", "Destiny Bond", "Perish Song", "Icy Wind", "Detect", "Bone Rush", "Lock-On", "Outrage", "Sandstorm", "Giga Drain", "Endure", "Charm", "Rollout", "False Swipe", "Swagger", "Milk Drink", "Spark", "Fury Cutter", "Steel Wing", "Mean Look", "Attract", "Sleep Talk", "Heal Bell", "Return", "Present", "Frustration", "Safeguard", "Pain Split", "Sacred Fire", "Magnitude", "Dynamic Punch", "Megahorn", "Dragon Breath", "Baton Pass", "Encore", "Pursuit", "Rapid Spin", "Sweet Scent", "Iron Tail", "Metal Claw", "Vital Throw", "Morning Sun", "Synthesis", "Moonlight", "Hidden Power", "Cross Chop", "Twister", "Rain Dance", "Sunny Day", "Crunch", "Mirror Coat", "Psych Up", "Extreme Speed", "Ancient Power", "Shadow Ball", "Future Sight", "Rock Smash", "Whirlpool", "Beat Up", "Fake Out", "Uproar", "Stockpile", "Spit Up", "Swallow", "Heat Wave", "Hail", "Torment", "Flatter", "Will-O-Wisp", "Memento", "Facade", "Focus Punch", "Smelling Salts", "Follow Me", "Nature Power", "Charge", "Taunt", "Helping Hand", "Trick", "Role Play", "Wish", "Assist", "Ingrain", "Superpower", "Magic Coat", "Recycle", "Revenge", "Brick Break", "Yawn", "Knock Off", "Endeavor", "Eruption", "Skill Swap", "Imprison", "Refresh", "Grudge", "Snatch", "Secret Power", "Dive", "Arm Thrust", "Camouflage", "Tail Glow", "Luster Purge", "Mist Ball", "Feather Dance", "Teeter Dance", "Blaze Kick", "Mud Sport", "Ice Ball", "Needle Arm", "Slack Off", "Hyper Voice", "Poison Fang", "Crush Claw", "Blast Burn", "Hydro Cannon", "Meteor Mash", "Astonish", "Weather Ball", "Aromatherapy", "Fake Tears", "Air Cutter", "Overheat", "Odor Sleuth", "Rock Tomb", "Silver Wind", "Metal Sound", "Grass Whistle", "Tickle", "Cosmic Power", "Water Spout", "Signal Beam", "Shadow Punch", "Extrasensory", "Sky Uppercut", "Sand Tomb", "Sheer Cold", "Muddy Water", "Bullet Seed", "Aerial Ace", "Icicle Spear", "Iron Defense", "Block", "Howl", "Dragon Claw", "Frenzy Plant", "Bulk Up", "Bounce", "Mud Shot", "Poison Tail", "Covet", "Volt Tackle", "Magical Leaf", "Water Sport", "Calm Mind", "Leaf Blade", "Dragon Dance", "Rock Blast", "Shock Wave", "Water Pulse", "Doom Desire", "Psycho Boost"]
		return moves[id - 1]

	def naturename(self, id):

		natures = ["Hardy", "Lonely", "Brave", "Adamant", "Naughty", "Bold", "Docile", "Relaxed", "Impish", "Lax", "Timid", "Hasty", "Serious", "Jolly", "Naive", "Modest", "Mild", "Quiet", "Bashful", "Rash", "Calm", "Gentle", "Sassy", "Careful", "Quirky"]
		return natures[id]

	def movetype(self, id):

		return ""

	def readstring(self, text):

		chars = "0123456789!?.-         ,  ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
		ret = ""
		for i in text:
			c = int(i) - 161
			if c<0 or c>len(chars):
				ret = ret + " "
			else:
				ret = ret + chars[c]
		return ret.strip()

	def getindex(self, data):

		ret = []

		for i in range(0, 14):
			ix = i * 4096
			section = data[ix:(ix+4096)]
			footer = section[4084:]
			id = struct.unpack('<H', footer[0:2])[0]
			index = struct.unpack('<I', footer[4:8])[0]
			ds = 0

			if id == 0:
				ds = struct.unpack('<HBBB', section[14:19])
				dt = (ds[0] * 3600) + (ds[1] * 60) + ds[2]
				ret = [index, dt]

		return ret

	def load(self, filename):

		f = open(filename, "rb")
		data = bytearray(f.read())

		filea = data[0:57344]
		fileb = data[57344:114688]

		a = self.getindex(filea)
		b = self.getindex(fileb)

		if a[0] < b[0]:
			savedata = fileb
			self.time = b[1]
		elif a[0] > b[0]:
			savedata = filea
			self.time = a[1]
		else:
			if a[1] < b[1]:
				savedata = fileb
				self.time = b[1]
			else:
				savedata = filea
				self.time = a[1]

		self.process(savedata)

	def processpkm(self, pkm):

		ret = {}
		orders = ['GAEM', 'GAME', 'GEAM', 'GEMA', 'GMAE', 'GMEA', 'AGEM', 'AGME', 'AEGM', 'AEMG', 'AMGE', 'AMEG', 'EGAM', 'EGMA', 'EAGM', 'EAMG', 'EMGA', 'EMAG', 'MGAE', 'MGEA', 'MAGE', 'MAEG', 'MEGA', 'MEAG']
		ret['name'] = self.readstring(pkm[8:18])
		trainer = self.readstring(pkm[20:27])
		if trainer == '' and ret['name'] == '':
			return {}
		ret['personality'] = struct.unpack('<I', pkm[0:4])[0]
		ret['trainer'] = {'id': struct.unpack('<I', pkm[4:8])[0],'name': trainer}
		key = xor(ret['trainer']['id'], ret['personality'])

		data = pkm[32:]
		order = ret['personality'] % 24
		orderstring = orders[order]
		sections = {}
		for i in range(0, 4):
			section = orderstring[i]
			sectiondata = data[(i * 12):((i + 1) * 12)]
			sections[section] = self.decryptsubsection(sectiondata, key)
		ret['species'] = {'id': int(struct.unpack('<H', sections['G'][0:2])[0])}
		ret['species']['name'] = self.speciesname(ret['species']['id'])
		ret['exp'] = int(struct.unpack('<I', sections['G'][4:8])[0])

		moves = []
		for i in range(0, 4):
			item = {}
			item['id'] = int(struct.unpack('<H', sections['A'][(i * 2):((i + 1) * 2)])[0])
			if item['id'] == 0:
				continue
			item['name'] = self.movename(item['id'])
			item['type'] = self.movetype(item['id'])
			item['pp'] = int(struct.unpack('B', sections['A'][(i + 8)])[0])
			moves.append(item)
		ret['moves'] = moves
		ret['nature'] = self.naturename(ret['personality'] % 25)

		ev = {}
		ev['hp'] = int(struct.unpack('B', sections['E'][0])[0])
		ev['attack'] = int(struct.unpack('B', sections['E'][1])[0])
		ev['defence'] = int(struct.unpack('B', sections['E'][2])[0])
		ev['speed'] = int(struct.unpack('B', sections['E'][3])[0])
		ev['spatk'] = int(struct.unpack('B', sections['E'][4])[0])
		ev['spdef'] = int(struct.unpack('B', sections['E'][5])[0])
		ev['cool'] = int(struct.unpack('B', sections['E'][6])[0])
		ev['beauty'] = int(struct.unpack('B', sections['E'][7])[0])
		ev['cute'] = int(struct.unpack('B', sections['E'][8])[0])
		ev['smart'] = int(struct.unpack('B', sections['E'][9])[0])
		ev['tough'] = int(struct.unpack('B', sections['E'][10])[0])
		ev['feel'] = int(struct.unpack('B', sections['E'][11])[0])
		ret['ev'] = ev

		if ret['species']['id'] > 386:
			return {}

		return ret

	def decryptsubsection(self, data, key):

		if len(data) != 12:
			return []
		a = xor(struct.unpack('<I', data[0:4])[0], key)
		b = xor(struct.unpack('<I', data[4:8])[0], key)
		c = xor(struct.unpack('<I', data[8:12])[0], key)
		return struct.pack('<III', a, b, c)

	def process(self, savedata):

		sections = []
		for i in range(0, 14):
			sections.append([])
		for i in range(0, 14):
			ix = i * 4096
			section = savedata[ix:(ix+4096)]
			footer = section[4084:]
			id = struct.unpack('<H', footer[0:2])[0]
			index = struct.unpack('<I', footer[4:8])[0]
			sections[id] = section[0:3968]

		self.name = self.readstring(sections[0][0:7]).strip()
		self.boxes = []

		dex = bytearray()
		for i in range(5, 14):
			dex = dex + sections[i]
		dex = dex[4:33604]
		for i in range(0, 420):
			pkm = self.processpkm(dex[(i * 80):((i + 1) * 80)])
			if len(pkm) == 0:
				continue
			self.boxes.append(pkm)

if __name__ == "__main__":

	if len(sys.argv) < 2:
		sys.exit('Usage: %s [save_file]' % sys.argv[0])

	if not os.path.exists(sys.argv[1]):
		sys.exit('ERROR: File %s not found' % sys.argv[1])

	sf = SaveFile()
	sf.load(sys.argv[1])

	print json.dumps(sf.boxes)

