import sys, os, re

#open file and give usage message


if len(sys.argv) < 2:
	sys.exit("Usage: %s filename" % sys.argv[0])

filename = sys.argv[1]
if not os.path.exists(filename):
	sys.exit("Error: File '%s' not present" % sys.argv[1])
 
f = open(filename)

#make the regular expression

name_regex = re.compile(r"[\s\w]+(?=\sbatted\b)")
bating_regex = re.compile(r"(?<=\bbatted\b\s\b)\d+\b")
hiting_regex = re.compile(r"(?<=\bwith\b\s\b)\d+\b")

#define the function that get the name/bat time/hit time

def find_one_name(test):
	match = name_regex.match(test)
	if match is not None:
		return match.group(0)
	else:
		return False

def find_one_bat(test1):
	match = re.search(bating_regex,test1)
	if match is not None:
		#print match.group
		return match.group(0)
	else:
		return False

def find_one_hit(test1):
	match = re.search(hiting_regex,test1)
	if match is not None:
		#print match.group
		return match.group(0)
	else:
		return False

#define list and dictionary

names=[]
batdic={}
hitdic={}
ratdic={}

for line in f:
	nam=find_one_name(line.rstrip())
	if (nam<>False)and(nam not in names) :
		names.append(nam)
		batdic[nam]=0
		hitdic[nam]=0
		ratdic[nam]=0

f.close()

#the adding process

f=open(filename)

for line in f:
	s=line.rstrip()
	nam=find_one_name(s)
	if nam<>False :
		b=find_one_bat(s)
		h=find_one_hit(s)
		batdic[nam]+=int(b)
		hitdic[nam]+=int(h)

f.close()

#calculate the percentage

for name in names:
	if batdic[name]<>0:
		ratdic[name]=hitdic[name]/float(batdic[name])
	else:
		ratdic[name]=0

#get sorted percentage

newnm=sorted(ratdic.items(), key=lambda d: d[1] ,reverse = True)
#print newnm
for group in newnm:
	print "%s: %.3f"%(group[0],group[1])