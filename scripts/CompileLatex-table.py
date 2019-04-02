import json
import os, subprocess

# Load json
with open('../data/dnd_spells_clean.json','r') as f:
	spells = json.load(f)

# Ensure directory for LaTeX compilation
if not os.path.isdir("LatexCompile"):
	os.mkdir("LatexCompile")

# Write LaTex code for each spell
with open('LatexCompile/spells_table.tex','w') as f:
	f.write(r'\documentclass[11pt]{report}' + '\n\n')
	f.write(r'\usepackage{multicol,float}' + '\n\n')
	f.write(r'\oddsidemargin=0in' + '\n' + r'\evensidemargin=0in' +'\n')
	f.write(r'\topmargin=0in' + '\n')
	f.write(r'\begin{document}' + '\n\n')
	
	for spell in spells:
		f.write(r'\begin{table}[H]' + '\n')
		f.write('\t' + r'\begin{tabular}{||p{6cm}|p{6cm}||}' + '\n')
		f.write('\t\t' + r'\hline\hline' + '\n')
		f.write('\t\t' + r'\bf{'+spell['name'] + r'} & Level ' + spell['level'] + r'\\ \hline' + '\n')
		f.write('\t\t' + spell['school'] + r' & Cast: ' + spell['casting time'] + r'\\ \hline' + '\n')
		f.write('\t\t' + r'Range: ' + spell['range'] + r' & ' + spell['components'] + r'\\ \hline' + '\n')
		f.write('\t\t' + r'Duration: ' + spell['duration'] + r' & ' + spell['material_components'] + r'\\ \hline' + '\n')
		f.write('\t\t' + r'\multicolumn{2}{||p{12cm}||}{' + spell['desc'] + r'}\\ \hline' + '\n')
		if 'higher_level_desc' in spell.keys():
			f.write('\t\t' + r'\multicolumn{2}{||p{12cm}||}{' + spell['higher_level_desc'] + r'}\\ \hline' + '\n')
		f.write(spell['page'] + r' & ')
		for cl in spell['classes']:
			f.write(cl + r', ') 
		f.write(r'\\ \hline\hline' + '\n')
		f.write('\t' + r'\end{tabular}' + '\n')
		f.write(r'\end{table}' + '\n\n')

	f.write(r'\end{document}' + '\n')

# Compile LaTeX to pdf format
subprocess.run(["pdflatex","-output-directory=LatexCompile","LatexCompile/spells_table.tex"])

