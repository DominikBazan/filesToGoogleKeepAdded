import os
import gkeepapi
import sys

keep = gkeepapi.Keep()
success = keep.login(sys.argv[2], sys.argv[3])
directory = sys.argv[1]

for filename in os.listdir(directory):
	if filename.endswith(".txt"):
		with open("./files/" + filename, 'r') as mf:
			note = keep.createNote(filename[:-4], mf.read())
			note.pinned = True
			note.color = gkeepapi.node.ColorValue.White
	else:
		print("ERROR")
keep.sync()

