import aura

prize = aura.db.property('prize', '')
value = aura.db.property('value', 0)
donor = aura.db.property('donor', '')
left = aura.db.property('left', 0)

for lbx in aura.obj.lootbox.list:
	print(lbx.prize, '*', lbx.left)

