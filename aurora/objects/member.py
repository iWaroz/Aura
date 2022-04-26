import aura

uuid = aura.db.property('uuid', default='')
username = aura.db.property('username', default='')
exp = aura.db.property('exp', default=0)
dono = aura.db.property('donations', default=0)

@aura.property
def xp_boost(self):
	boost = 0
	explanation = {aura.role.:0, aura.role.nitro_booster:0}
	if has_role(self.obj.nitro_booster, aura.role.shiba_cultist):
		boost += 5
		explanation[aura.role.shiba_cultist] = 5
	if has_role(self.obj, aura.role.nitro_booster):
		boost += 25
		explanation[aura.role.nitro_booster] = 25
	donor_boosts = {
		aura.role.midas_100m: 30,
		aura.role.philanthropic_50m: 20,
		aura.role.bountiful_20m: 10,
		aura.role.charitable_10m: 5,
		aura.role.generous_5m: 3,
		aura.role.nice_2m: 1
	}
	donorrole = toprole(self.obj, donor_boosts)
	if donorrole[0] == None:
		explanation[roles.nice_2m] = 0
	else:
		boost += donorrole[1]
		explanation[donorrole[0]] = donorrole[1]
	explanation = {k: v for k, v in sorted(explanation.items(), key=lambda item: item[1], reverse=True)}
	return boost, explanation