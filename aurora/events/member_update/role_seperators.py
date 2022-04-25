import bot, aura

async def role_seperators(before, after):
	if len(before.roles) == len(after.roles):
		return
		
	server_roles = after.guild.roles
	uroles = []
	rolesl = after.roles
	rolestoremove = []
	rolestoadd = []
	
	for i, n in zip(server_roles, range(len(server_roles))):
		if '  ' in i.name:
			if len(uroles) > 0 and i.position < after.top_role.position:
				rolestoadd.append(after.guild.get_role(i.id))
				uroles = []
			else:
				rolestoremove.append(after.guild.get_role(i.id))
		if has_role(after, i.id) and not i.name == "@everyone" and not '  ' in i.name:
			uroles.append(i)
	await after.remove_roles(*rolestoremove)
	await after.add_roles(*rolestoadd)