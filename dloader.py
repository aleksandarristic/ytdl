#!/usr/bin/env python

import os
import sys

config = {
	'a': {
		'message': 'Download Audio (mp3) to Downloads/music with YouTube-DL',
		'command': 'youtube-dl -o "/data/data/com.termux/files/home/storage/downloads/music/%(title)s.%(ext)s" -x --audio-format mp3 -i'
	},
	'v': {
		'message': 'Download Video to Downloads/video with YouTube-DL',
		'command': 'youtube-dl -o "/data/data/com.termux/files/home/storage/downloads/video/%(title)s.%(ext)s" -i'
	},
#	'd': {
#		'message': 'Download file to Downloads with Wget',
#		'command': 'wget -P /data/data/com.termux/files/home/storage/downloads/'
#	},
#	'r': {
#		'message': 'Download all recursively to Downloads with Wget',
#		'command': 'wget --recursive --no-parent -P /data/data/com.termux/files/home/storage/downloads/'
#	},
	'q': {
		'message': 'Quit - do nothing',
		'command': None
	}
}

class Choice(object):
	def __init__(self, config, message):
		self.config = config
		self.message = message

		self.possible_choices = self.config.keys()
		self.selection_done = False
		self.choice = None

	def select(self):
		while not self.selection_done:
			self.choice = None
			self.print_choices()
			self.choice = input('> ')

			if self.choice not in self.possible_choices:
				print('ERROR: please select one of the options before proceeding!')
			else:
				self.selection_done = True
	
	def print_choices(self):
		print(self.message)
		for k, v in self.config.items():
			print("\t%s) %s" % (k, v.get('message')))
	
	def command(self):
		if self.selection_done:
			return self.config.get(self.choice).get('command')
		return None


chooser = Choice(config, "What do you want to do?")
current_path = os.getcwd()
url = sys.argv[1]

chooser.select()
log = "2>&1 | tee /data/data/com.termux/files/home/storage/downloads/ytdl.log"
if chooser.command() is not None:
	command = '%s %s %s' % (chooser.command(), url, log)
	os.system(command)

print('Bye!')