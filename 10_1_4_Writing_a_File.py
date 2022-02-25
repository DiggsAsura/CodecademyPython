# Chap 10
# 1. Learn Python: Files
# 4. Writing a File

# Yes, this is the good stuff. Savefile for my future rpg? xD

# with open needs another argument, "w" (write) 
# with open("file.txt", "w") as file:
#		file_write("What an incredible file")
#
# default argument is "r" (read)

with open("bad_bands.txt", "w") as bad_bands_doc:
	bad_bands = bad_bands_doc.write("Creed")

print(bad_bands) # ok interesting, this prints 5. apparently
								 # cant to much with the variable, or??

# Guess I can do it like this, but.. should be another
# way to use this information? Guess just have to proceed
# with the course. 
with open("bad_bands.txt", "r") as bad_bands_read:
	bad_bands_r = bad_bands_read.readline()
	
print(bad_bands_r)
