import regex as re

import bot

def filter_ascii(text):
	text = (
		text.replace('-', '_')
				.replace(' ', '_')
				.lower()
	)
	return ''.join(re.split(r'\W', text))

class channel:
	def __getattr__(self, name):
		for channel in bot.get_guild(bot.server).channels:
			if filter_ascii(channel.name) == name:
				return channel

channel = channel()

class role:
	def __getattr__(self, name):
		for role in bot.get_guild(bot.server).roles:
			if filter_ascii(role.name) == name:
				return role

role = role()

def property(fun):
	fun._aura = True
	return __builtins__.property(fun)

def method(fun):
	fun._aura = True
	return fun

def highest