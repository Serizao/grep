import sys
import re
import os
import argparse
__version__ = "1.0"
# -*- coding: utf-8 -*-


class use:

	def main(self, args): #fonction de recherche classique
		retour=[]
		a=0
		fichier=args['fichier']
		chaine=args['expression']
		fichier = open(fichier,"r").read()
		for ligne in fichier:
			a+=1
			if not args['invert_match']:
				if chaine in ligne:
					if args['line_number']:
							print(a, ligne)
					else:
						print(ligne)
				
			else:
				if not chaine in ligne:

					if args['line_number']:
							print(a, ligne)
					else:
						print(ligne)
				
		fichier.close()

	def regexsearch(self, args):#fonction de gestion des expression regulière
		regex=args['regexp']
		fichier=args['fichier']
		a=0
		print(fichier)
		fichier = open(fichier,"r")
		for ligne in fichier:
			if args['ignore_case']:
				ligne2=ligne.upper()
				regex2=regex.upper()
			else:
				ligne2=ligne
				regex2=regex
			a+=1
			if not args['invert_match']:
				if re.search(regex2,ligne2):
					if args['line_number']:
						print(a, ligne)
					elif args['recursive']:
						return 1
					else:
						print(ligne)
			else:
				if not re.search(regex2,ligne2):

					if args['line_number']:
						print(a, ligne)
					elif args['recursive']:
						return 1
					else:
						print(ligne)

	def split_regex(self, args): # fonction permettant de diviser les ligne de regex recus afin de les envoyer une a une a regexsearch
		regex=args['fixed_regexp']
		a=str.splitlines(regex)
		for i in a:
			args['regexp']=i
			self.regexsearch(args)
			
			

	def split_file(self, args):#même fonction que plus haut mais pour les fichier
		regfil=args['file']
		fichier = open(regfil,"r")
		for i in fichier:
			i = i.replace('\n', '').replace('\r', '')
			args['regexp']=i
			self.regexsearch(args)

	def recurse(self,args):
		path=u'.'
		for name in os.listdir(path):
			files=files=os.path.dirname(os.path.abspath(__file__))+""+name
			args['fichier']=files
		for (dir, _, files) in os.walk("."):
		    for f in files:
			    path = os.path.join(dir, f)
			    if os.path.exists(path):
			        files=os.path.dirname(os.path.abspath(__file__))+""+path[1:]
			        args['fichier']=files
			        self.regexsearch(args)

##############################parse des parametre
parser = argparse.ArgumentParser(description="Grep")
parser.add_argument('fichier', nargs='?', type=str, action="store", default="", help="fichier à ouvrir")
parser.add_argument('-e','--regexp', type=str, action="store", default="", help="expression reguliere a tester")
parser.add_argument('-F','--fixed-regexp', type=str, action="store", default="", help="expression reguliere separée par un retour a la ligne")
parser.add_argument('-f','--file', type=str, action="store", default="", help="expression reguliere separée par un retour a la ligne")
parser.add_argument('-v','--invert-match', action="store_true", help="selectionner leslignes sans correspondance")
parser.add_argument('-n','--line-number', action="store_true", help="affiche le numeros des ligne")
parser.add_argument('-i','--ignore-case', action="store_true", help="ignorer la distinction de la casse")
parser.add_argument('-r','--recursive', action="store_true", help="identique `a --directories=recurse")
parser.add_argument('--version','-V',action='version',version=__version__)
parser.add_argument('expression', nargs='?', type=str, action="store", default="", help="expression")
args = vars(parser.parse_args())
##############################choix des option par rapport aux parametre
a=use()
print(args)
if args['recursive']:
	a.recurse(args)
if args['regexp']:
	a.regexsearch(args)
if args['fixed_regexp']:
	a.split_regex(args)
if args['file']:
	a.split_file(args)
if args['expression']:
	a.main(args)









