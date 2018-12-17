#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import re
#Consigne Faire une fonction qui liste en donnant en paramètre une mutation et un chromosome toutes les positions où il y a cette mutation
file_name1="data/human_CEU.vcf"
with open(file_name1,"r") as vcf:
	file_read=vcf.readlines()


chromosome_ref={}
for line_vcf in file_read:
	if not line_vcf.startswith("#"):#si la ligne ne commence pas par # -> lecture de la ligne
		information=re.findall("\S+",line_vcf)
		#Instruction permettant de valider la présence d'informations pour chaque ligne
		if len(information)>0:
			chromosome=information[0]
		if len(information)==0:
			chromosome, position, identifiant,  ref, alt, qual="?", "?", "?", "?", "?", "?"
		if len(information)>1:
			position=information[1]
			print(position)
		if len(information)>2:
			identifiant=information[2]
		if len(information)>3:
			ref=information[3]
		if len(information)>4:
			alt=information[4]
		if len(information)>5:
			qual=information[5]
		
			liste_mutation=[]
			if chromosome in chromosome_ref:
				if position in chromosome_ref[chromosome].keys():
					liste_mutation.append(ref)
					liste_mutation.append(alt)
					liste_mutation.append(qual)
					chromosome_ref[chromosome][position]=liste_mutation
				else:
					liste_mutation.append(ref)
					liste_mutation.append(alt)
					liste_mutation.append(qual)
					chromosome_ref.get(chromosome)[position]=liste_mutation
			   
			else:
				liste_mutation.append(ref)
				liste_mutation.append(alt)
				liste_mutation.append(qual)
				chromosome_ref[chromosome]={}
				chromosome_ref[chromosome][position]=liste_mutation

			   

def position_mutation (chromosome, mutation):
	tableau_position = chromosome_ref[chromosome].keys()
	dic_position_info = chromosome_ref[chromosome]
	for position in tableau_position:
		tableau_info = dic_position_info[position]
		print (tableau_info[1])
		chain = re.search(mutation, tableau_info[1])

		if chain:
			print (position)


position_mutation("1", "INS")
