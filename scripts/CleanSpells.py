import json

# Load json
with open('../data/dnd_spells.json','r') as f:
	spells = json.load(f)

# Alphabetize spells by 'name'
spells = sorted(spells, key=lambda k: k['name'])

# Modify 'name' to remove '(Ritual)' and add 'ritual' key
for spell in spells:
	if spell['name'][-8:] == '(Ritual)':
		spell['name'] = spell['name'][:-9]
		spell['ritual'] = True
	else:
		spell['ritual'] = False

# Modify 'duration' to remove 'Concentration, ' and add 'concentration' key
for spell in spells:
	if spell['duration'][:13] == 'Concentration':
		spell['duration'] = (spell['duration'][15].upper() + spell['duration'][16:])
		spell['concentration'] = True
	else:
		spell['concentration'] = False

# Add spell component keys to dict
for spell in spells:
	comps = spell['components']
	spell['verbal'] = ('V' in comps)
	spell['somatic'] = ('S' in comps)
	spell['material'] = ('M' in comps)
	paren = comps.find('(')
	if paren > 0:
		spell['material_components'] = comps[paren+1:-1]
		spell['components'] = comps[:paren-1]
	else:
		spell['material_components'] = ''

# Modify 'page' keys
for spell in spells:
	onespace = spell['page'].find(' ')
	twospace = spell['page'].find('  ')
	source = (spell['page'][twospace + 2:] + ' p. ' + spell['page'][onespace + 1:twospace])
	source = source.replace('from EE Players Companion','Elemental Evil')
	source = source.replace('Players Handbook','Player\'s Handbook')
	source = source.replace('from ','')
	spell['page'] = source

# Save json
with open('../data/dnd_spells_clean.json','w') as f:
	json.dump(spells,f)

