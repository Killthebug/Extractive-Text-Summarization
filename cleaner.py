import re
import sys
import os

TRAIN_PATH  = "./training/"
TEST_PATH = "./test/"
VALIDATION_PATH = "./validation/"

outfile = None

if __name__ == "__main__" :

	training = os.listdir(TRAIN_PATH)
	testing = os.listdir(TEST_PATH)
	validation = os.listdir(VALIDATION_PATH)

	for file in training:
		f = open(TRAIN_PATH+ file, 'r')
		try:
			lines = f.readlines()
		except UnicodeDecodeError:
			print(file)
			continue
		lines = lines[1:]
		en = {}
		outfile = "./Only_Words/"+ file
		string = ""
		for line in lines :
			p = re.compile('^@.*:.*')
			m = p.match(line)
			if m:
				pos = line.find(":")
				entity = line[:pos]
				name = line[pos+1:].strip()
				en[entity] = name
			else :
				if line.strip() is not "":
					k = re.compile('$([ \t][0-9]+)')
					o = k.match(line)
					if o :
						line = line.strip()[:-1].strip()
					else :
						line = line.strip()
					string += line + " "
		lis = string.split()

		for i,word in enumerate(lis) :
			p = re.compile('^@entity[0-9]+')
			m = p.match(word)
			if m:
				try:
					lis[i] = en[word]
				except KeyError:
					print("IGNORED : ", file)
					
		string = " ".join(lis)
		xx = open(outfile,'w')
		xx.write(string)

	
