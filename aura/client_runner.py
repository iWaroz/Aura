import importlib, os

import disnake

def run(self, token, bot):
	# initialize bot data
	dirc = bot.__name__
	folders = os.listdir(dirc)

	def modules(name):
		try:
			for mod in os.listdir(dirc + '/' + name):
				if mod.endswith('.py'):
					yield mod
		except:
			pass
	
	# import every event file
	for evn in os.listdir(dirc + '/events'):
		if evn == '__pycache__': 
			continue

		self.event_callbacks[evn] = []

		for mod in modules('events/' + evn):
			evnmod = importlib.import_module(dirc + ".events." + evn + '.' + mod[:-3])
			callback = getattr(evnmod, mod[:-3])
			self.event_callbacks[evn].append(callback)

	# loading object models
	for mod in modules('objects'):
		if mod == 'member.py':
			mbmpy = importlib.import_module(dirc + '.objects.' + mod[:-3])
			print(dir(mbmpy))
			for i in dir(mbmpy):
				if hasattr(getattr(mbmpy, i), '_aura'):
					setattr(disnake.Member, i, getattr(mbmpy, i))
			
	# loading setup files
	for mod in modules('setup'):
		if mod == 'consts':
			consts = importlib.import_module(dirc + '.setup.consts')
			import aura
			aura.const = consts