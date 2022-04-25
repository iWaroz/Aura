import importlib, os

import disnake

class Client(disnake.Client):
	def __init__(self, *args, **kwargs):
		self.event_callbacks = {}
		super().__init__(*args, **kwargs)

	def set_server(self, server):
		# preliminary function to setup configuration before running anything
		self.server = server
	
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
			if mod == 'emember.py':
				mbmpy = importlib.import_module(dirc + '.objects.' + mod[:-3])
				print(dir(mbmpy))
				print(mbmpy.__annotations__)
				
		# loading setup files
		for mod in modules('setup'):
			if mod == 'consts':
				consts = importlib.import_module(dirc + '.setup.consts')
				import aura
				aura.const = consts
		
		# run the actual bot
		super().run(token)

	# dynamically create event functions to handle any event type, else super it
	def __getattr__(self, name):
		if not name in ["on_message", "on_ready", "on_member_update"]:
			return getattr(super(), name)

		relevant_callbacks = self.event_callbacks.get(name[3:], [])

		async def event_handler(*args, **kwargs):
			for fun in relevant_callbacks:
				await fun(*args, **kwargs)

		return event_handler