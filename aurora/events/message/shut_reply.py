import bot, aura

async def shut_reply(msg):
	if not (
		msg.reference != None # iWaroz & qsyl
		and msg.author.id in [715902532110516304, 652878672180543488] \
		and msg.content in ['shut', 'stfu', 'shut up']
	):
		return

	replied = msg.reference.message_id
	ms = await msg.channel.fetch_message(replied)
	await ms.author.add_roles(aura.role.muted)
	await msg.reply(f'<:gangsta:758740652145770536>  {ms.author.mention} has been stfu\'d')