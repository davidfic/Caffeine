import os

## find files for each CPU/config and send them to caffeine server to the appropriate directory
suffix = 'png'
png_files = []
OCAP = 'ocap'
cur_dir = os.path.dirname(os.path.abspath(__file__))
for root, dirs, files in os.walk(os.path.join(cur_dir,'.')):
	if suffix in files:
		if OCAP in files:
			print hello
		# png_files.extend([os.path.join(root, f) for f in files ])




