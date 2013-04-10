import os

# CPU types
i686 		= 'i686'
ARM 		= 'arm'
POWERPC 	= 'powerpc'
MIPS 		= 'mips'

# Config Types

OCAP 		= 'OCAP'
PERSONAL 	= 'Personal'
STANDARD 	= 'Standard'

suffix 		= 'png'

cur_dir 	= os.path.dirname(os.path.abspath(__file__))
png_files 	= []



def rsync_files(cpu, config):
	os.system("rsync -auv --delete 10.10.10.12:/var/www/caffeine/app/static/images/caffeine" + cpu + "/" + config )


def find_cpu(item):
	if ARM in item:
		return ARM
	elif POWERPC in item:
		return POWERPC
	elif i686 in item:
		return i686
	elif MIPS in item:
		return MIPS
	else:
		return ""

for (path, dirs, files) in os.walk(cur_dir):
	for item in files:
		if item.endswith(suffix):
			if item.startswith(OCAP):
				rsync_files(find_cpu(item), OCAP)
			elif item.startswith(PERSONAL):
				rsync_files(find_cpu(item), OCAP)
			elif item.startswith(STANDARD):
				rsync_files(find_cpu(item), OCAP)
			else:
				print "not sure what this is " + item

	



