import json, struct, sys, os
from operator import xor
from Gen3Pokemon import Gen3Pokemon

class Gen3Save:

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

	def __getindex(self, data):

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

	def __init__(self, filename):

		f = open(filename, "rb")
		data = bytearray(f.read())

		filea = data[0:57344]
		fileb = data[57344:114688]

		a = self.__getindex(filea)
		b = self.__getindex(fileb)

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

		self.__process(savedata)

	def __process(self, savedata):

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

		self.name = self.__readstring(sections[0][0:7]).strip()
		self.team = []
		self.boxes = []

		gamecode = int(struct.unpack('<I', sections[0][172:176])[0])
		self.game = 'emerald'
		if gamecode == 0:
			self.game = 'rubysapphire'
		if gamecode == 1:
			self.game = 'fireredleafgreen'
		if gamecode == 1:
			self.teamcount = int(struct.unpack('<I', sections[1][52:56])[0])
			teamoffset = 56
		else:
			self.teamcount = int(struct.unpack('<I', sections[1][564:568])[0])
			teamoffset = 568

		gender = int(struct.unpack('<B', chr(sections[0][8]))[0])
		self.gender = ''
		if gender == 0:
			self.gender = 'boy'
		if gender == 1:
			self.gender = 'girl'

		dex = bytearray()
		for i in range(5, 14):
			dex = dex + sections[i]
		dex = dex[4:33604]
		for i in range(0, 420):
			pkm = Gen3Pokemon(dex[(i * 80):((i + 1) * 80)])
			if not(hasattr(pkm, 'species')):
				continue
			self.boxes.append(pkm)
		for i in range(0, self.teamcount):
			ofs = teamoffset + (i * 100)
			pkm = Gen3Pokemon(sections[1][ofs:(ofs + 80)])
			if not(hasattr(pkm, 'species')):
				continue
			self.team.append(pkm)

if __name__ == "__main__":

	if len(sys.argv) < 2:
		sys.exit('Usage: %s [save_file]' % sys.argv[0])

	if not os.path.exists(sys.argv[1]):
		sys.exit('ERROR: File %s not found' % sys.argv[1])

	sf = Gen3Save(sys.argv[1])
	print sf.name + ' (' + sf.gender + ')'
	print sf.teamcount
	for pkm in sf.team:
		print pkm.species['name'] + '/' + pkm.name + ' Level ' + str(pkm.level)

