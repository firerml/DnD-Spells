import json
import os, subprocess

# Load json
with open('../data/dnd_spells_clean.json','r') as f:
	spells = json.load(f)

# Ensure directory for LaTeX compilation
if not os.path.isdir("LatexCompile"):
	os.mkdir("LatexCompile")

# Write LaTex code for each spell
with open('LatexCompile/spells_text.tex','w') as f:
	f.write(r'\documentclass[10pt,twocolumn]{report}' + '\n\n')
	f.write(r'\usepackage{multicol,float}' + '\n\n')
	f.write(r'\oddsidemargin=0in' + '\n' + r'\evensidemargin=0in' +'\n')
	f.write(r'\topmargin=0in' + '\n\n')
	f.write(r'\begin{document}' + '\n')
	
	for spell in spells:
		f.write('\n\n')
		f.write(r'\noindent {\bf\large '+spell['name'] + r'} \\' + '\n') 
		f.write('Level ' + spell['level'] + r' \quad ')
		f.write(spell['school'] + r' \quad Cast: ' + spell['casting time'] + r'\\' + '\n')
		f.write(r'Range: ' + spell['range'] + r' \quad ' + spell['components'] + r'\\' + '\n')
		f.write(r'Duration: ' + spell['duration'] + r' \quad ' + spell['material_components'] + r'\\' + '\n')
		f.write('-' + spell['desc'] + r'\\' + '\n')
		if 'higher_level_desc' in spell.keys():
			f.write('-' + spell['higher_level_desc'] + r'\\' + '\n')
		f.write('A ')
		for cl in spell['classes']:
			f.write(cl)
			if cl != spell['classes'][-1]:
				f.write(r', ')
		f.write(' spell. (' + spell['page'] +  r') \\' + '\n')

	f.write(r'\end{document}' + '\n')

# Compile LaTeX to pdf format
subprocess.run(["pdflatex","-output-directory=LatexCompile","LatexCompile/spells_text.tex"])

