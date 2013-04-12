from flask import render_template, send_file
from app import app
import os

chips = {
	"i686": "i686",
	"powerpc": "PowerPC",
	"mips": "MIPS",
	"arm": "ARM"
}

confs = {
	"standard": "Standard",
	"personal": "Personal",
	"ocap":	"OCAP11",
}

#use lstrip in the future
def strip(filename):
	replacer = "/Users/davidfic/Dropbox/Projects/web/caffeine/app/static/images/caffeine"
	return filename.replace(replacer,'')


def all_images(image_path):
	cur_dir = os.path.dirname(os.path.abspath(__file__))
	for root, dirs, files in os.walk(os.path.join(cur_dir,image_path)):
		for file in files:
			file = os.path.join(root, file)
			#app.logger.debug(file)
			yield strip(file)

def get_images(image_path, chip, config):
	for file in all_images(image_path):
		#app.logger.debug(image_path)
		conf_cpu = "%s-%s" % (confs.get(config), chip)
		if conf_cpu in file:
			#app.logger.debug(file)
			yield file

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html",
		title = 'CaffeineMark Results')

@app.route('/static/images/caffeine<path:filename>')
def custom_static(filename):
	return send_file(filename)

@app.route('/caffeine')
@app.route('/caffeine-<chip>/')
@app.route('/caffeine-<chip>-<configuration>')
def caffeinemips(chip=None,configuration=None):
	if not chip and not configuration:
		return render_template("caffeine.html",
			title = "All the CaffeineMark Numbers",
			files = all_images('static/images/caffeine'),configuration="",cpu="All")
	elif not configuration:
		app.logger.debug(chips.get(chip))
		return render_template("caffeine.html",
			title = "All the " + chip + " Numbers",
			files = all_images('static/images/caffeine'),configuration="All",cpu=chips.get(chip,"Unknown"))

	return render_template("caffeine.html",
		title = 'Caffeine Mark numbers',
		files=get_images('static/images/caffeine/',chip,configuration),
		configuration=confs.get(configuration,"unknown"), cpu=chips.get(chip,"unknown"))



