from flask import render_template, send_file
from app import app
import os
import re

chips = {
	"i686": "i686",
	"powerpc": "PowerPC",
	"mips": "Mips",
	"arm": "ARM"
}

confs = {
	"standard": "Standard",
	"personal": "Personal",
	"ocap":	"OCAP11",
}

def strip(filename):
	replacer = "/Users/davidfic/Dropbox/Projects/web/caffeine/app/static/images/caffeine"
	return filename.replace(replacer,'')
#lstrip to replace my replace	



#Personal-powerpc-e500-linux-gnu3-staticlib-555-fixedpoint-bspio_average_120.jpg

# def all_files(root,patterns='*', single_level=False, yield_folders=False):
#         patterns = patterns.split(';')
#         for path, subdirs, files in os.walk(root):
#             if yield_folders:
#                 fields.extend(subdirs)
#             files.sort()
#             for name in files:
# 				for in patterns:
# 					if fnmatch.fnmatch(name, pattern):
# 						yield os.path.join(path,name)
# 					break
#             if single_level:
#                 break
def all_images(image_path):
	cur_dir = os.path.dirname(os.path.abspath(__file__))
	for root, dirs, files in os.walk(os.path.join(cur_dir,image_path)):
		for file in files:
			file = os.path.join(root, file)
			app.logger.debug(file)
			yield strip(file)
			


def get_images(image_path, chip, config):
	for file in all_images(image_path):
		app.logger.debug(image_path)
		conf_cpu = "%s-%s" % (confs.get(config), chip)
		if conf_cpu in file:	
			app.logger.debug(file)
			yield file
	
@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html", 
		title = 'CaffeineMark Results')
#/Users/davidfic/Dropbox/Projects/web/caffeine/app/static/images/caffeine/OCAP11-i686-pc-linux-gnu3-staticlib-565-bspio-jit_2336.jpg
@app.route('/static/images/caffeine<path:filename>')
def custom_static(filename):
	return send_file(filename)
	
# @app.route('/caffeine-all')
# def caffeineshowall():
# 	return render_template("caffeine.html",title = 'All the results', 
# 		files=get_images('static/images/caffeine/'),)

@app.route('/caffeine')
@app.route('/caffeine-<chip>/', defaults={'configuration': 'all'})
@app.route('/caffeine-<chip>-<configuration>')
def caffeinemips(chip=None,configuration=None):
	if not chip and not configuration:
		return render_template("caffeine.html",
			title = "All the CaffeineMark Numbers",
			files = all_images('static/images/caffeine'),configuration="",cpu="All")
	return render_template("caffeine.html",
		title = 'Caffeine Mark numbers', 
		files=get_images('static/images/caffeine/',chip,configuration),
		configuration=configuration, cpu=chips.get(chip,"unknown"))
	# elif configuration == 'ocap':
	# 	return render_template("caffeine-%s-ocap.html" % chip,
	# 		title = 'MIPS numbers', files=getImages('static/images/caffeine/mips/ocap'), configuration=configuration, cpu=cpu)
	# elif configuration == 'standard':
	# 	return render_template("caffeine-mips-standard.html",
	# 		title = 'MIPS numbers for Standard', files=getImages('static/images/caffeine/mips/standard'), configuration=configuration, cpu=cpu)
	# else:
	# 	return render_template("caffeine-mips.html",
	# 		title = 'MIPS numbers', files=getImages('static/images/caffeine/mips/'), cpu=cpu )


# @app.route('/caffeine-arm/', defaults={'configuration': 'all'})
# @app.route('/caffeine-arm-<configuration>')
# def caffeinearm(configuration):
# 	cpu = "ARM"
# 	if configuration == 'personal':
# 		return render_template("caffeine-arm-personal.html",
# 			title = 'ARM numbers', files=getImages('static/images/caffeine/arm/personal'), configuration=configuration, cpu=cpu)
# 	elif configuration == 'ocap':
# 		return render_template("caffeine-arm-ocap.html",
# 			title = 'ARM numbers', files=getImages('static/images/caffeine/arm/ocap'), configuration=configuration, cpu=cpu)
# 	elif configuration == 'standard':
# 		return render_template("caffeine-arm-standard.html",
# 			title = 'ARM numbers', files=getImages('static/images/caffeine/arm/standard'), configuration=configuration, cpu=cpu)
# 	else:
# 		return render_template("caffeine-arm.html",
# 			title = 'ARM numbers', files=getImages('static/images/caffeine/arm/'),  cpu=cpu)


# @app.route('/caffeine-i686/', defaults={'configuration': 'all'})
# @app.route('/caffeine-i686-<configuration>')
# def caffeinei686(configuration):
# 	cpu = 'i686'
# 	if configuration == 'personal':
# 		return render_template("caffeine-i686-personal.html",
# 			title = 'i686 numbers', files=getImages('static/images/caffeine/i686/personal'), configuration=configuration, cpu=cpu)
# 	elif configuration == 'ocap':
# 		return render_template("caffeine-i686-ocap.html",
# 			title = 'i686 numbers', files=getImages('static/images/caffeine/i686/ocap'), configuration=configuration, cpu=cpu)
# 	elif configuration == 'standard':
# 		return render_template("caffeine-i686-standard.html",
# 			title = 'i686 numbers', files=getImages('static/images/caffeine/i686/standard'), configuration=configuration, cpu=cpu)
# 	else:
# 		return render_template("caffeine-i686.html",
# 			title = 'i686 numbers', files=getImages('static/images/caffeine/i686/'),  cpu=cpu)

# @app.route('/caffeine-powerpc/', defaults={'configuration': 'all'})
# @app.route('/caffeine-powerpc-<configuration>')
# def caffeinepowerpc(configuration):
# 	cpu = 'PowerPC'
# 	if configuration == 'personal':
# 		return render_template("caffeine-powerpc-personal.html",
# 			title = 'PowerPC numbers', files=getImages('static/images/caffeine/powerpc/personal'), configuration=configuration, cpu=cpu)
# 	elif configuration == 'ocap':
# 		return render_template("caffeine-powerpc-ocap.html",
# 			title = 'PowerPC numbers', files=getImages('static/images/caffeine/powerpc/ocap'), configuration=configuration, cpu=cpu)
# 	elif configuration == 'standard':
# 		return render_template("caffeine-powerpc-standard.html",
# 			title = 'PowerPC numbers', files=getImages('static/images/caffeine/powerpc/standard'), configuration=configuration, cpu=cpu)
# 	else:
# 		return render_template("caffeine-powerpc.html",
# 			title = 'PowerPC numbers', files=getImages('static/images/caffeine/powerpc/'),  cpu=cpu)


