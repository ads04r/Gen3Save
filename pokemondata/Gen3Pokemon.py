import json, struct, sys, os
from operator import xor

class Gen3Pokemon:

	def __speciesname(self, id):

		names = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot", "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran (F)", "Nidorina", "Nidoqueen", "Nidoran (M)", "Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat", "Venomoth", "Diglett", "Dugtrio", "Meowth", "Persian", "Psyduck", "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag", "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop", "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool", "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash", "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetch'd", "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer", "Muk", "Shellder", "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute", "Exeggutor", "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung", "Koffing", "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela", "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie", "Mr. Mime", "Scyther", "Jynx", "Electabuzz", "Magmar", "Pinsir", "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto", "Eevee", "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte", "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew", "Chikorita", "Bayleef", "Meganium", "Cyndaquil", "Quilava", "Typhlosion", "Totodile", "Croconaw", "Feraligatr", "Sentret", "Furret", "Hoothoot", "Noctowl", "Ledyba", "Ledian", "Spinarak", "Ariados", "Crobat", "Chinchou", "Lanturn", "Pichu", "Cleffa", "Igglybuff", "Togepi", "Togetic", "Natu", "Xatu", "Mareep", "Flaaffy", "Ampharos", "Bellossom", "Marill", "Azumarill", "Sudowoodo", "Politoed", "Hoppip", "Skiploom", "Jumpluff", "Aipom", "Sunkern", "Sunflora", "Yanma", "Wooper", "Quagsire", "Espeon", "Umbreon", "Murkrow", "Slowking", "Misdreavus", "Unown", "Wobbuffet", "Girafarig", "Pineco", "Forretress", "Dunsparce", "Gligar", "Steelix", "Snubbull", "Granbull", "Qwilfish", "Scizor", "Shuckle", "Heracross", "Sneasel", "Teddiursa", "Ursaring", "Slugma", "Magcargo", "Swinub", "Piloswine", "Corsola", "Remoraid", "Octillery", "Delibird", "Mantine", "Skarmory", "Houndour", "Houndoom", "Kingdra", "Phanpy", "Donphan", "Porygon2", "Stantler", "Smeargle", "Tyrogue", "Hitmontop", "Smoochum", "Elekid", "Magby", "Miltank", "Blissey", "Raikou", "Entei", "Suicune", "Larvitar", "Pupitar", "Tyranitar", "Lugia", "Ho-Oh", "Celebi", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Treecko", "Grovyle", "Sceptile", "Torchic", "Combusken", "Blaziken", "Mudkip", "Marshtomp", "Swampert", "Poochyena", "Mightyena", "Zigzagoon", "Linoone", "Wurmple", "Silcoon", "Beautifly", "Cascoon", "Dustox", "Lotad", "Lombre", "Ludicolo", "Seedot", "Nuzleaf", "Shiftry", "Nincada", "Ninjask", "Shedinja", "Taillow", "Swellow", "Shroomish", "Breloom", "Spinda", "Wingull", "Pelipper", "Surskit", "Masquerain", "Wailmer", "Wailord", "Skitty", "Delcatty", "Kecleon", "Baltoy", "Claydol", "Nosepass", "Torkoal", "Sableye", "Barboach", "Whiscash", "Luvdisc", "Corphish", "Crawdaunt", "Feebas", "Milotic", "Carvanha", "Sharpedo", "Trapinch", "Vibrava", "Flygon", "Makuhita", "Hariyama", "Electrike", "Manectric", "Numel", "Camerupt", "Spheal", "Sealeo", "Walrein", "Cacnea", "Cacturne", "Snorunt", "Glalie", "Lunatone", "Solrock", "Azurill", "Spoink", "Grumpig", "Plusle", "Minun", "Mawile", "Meditite", "Medicham", "Swablu", "Altaria", "Wynaut", "Duskull", "Dusclops", "Roselia", "Slakoth", "Vigoroth", "Slaking", "Gulpin", "Swalot", "Tropius", "Whismur", "Loudred", "Exploud", "Clamperl", "Huntail", "Gorebyss", "Absol", "Shuppet", "Banette", "Seviper", "Zangoose", "Relicanth", "Aron", "Lairon", "Aggron", "Castform", "Volbeat", "Illumise", "Lileep", "Cradily", "Anorith", "Armaldo", "Ralts", "Kirlia", "Gardevoir", "Bagon", "Shelgon", "Salamence", "Beldum", "Metang", "Metagross", "Regirock", "Regice", "Registeel", "Kyogre", "Groudon", "Rayquaza", "Latias", "Latios", "Jirachi", "Deoxys", "Chimecho", "Pok\u00e9mon Egg", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown", "Unown"]
		if id>len(names):
			return ""
		return names[id - 1]

	def __movename(self, id):

		moves = ["Pound", "Karate Chop", "Double Slap", "Comet Punch", "Mega Punch", "Pay Day", "Fire Punch", "Ice Punch", "Thunder Punch", "Scratch", "Vice Grip", "Guillotine", "Razor Wind", "Swords Dance", "Cut", "Gust", "Wing Attack", "Whirlwind", "Fly", "Bind", "Slam", "Vine Whip", "Stomp", "Double Kick", "Mega Kick", "Jump Kick", "Rolling Kick", "Sand Attack", "Headbutt", "Horn Attack", "Fury Attack", "Horn Drill", "Tackle", "Body Slam", "Wrap", "Take Down", "Thrash", "Double-Edge", "Tail Whip", "Poison Sting", "Twineedle", "Pin Missile", "Leer", "Bite", "Growl", "Roar", "Sing", "Supersonic", "Sonic Boom", "Disable", "Acid", "Ember", "Flamethrower", "Mist", "Water Gun", "Hydro Pump", "Surf", "Ice Beam", "Blizzard", "Psybeam", "Bubble Beam", "Aurora Beam", "Hyper Beam", "Peck", "Drill Peck", "Submission", "Low Kick", "Counter", "Seismic Toss", "Strength", "Absorb", "Mega Drain", "Leech Seed", "Growth", "Razor Leaf", "Solar Beam", "Poison Powder", "Stun Spore", "Sleep Powder", "Petal Dance", "String Shot", "Dragon Rage", "Fire Spin", "Thunder Shock", "Thunderbolt", "Thunder Wave", "Thunder", "Rock Throw", "Earthquake", "Fissure", "Dig", "Toxic", "Confusion", "Psychic", "Hypnosis", "Meditate", "Agility", "Quick Attack", "Rage", "Teleport", "Night Shade", "Mimic", "Screech", "Double Team", "Recover", "Harden", "Minimize", "Smokescreen", "Confuse Ray", "Withdraw", "Defense Curl", "Barrier", "Light Screen", "Haze", "Reflect", "Focus Energy", "Bide", "Metronome", "Mirror Move", "Self-Destruct", "Egg Bomb", "Lick", "Smog", "Sludge", "Bone Club", "Fire Blast", "Waterfall", "Clamp", "Swift", "Skull Bash", "Spike Cannon", "Constrict", "Amnesia", "Kinesis", "Soft-Boiled", "High Jump Kick", "Glare", "Dream Eater", "Poison Gas", "Barrage", "Leech Life", "Lovely Kiss", "Sky Attack", "Transform", "Bubble", "Dizzy Punch", "Spore", "Flash", "Psywave", "Splash", "Acid Armor", "Crabhammer", "Explosion", "Fury Swipes", "Bonemerang", "Rest", "Rock Slide", "Hyper Fang", "Sharpen", "Conversion", "Tri Attack", "Super Fang", "Slash", "Substitute", "Struggle", "Sketch", "Triple Kick", "Thief", "Spider Web", "Mind Reader", "Nightmare", "Flame Wheel", "Snore", "Curse", "Flail", "Conversion 2", "Aeroblast", "Cotton Spore", "Reversal", "Spite", "Powder Snow", "Protect", "Mach Punch", "Scary Face", "Feint Attack", "Sweet Kiss", "Belly Drum", "Sludge Bomb", "Mud-Slap", "Octazooka", "Spikes", "Zap Cannon", "Foresight", "Destiny Bond", "Perish Song", "Icy Wind", "Detect", "Bone Rush", "Lock-On", "Outrage", "Sandstorm", "Giga Drain", "Endure", "Charm", "Rollout", "False Swipe", "Swagger", "Milk Drink", "Spark", "Fury Cutter", "Steel Wing", "Mean Look", "Attract", "Sleep Talk", "Heal Bell", "Return", "Present", "Frustration", "Safeguard", "Pain Split", "Sacred Fire", "Magnitude", "Dynamic Punch", "Megahorn", "Dragon Breath", "Baton Pass", "Encore", "Pursuit", "Rapid Spin", "Sweet Scent", "Iron Tail", "Metal Claw", "Vital Throw", "Morning Sun", "Synthesis", "Moonlight", "Hidden Power", "Cross Chop", "Twister", "Rain Dance", "Sunny Day", "Crunch", "Mirror Coat", "Psych Up", "Extreme Speed", "Ancient Power", "Shadow Ball", "Future Sight", "Rock Smash", "Whirlpool", "Beat Up", "Fake Out", "Uproar", "Stockpile", "Spit Up", "Swallow", "Heat Wave", "Hail", "Torment", "Flatter", "Will-O-Wisp", "Memento", "Facade", "Focus Punch", "Smelling Salts", "Follow Me", "Nature Power", "Charge", "Taunt", "Helping Hand", "Trick", "Role Play", "Wish", "Assist", "Ingrain", "Superpower", "Magic Coat", "Recycle", "Revenge", "Brick Break", "Yawn", "Knock Off", "Endeavor", "Eruption", "Skill Swap", "Imprison", "Refresh", "Grudge", "Snatch", "Secret Power", "Dive", "Arm Thrust", "Camouflage", "Tail Glow", "Luster Purge", "Mist Ball", "Feather Dance", "Teeter Dance", "Blaze Kick", "Mud Sport", "Ice Ball", "Needle Arm", "Slack Off", "Hyper Voice", "Poison Fang", "Crush Claw", "Blast Burn", "Hydro Cannon", "Meteor Mash", "Astonish", "Weather Ball", "Aromatherapy", "Fake Tears", "Air Cutter", "Overheat", "Odor Sleuth", "Rock Tomb", "Silver Wind", "Metal Sound", "Grass Whistle", "Tickle", "Cosmic Power", "Water Spout", "Signal Beam", "Shadow Punch", "Extrasensory", "Sky Uppercut", "Sand Tomb", "Sheer Cold", "Muddy Water", "Bullet Seed", "Aerial Ace", "Icicle Spear", "Iron Defense", "Block", "Howl", "Dragon Claw", "Frenzy Plant", "Bulk Up", "Bounce", "Mud Shot", "Poison Tail", "Covet", "Volt Tackle", "Magical Leaf", "Water Sport", "Calm Mind", "Leaf Blade", "Dragon Dance", "Rock Blast", "Shock Wave", "Water Pulse", "Doom Desire", "Psycho Boost"]
		return moves[id - 1]

	def __naturename(self, id):

		natures = ["Hardy", "Lonely", "Brave", "Adamant", "Naughty", "Bold", "Docile", "Relaxed", "Impish", "Lax", "Timid", "Hasty", "Serious", "Jolly", "Naive", "Modest", "Mild", "Quiet", "Bashful", "Rash", "Calm", "Gentle", "Sassy", "Careful", "Quirky"]
		return natures[id]

	def __movetype(self, id):

		return ""

	def __expgroup(self, id):

		groups = ['Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Fast', 'Fast', 'Medium Fast', 'Medium Fast', 'Fast', 'Fast', 'Medium Fast', 'Medium Fast', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Slow', 'Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Slow', 'Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Slow', 'Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Slow', 'Slow', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Slow', 'Slow', 'Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Slow', 'Slow', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Slow', 'Slow', 'Slow', 'Slow', 'Slow', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Slow', 'Slow', 'Slow', 'Slow', 'Slow', 'Slow', 'Slow', 'Slow', 'Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Fast', 'Fast', 'Fast', 'Fast', 'Medium Fast', 'Slow', 'Slow', 'Medium Fast', 'Fast', 'Fast', 'Fast', 'Fast', 'Medium Fast', 'Medium Fast', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Fast', 'Fast', 'Medium Fast', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Fast', 'Medium Slow', 'Medium Slow', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Slow', 'Medium Fast', 'Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Slow', 'Medium Fast', 'Fast', 'Fast', 'Medium Fast', 'Medium Fast', 'Medium Slow', 'Slow', 'Medium Slow', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Slow', 'Slow', 'Fast', 'Medium Fast', 'Medium Fast', 'Fast', 'Slow', 'Slow', 'Slow', 'Slow', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Slow', 'Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Slow', 'Fast', 'Slow', 'Slow', 'Slow', 'Slow', 'Slow', 'Slow', 'Slow', 'Slow', 'Medium Slow', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Erratic', 'Erratic', 'Erratic', 'Medium Slow', 'Medium Slow', 'Fluctuating', 'Fluctuating', 'Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Fluctuating', 'Fluctuating', 'Fast', 'Fast', 'Medium Slow', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Fast', 'Medium Slow', 'Medium Fast', 'Medium Fast', 'Fast', 'Fluctuating', 'Fluctuating', 'Erratic', 'Erratic', 'Slow', 'Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Fluctuating', 'Fluctuating', 'Slow', 'Slow', 'Medium Fast', 'Medium Fast', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Medium Fast', 'Medium Fast', 'Fast', 'Fast', 'Fast', 'Fast', 'Fast', 'Medium Fast', 'Medium Fast', 'Fast', 'Medium Fast', 'Medium Fast', 'Erratic', 'Erratic', 'Medium Fast', 'Fast', 'Fast', 'Medium Slow', 'Slow', 'Slow', 'Slow', 'Fluctuating', 'Fluctuating', 'Slow', 'Medium Slow', 'Medium Slow', 'Medium Slow', 'Erratic', 'Erratic', 'Erratic', 'Medium Slow', 'Fast', 'Fast', 'Fluctuating', 'Erratic', 'Slow', 'Slow', 'Slow', 'Slow', 'Medium Fast', 'Erratic', 'Fluctuating', 'Erratic', 'Erratic', 'Erratic', 'Erratic', 'Slow', 'Slow', 'Slow', 'Slow', 'Slow', 'Slow', 'Slow', 'Slow', 'Slow', 'Slow', 'Slow', 'Slow', 'Slow', 'Slow', 'Slow', 'Slow', 'Slow', 'Slow', 'Slow', 'Fast']
		return groups[id - 1]

	def __level(self, expgroup, exp):

		levels = []
		level = 0
		if expgroup == 'Fast':
			levels = [0, 6, 21, 51, 100, 172, 274, 409, 583, 800, 1064, 1382, 1757, 2195, 2700, 3276, 3930, 4665, 5487, 6400, 7408, 8518, 9733, 11059, 12500, 14060, 15746, 17561, 19511, 21600, 23832, 26214, 28749, 31443, 34300, 37324, 40522, 43897, 47455, 51200, 55136, 59270, 63605, 68147, 72900, 77868, 83058, 88473, 94119, 100000, 106120, 112486, 119101, 125971, 133100, 140492, 148154, 156089, 164303, 172800, 181584, 190662, 200037, 209715, 219700, 229996, 240610, 251545, 262807, 274400, 286328, 298598, 311213, 324179, 337500, 351180, 365226, 379641, 394431, 409600, 425152, 441094, 457429, 474163, 491300, 508844, 526802, 545177, 563975, 583200, 602856, 622950, 643485, 664467, 685900, 707788, 730138, 752953, 776239, 800000]
		if expgroup == 'Medium Fast':
			levels = [0, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859, 8000, 9261, 10648, 12167, 13824, 15625, 17576, 19683, 21952, 24389, 27000, 29791, 32768, 35937, 39304, 42875, 46656, 50653, 54872, 59319, 64000, 68921, 74088, 79507, 85184, 91125, 97336, 103823, 110592, 117649, 125000, 132651, 140608, 148877, 157464, 166375, 175616, 185193, 195112, 205379, 216000, 226981, 238328, 250047, 262144, 274625, 287496, 300763, 314432, 328509, 343000, 357911, 373248, 389017, 405224, 421875, 438976, 456533, 474552, 493039, 512000, 531441, 551368, 571787, 592704, 614125, 636056, 658503, 681472, 704969, 729000, 753571, 778688, 804357, 830584, 857375, 884736, 912673, 941192, 970299, 1000000]
		if expgroup == 'Medium Slow':
			levels = [0, 9, 57, 96, 135, 179, 236, 314, 419, 560, 742, 973, 1261, 1612, 2035, 2535, 3120, 3798, 4575, 5460, 6458, 7577, 8825, 10208, 11735, 13411, 15244, 17242, 19411, 21760, 24294, 27021, 29949, 33084, 36435, 40007, 43808, 47846, 52127, 56660, 61450, 66505, 71833, 77440, 83335, 89523, 96012, 102810, 109923, 117360, 125126, 133229, 141677, 150476, 159635, 169159, 179056, 189334, 199999, 211060, 222522, 234393, 246681, 259392, 272535, 286115, 300140, 314618, 329555, 344960, 360838, 377197, 394045, 411388, 429235, 447591, 466464, 485862, 505791, 526260, 547274, 568841, 590969, 613664, 636935, 660787, 685228, 710266, 735907, 762160, 789030, 816525, 844653, 873420, 902835, 932903, 963632, 995030, 1027103, 1059860]
		if expgroup == 'Slow':
			levels = [0, 10, 33, 80, 156, 270, 428, 640, 911, 1250, 1663, 2160, 2746, 3430, 4218, 5120, 6141, 7290, 8573, 10000, 11576, 13310, 15208, 17280, 19531, 21970, 24603, 27440, 30486, 33750, 37238, 40960, 44921, 49130, 53593, 58320, 63316, 68590, 74148, 80000, 86151, 92610, 99383, 106480, 113906, 121670, 129778, 138240, 147061, 156250, 165813, 175760, 186096, 196830, 207968, 219520, 231491, 243890, 256723, 270000, 283726, 297910, 312558, 327680, 343281, 359370, 375953, 393040, 410636, 428750, 447388, 466560, 486271, 506530, 527343, 548720, 570666, 593190, 616298, 640000, 664301, 689210, 714733, 740880, 767656, 795070, 823128, 851840, 881211, 911250, 941963, 973360, 1005446, 1038230, 1071718, 1105920, 1140841, 1176490, 1212873, 1250000]
		if expgroup == 'Fluctuating':
			levels = [0, 4, 13, 32, 65, 112, 178, 276, 393, 540, 745, 967, 1230, 1591, 1957, 2457, 3046, 3732, 4526, 5440, 6482, 7666, 9003, 10506, 12187, 14060, 16140, 18439, 20974, 23760, 26811, 30146, 33780, 37731, 42017, 46656, 50653, 55969, 60505, 66560, 71677, 78533, 84277, 91998, 98415, 107069, 114205, 123863, 131766, 142500, 151222, 163105, 172697, 185807, 196322, 210739, 222231, 238036, 250562, 267840, 281456, 300293, 315059, 335544, 351520, 373744, 390991, 415050, 433631, 459620, 479600, 507617, 529063, 559209, 582187, 614566, 639146, 673863, 700115, 737280, 765275, 804997, 834809, 877201, 908905, 954084, 987754, 1035837, 1071552, 1122660, 1160499, 1214753, 1254796, 1312322, 1354652, 1415577, 1460276, 1524731, 1571884, 1640000]
		if expgroup == 'Erratic':
			levels = [0, 15, 52, 122, 237, 406, 637, 942, 1326, 1800, 2369, 3041, 3822, 4719, 5737, 6881, 8155, 9564, 11111, 12800, 14632, 16610, 18737, 21012, 23437, 26012, 28737, 31610, 34632, 37800, 41111, 44564, 48155, 51881, 55737, 59719, 63822, 68041, 72369, 76800, 81326, 85942, 90637, 95406, 100237, 105122, 110052, 115015, 120001, 125000, 131324, 137795, 144410, 151165, 158056, 165079, 172229, 179503, 186894, 194400, 202013, 209728, 217540, 225443, 233431, 241496, 249633, 257834, 267406, 276458, 286328, 296358, 305767, 316074, 326531, 336255, 346965, 357812, 367807, 378880, 390077, 400293, 411686, 423190, 433572, 445239, 457001, 467489, 479378, 491346, 501878, 513934, 526049, 536557, 548720, 560922, 571333, 583539, 591882, 600000]
		for i in range(0, 100):
			if exp > levels[i]:
				level = i
			else:
				break
		return level

	def __init__(self, pkm):

		orders = ['GAEM', 'GAME', 'GEAM', 'GEMA', 'GMAE', 'GMEA', 'AGEM', 'AGME', 'AEGM', 'AEMG', 'AMGE', 'AMEG', 'EGAM', 'EGMA', 'EAGM', 'EAMG', 'EMGA', 'EMAG', 'MGAE', 'MGEA', 'MAGE', 'MAEG', 'MEGA', 'MEAG']
		self.name = self.__readstring(pkm[8:18])
		self.data = pkm
		trainer = self.__readstring(pkm[20:27])
		if trainer == '' and self.name == '':
			return None
		self.personality = struct.unpack('<I', pkm[0:4])[0]
		self.trainer = {'id': struct.unpack('<I', pkm[4:8])[0],'name': trainer}
		key = xor(self.trainer['id'], self.personality)

		data = pkm[32:]
		order = self.personality % 24
		orderstring = orders[order]
		sections = {}
		for i in range(0, 4):
			section = orderstring[i]
			sectiondata = data[(i * 12):((i + 1) * 12)]
			sections[section] = self.__decryptsubsection(sectiondata, key)
		self.species = {'id': int(struct.unpack('<H', sections['G'][0:2])[0])}
		self.species['name'] = self.__speciesname(self.species['id'])
		self.exp = int(struct.unpack('<I', sections['G'][4:8])[0])
		self.expgroup = self.__expgroup(self.species['id'])
		self.level = self.__level(self.expgroup, self.exp)

		moves = []
		for i in range(0, 4):
			item = {}
			item['id'] = int(struct.unpack('<H', sections['A'][(i * 2):((i + 1) * 2)])[0])
			if item['id'] == 0:
				continue
			item['name'] = self.__movename(item['id'])
			item['pp'] = int(struct.unpack('<B', sections['A'][(i + 8)])[0])
			moves.append(item)
		self.moves = moves
		self.nature = self.__naturename(self.personality % 25)
		self.ivs = self.__getivs(int(struct.unpack('<I', sections['M'][4:8])[0]))
		self.evs = self.__getevs(sections['E'])

	def __getivs(self, value):

		iv = {}
		bitstring = str(str(bin(value)[2:])[::-1] + '00000000000000000000000000000000')[0:32]
		iv['hp'] = int(bitstring[0:5], 2)
		iv['attack'] = int(bitstring[5:10], 2)
		iv['defence'] = int(bitstring[10:15], 2)
		iv['speed'] = int(bitstring[15:20], 2)
		iv['spatk'] = int(bitstring[20:25], 2)
		iv['spdef'] = int(bitstring[25:30], 2)
		return iv

	def __getevs(self, section):

		ev = {}
		ev['hp'] = int(struct.unpack('<B', section[0])[0])
		ev['attack'] = int(struct.unpack('<B', section[1])[0])
		ev['defence'] = int(struct.unpack('<B', section[2])[0])
		ev['speed'] = int(struct.unpack('<B', section[3])[0])
		ev['spatk'] = int(struct.unpack('<B', section[4])[0])
		ev['spdef'] = int(struct.unpack('<B', section[5])[0])
		ev['cool'] = int(struct.unpack('<B', section[6])[0])
		ev['beauty'] = int(struct.unpack('<B', section[7])[0])
		ev['cute'] = int(struct.unpack('<B', section[8])[0])
		ev['smart'] = int(struct.unpack('<B', section[9])[0])
		ev['tough'] = int(struct.unpack('<B', section[10])[0])
		ev['feel'] = int(struct.unpack('<B', section[11])[0])
		return ev

	def __decryptsubsection(self, data, key):

		if len(data) != 12:
			return []
		a = xor(struct.unpack('<I', data[0:4])[0], key)
		b = xor(struct.unpack('<I', data[4:8])[0], key)
		c = xor(struct.unpack('<I', data[8:12])[0], key)
		return struct.pack('<III', a, b, c)

	def __readstring(self, text):

		chars = "0123456789!?.-         ,  ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
		ret = ""
		for i in text:
			c = int(i) - 161
			if c<0 or c>len(chars):
				ret = ret + " "
			else:
				ret = ret + chars[c]
		return ret.strip()

