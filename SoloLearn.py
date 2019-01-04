import sys

names={}


for line in sys.stdin.readlines():
	line = line.strip()

	if 'failure' in line:

		name = line.split()[3]

		if name in names:

			names[name] +=1
		else:
			names[name] = 1

print(names)