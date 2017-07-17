# f = open("names.txt", "a")
# f.write("Street: Azmi\n")
# f.write("Phone: 06-435333\n")
# f.close()

with open("names.txt", "r") as f:
	f.seek(15)
	print(f.read())

print('Bye')
