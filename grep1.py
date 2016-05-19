import sys
import re
import argparse
__version__ = "1.0"



class use:

	def main(self, args):
		retour=[]
		fichier=args['fichier']
		chaine=r'',args['expression']
		fichier = open(fichier,"r")
		for ligne in fichier:
			if chaine in ligne:
				print(ligne)
				retour.append(ligne)
			return retour


		fichier.close()

	def regexsearch(self, fil, regex):
		fichier = open(fil,"r")
		for ligne in fichier:
			if re.search(regex,ligne):
				print(ligne)


##############################parse des parametre
parser = argparse.ArgumentParser(description="Grep")
parser.add_argument('fichier', nargs='?', type=str, action="store", default="", help="fichier à ouvrir")
parser.add_argument('expression', nargs='?', type=str, action="store", default="", help="expression")
parser.add_argument('-e','--regexp', type=str, action="store", default="", help="expression reguliere a tester")
parser.add_argument('--version','-v',action='version',version=__version__)
args = vars(parser.parse_args())
##############################choix des option par rapport aux parametre
a=use()
print args
if args['regexp']:
	a.regexsearch(args['fichier'],args['regexp'])





