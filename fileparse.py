import fnmatch
import os
import mmap

# i is used to keep count of files matching android_*.png
i = 0

# list to store all the filenames with full path
results = []
notfound = []

# Traverse current working directory and all subdirectories
for root, dirs, files in os.walk(os.getcwd()):
	if 'bin' in dirs:
		dirs.remove('bin')
	if 'gen' in dirs:
		dirs.remove('gen')
	for	_file in files:
		# For each file, check if the file matches the pattern
		if fnmatch.fnmatch(_file, 'android_*.png'):
			# If match found, store the file with full path in results list
			results.append(os.path.join(root, _file))
			i = i + 1

# For every file in results, search for the filename(minus .png) in the directory structure
for element in results:
	print element
	# Get the filename minus .png. This will be searched in the directory structure
	temp = element.split("/")[-1][:-4]
	# Traverse current working directory and all subdirectories
	found = 0
	for root, dirs, files in os.walk(os.getcwd()):
		if 'bin' in dirs:
			dirs.remove('bin')
		if 'gen' in dirs:
			dirs.remove('gen')
		for _file in files:
			# For each file, check if temp is found in the file
			f = open(os.path.join(root, _file))
			# filecontent = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
			filecontent = f.read()
			if temp in filecontent:
				found = 1
				print "Found " + temp + " in file: " + os.path.join(root, _file)
				replacewith = temp[8:]
				print replacewith
				filecontent = filecontent.replace(temp,replacewith)
				f = open(os.path.join(root, _file),"w")
				f.write(filecontent)
			f.close()
	if found == 0:
		print "NOT FOUND"
		notfound.append(element)

print "Total Number of files:"
print i

print "Not Used files"
count = 0
for elems in notfound:
	print elems
	count=count+1
	
print "Number of Unused files"
print count

# Now rename all files in results list
for items in results:
	(dirName, fileName) = os.path.split(items)
	newfileName = os.path.join(dirName,fileName[8:])
	os.rename(items,newfileName)
	print newfileName