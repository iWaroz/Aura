import bot, aura

async def meme_voter(msg):
	if msg.channel != aura.channel.memes:
		return
	if len(msg.attachments) == 0:
		return

	await msg.add_reaction('<:upvote:699614509777551391>')
	await msg.add_reaction('<:downvote:699614552148672593>')