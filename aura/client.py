import disnake

from . import client_runner

class Client(disnake.Client):
	def __init__(self, *args, **kwargs):
		self.event_callbacks = {}
		super().__init__(*args, **kwargs)

	def set_server(self, server):
		# preliminary function to setup configuration before running anything
		self.server = server

	def run(self, token, bot):
		# load stuff
		client_runner.run(self, token, bot)

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