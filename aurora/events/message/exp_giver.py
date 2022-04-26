import random

import bot, aura

async def exp_giver(msg):
	channel_xps = {
		aura.channel.general: (15, 25),
		aura.channel.media: (10, 15),
		aura.channel.memes: (15, 20),
		aura.channel.development: (1, 5)
	}
	
	if not msg.channel in channel_xps:
		return

	msg.author.exp += 1
	print(msg.author.exp)
	
	xp_reward = random.randint(
		*channel_xps[msg.channel]
  )

	multiplier = msg.author.xp_boost.multiplier
	msg.author.exp += int(xp_reward * multiplier)
	print(msg.author.exp)
	
	"""
    with aura.member(msg.author) as user:
        multiplier = user.xp_boost.multiplier
        user.exp += int(xp_reward * multiplier)

    top_exp_role = aura.util.highest(
        aura.config.role_exp_reqs,
        user.exp
    )

    if not user.has_role(top_exp_role) and top_exp_role != None:
        await user.remove_roles(*[
            role for role in aura.config.level_roles if user.has_role(role)
        ])
        await user.add_roles(top_exp_role)
        level = aura.config.level_roles[top_exp_role]
        await msg.reply('',
            embed=aura.embed(
                description=f'**LEVEL UP!** Chatting {level-1} **➜** {level}\n{user.mention}, you are now a {top_exp_role.mention}!',
                color=bot.color
            )
        )
	"""