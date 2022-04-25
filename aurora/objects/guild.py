import aura

lootboxes = aura.db.property('lootboxes', [])


async def lootboxes_new(msg):
	with msg.author as user:
		with msg.guild as guild:
			for lbx in guild.lootboxes:
				if aura.roll_percent(lbx["chance"] * user.magic_find.multiplier * 0.420):
					lbx["amount"] -= 1
					await message.reply(
						'', 
						embed=discord.Embed(
							description=f'**Congratulations!** You found a **{lbx["title"]}**! (+{user.magic_find.value}% Magic Find)\n*This prize is valued at {lbx["value"]:,} coins and there are {lbx["amount"]} still left to be obtained*', 
							color=bot.color
						)
					)
					await aura.channel.unclaimed_prizes.send(
						'',
						embed=discord.Embed(
							description=f"{user.mention} won a **{lbx['title']}**.\n- IGN: {user.username}",
							color=0xe86059
						),
						components=[
							aura.component.row(
								aura.component.button(
									style="red",
									label="Mark as Claimed",
									custom_id="lbxclaimed"
								)
							)
						]
					)


async def lootboxes_old(message):
	lbxs = Lade.get('lootboxes')
	mf = user.magic_find()[0]
	amf = mf
	#print('mf:', mf)
	winnings = []
	for it in range(len(lbxs)):
		i = lbxs[it]
		chance = (i['chance'] * (1 + (amf/100))) / 100
		chance *= 0.420
		#print(chance)
		if chance > random.random():
			await message.reply('', embed=discord.Embed(description=f'**Congratulations!** You found a **{i["title"]}**! (+{mf}% Magic Find)\n*This prize is valued at {commaformat(i["value"])} coins and there are {i["amount"]-1} still left to be obtained*', color=botcolor(message)))
			print('won', i["title"], chance)
			winnings.append(it)
			today.lootboxes += 1
			today.lbxvalue += i["value"]
			await message.guild.get_channel(915581263522455573).send('', embed=discord.Embed(description=f"{message.author.mention} won a **{i['title']}**.\n<:dot:827907423381487657> IGN: {user.username}", color=0xe86059), components=[create_actionrow(create_button(style=ButtonStyle.red, label="Mark as Claimed", custom_id='lbxclaimed'))])