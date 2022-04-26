import os

import aura, bot

bot.set_server(677155964188753921)

import aurora

bot.run(
	os.getenv('discord_token'),
	bot=aurora
)

# Test